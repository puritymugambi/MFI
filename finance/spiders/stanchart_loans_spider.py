from scrapy.selector import Selector
from finance.spiders import Nini

from ..items import StanChartBankLoanItem as SCBLI


class StanChartBankLoanSpider(Nini):
    name = "stanchartbankloan"
    allowed_domains = ["sc.com/ke"]
    start_urls = [
        "https://www.sc.com/ke/borrow/loans-personal.html",
    ]


    def parse(self, response):
        sel = Selector(response)
        base = sel.xpath('//*[@id="wrapper"]/article[2]')
        loan_st, features_st, eligibility_st, calculator, contact, bullet_data = base.xpath("section")

        item = SCBLI()

        item['loans'] = loan_st.xpath('div/div/ol/li/strong/text()').extract()
        #[{"title": i.xpath('strong/text()').extract(),"desc": i.xpath('p/text()')} for i in loan_st.xpath('div/div/ol/li')]desc???
        item['features'] = [{"content": i.xpath('text()').extract(), "link": i.xpath('a/@href').extract()}
                            for i in features_st.xpath('div/div/ul/li')]
        item['eligibility'] = eligibility_st.xpath('div/div/ul/li/ul/li/text()').extract()

        return item

