from scrapy.selector import Selector
from finance.spiders import Nini

from ..items import LoanItem


class StanChartBankLoanSpider(Nini):
    name = "stanchartbankloan"
    allowed_domains = ["sc.com/ke"]
    start_urls = [
        "https://www.sc.com/ke/borrow/loans-personal.html",
    ]

    institution_name = 'Stanchart'

    def parse(self, response):
        sel = Selector(response)
        base = sel.xpath('//*[@id="wrapper"]/article[2]')
        loan_st, features_st, eligibility_st, calculator, contact, bullet_data = base.xpath("section")

        items = []

        for loan_item in loan_st.xpath('div/div/ol/li/strong/text()').extract():
            item = LoanItem()
            item['loan_name'] = loan_item
            items.append(item)
        #[{"title": i.xpath('strong/text()').extract(),"desc": i.xpath('p/text()')} for i in loan_st.xpath('div/div/ol/li')]desc???

        for loan_item in features_st.xpath('div/div/ul/li/text()').extract():
            item = LoanItem()
            item['features'] = loan_item
            items.append(item)

        for loan_item in eligibility_st.xpath('div/div/ul/li/ul/li/text()').extract():
            item = LoanItem()
            item['eligibility'] = loan_item
            items.append(item)

        return items

