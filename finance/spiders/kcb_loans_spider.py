from scrapy.selector import Selector
from finance.spiders import Nini

from ..items import KcbBankLoanItem as KBLI


class KcbBankLoanSpider(Nini):
    name = "kcbbankloan"
    allowed_domains = ["ke.kcbbankgroup.com/"]
    start_urls = [
        "http://ke.kcbbankgroup.com/personal-banking/borrowing/personal-loans/",
    ]


    def parse(self, response):
        sel = Selector(response)
        base = sel.xpath('//*[@id="main"]/div[1]/div[3]/div[1]/div[2]/table/tbody')
        title_tr, loan_tr, loan_tr, loan_tr, loan_tr, loan_tr = base.xpath("tr")

        item = KBLI()
        item['loans'] = [{"name": i.xpath('td[1]/h3/text()').extract(), "desc": i.xpath('td[1]/p/text()').extract(),
                          "link": i.xpath('td[1]/h3/a/@href').extract(), "benefits": i.xpath('td[2]/ul/li/text()'),
                          "requirements": i.xpath('td[3]/ul/li/text()')} for i in loan_tr]

        return item




