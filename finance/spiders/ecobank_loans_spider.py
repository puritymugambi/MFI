from scrapy.selector import Selector
from finance.spiders import Nini

from ..items import LoanItem


class EcobankLoanSpider(Nini):
    name = "ecobankloan"
    allowed_domains = ["ecobank.com"]
    start_urls = [
        "http://www.ecobank.com/loans.aspx",
    ]

    institution_name = 'Eco'


    def parse(self, response):
        sel = Selector(response)
        defs, defs1 = sel.xpath('//div[@class="def"]/text()'), sel.xpath('//div[@class="def1"]/text()')

        #item = LoanItem()
        items = []
        item = LoanItem()
        item['loan_name'] = defs[0].extract()
        item['desc'] = defs1[1].extract()
        items.append(item)

        item = LoanItem()
        item['loan_name'] = defs[1].extract()
        item['desc'] = "".join([i.extract() for i in defs1[2:-1]])
        items.append(item)

        item = LoanItem()
        item['loan_name'] = defs[-1].extract()
        item['desc'] = defs1[-1].extract()
        items.append(item)
        #item['loans'] = loans
        return items

