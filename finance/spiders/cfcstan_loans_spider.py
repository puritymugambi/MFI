from scrapy.selector import Selector
from finance.spiders import Nini

from ..items import CfcstanbicBankLoanItem as CBLI


class CfcstanbicBankLoanSpider(Nini):
    name = "cfcbankloan"
    allowed_domains = ["cfcstanbicbank.co.ke"]
    start_urls = [
        "http://www.cfcstanbicbank.co.ke/Kenya/Personal/Borrowing",
    ]


    def parse(self, response):
        sel = Selector(response)
        base = sel.xpath('//*[@id="products"]')
        #loan_ul, requirement_ul, contacts, form_ul = base.xpath("ul")


        item = CBLI()
        item['loans'] = [{"name": i.xpath('h1/text()').extract(), "desc": i.xpath('p/text()').extract(),
                          "link": i.xpath('p/a/@href')}
                         for i in base]

        return item

