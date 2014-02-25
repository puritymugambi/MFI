from scrapy.selector import Selector
from finance.spiders import Nini

from ..items import NicBankLoanItem as NBLI


class NicBankLoanSpider(Nini):
    name = "nicbankloan"
    allowed_domains = ["nic-bank.com"]
    start_urls = [
        "http://www.nic-bank.com/borrow/personal/",
    ]


    def parse(self, response):
        sel = Selector(response)
        base = sel.xpath('//div[@id="mainstuff"]/div[2]/div[1]')
        loan_ul, requirement_ul, contacts, form_ul = base.xpath("ul")

        item = NBLI()
        item['loans'] = loan_ul.xpath('li/text()').extract()
        item['requirements'] = requirement_ul.xpath('li/text()').extract()
        item['forms'] = [{"txt": i.xpath('text()').extract()[0], "lnk": i.xpath('a/@href').extract()[0]}
                         for i in form_ul.xpath('li')]

        return item
