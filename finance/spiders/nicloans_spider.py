from scrapy.selector import Selector
from finance.spiders import Nini

from ..items import LoanItem

class NicBankLoanSpider(Nini):
    name = "nicbankloan"
    allowed_domains = ["http://www.nic-bank.com/main/"]
    start_urls = [
        "http://www.nic-bank.com/main/borrow/personal/",
    ]

    institution_name = 'Nic'

    def parse(self, response):
        sel = Selector(response)
        base = sel.xpath('//div[@id="mainstuff"]/div[2]/div[1]')
        loan_ul, requirement_ul, contacts, form_ul = base.xpath("ul")

        items = []

        #item['loan_name'] = loan_ul.xpath('li/text()').extract()[0:5]

        #messin around
        for loan_item in loan_ul.xpath('li/text()').extract():
            item = LoanItem()
            item['loan_name'] = loan_item
            items.append(item)

        for loan_item in requirement_ul.xpath('li/text()').extract():
            item = LoanItem()
            item['requirements'] = loan_item
            items.append(item)

        for i in form_ul.xpath('li').extract():
            item = LoanItem()
            item['forms'] = i
            #[{"txt": i.xpath('text()').extract(), "lnk": i.xpath('a/@href').extract()}]
            items.append(item)

        return items
