from scrapy.selector import Selector
from finance.spiders import Nini

from ..items import LoanItem


class ConsolidatedBankLoanSpider(Nini):
    name = "consbankloan"
    allowed_domains = ["http://www.consolidated-bank.com/"]
    start_urls = [
        "http://www.consolidated-bank.com/index.php?option=com_content&view=article&id=43&Itemid=79",
    ]

    institution_name = 'Consolidated'

    def parse(self, response):
        sel = Selector(response)
        base = sel.xpath('//*[@id="maincolumn"]/div')


        items = []

        item = LoanItem()
        item['loan_name'] = base.xpath('table[1]/tr/td[1]/text()').extract()
        items.append(item)
        for fet in base.xpath('table[2]/tr/td/ul[1]/li/span/text()').extract():
            item = LoanItem()
            item['features'] = fet
            items.append(item)
        for req in base.xpath('table[2]/tr/td/ul[2]/li/span/text()').extract():
            item = LoanItem()
            item['requirements'] = req
            items.append(item)

        return items
