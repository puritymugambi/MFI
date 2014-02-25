from scrapy.selector import Selector
from finance.spiders import Nini

from ..items import EquityBankLoanItem as EBLI


class EquityBankLoanSpider(Nini):
    name = "equitybankloan"
    allowed_domains = ["equitybank.co.ke"]
    start_urls = [
        "http://www.equitybank.co.ke/index.php/loans/consumer-loans",
    ]


    def parse(self, response):
        sel = Selector(response)
        base = sel.xpath('//*[@id="main"]/div/div[2]/div/table/tbody')
        loan_tr = base.xpath("tr")

        item = EBLI()
        item['loans'] = [{"title": i.xpath('p[1]/strong/text()').extract(), "desc": i.xpath('p[2]/text()').extract()}
                         for i in loan_tr.xpath('td')]
        #"benefits":i.xpath('ol/li/text()').extract()


        return item


