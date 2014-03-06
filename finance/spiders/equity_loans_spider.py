from scrapy.selector import Selector
from finance.spiders import Nini

from ..items import LoanItem


class EquityBankLoanSpider(Nini):
    name = "equitybankloan"
    allowed_domains = ["equitybank.co.ke"]
    start_urls = [
        "http://www.equitybank.co.ke/index.php/loans/consumer-loans",
    ]

    institution_name = 'Equity'

    def parse(self, response):
        sel = Selector(response)
        base = sel.xpath('//*[@id="main"]/div/div[2]/div/table/tbody')
        loan_tr = base.xpath("tr")

        items = []

        for i in loan_tr.xpath('td'):
            item = LoanItem()
            item["loan_name"] = i.xpath('p[1]/strong/text()').extract()[0]
            item["desc"] = i.xpath('p[2]/text()').extract()[0]
            items.append(item)

        #"benefits":i.xpath('ol/li/text()').extract()


        return items


