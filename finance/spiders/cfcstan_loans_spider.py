from scrapy.selector import Selector
from finance.spiders import Nini

from ..items import LoanItem


class CfcstanbicBankLoanSpider(Nini):
    name = "cfcbankloan"
    allowed_domains = ["cfcstanbicbank.co.ke"]
    start_urls = [
        "http://www.cfcstanbicbank.co.ke/Kenya/Personal/Borrowing",
    ]

    institution_name = 'Cfc'

    def parse(self, response):
        sel = Selector(response)
        base = sel.xpath('//*[@id="products"]')
        #loan_ul, requirement_ul, contacts, form_ul = base.xpath("ul")

        items = []

        item = LoanItem()
        item['loan_name'] = base.xpath('h1[1]/text()').extract()
        item['desc'] = base.xpath('p[3]/text()').extract()
        items.append(item)

        item = LoanItem()
        item['loan_name'] = base.xpath('h1[2]/text()').extract()
        item['desc'] = base.xpath('p[5]/text()').extract()
        items.append(item)

        item = LoanItem()
        item['loan_name'] = base.xpath('h1[3]/text()').extract()
        item['desc'] = base.xpath('p[7]/text()').extract()
        items.append(item)

        return items

