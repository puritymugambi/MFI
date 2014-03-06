from scrapy.selector import Selector
from finance.spiders import Nini

from ..items import LoanItem

class BankofAfricaLoanSpider(Nini):
    name = "boabankloan"
    allowed_domains = ["boakenya.com"]
    start_urls = [
        "http://www.boakenya.com/personal-banking/loans-credit-facilities/other-loans/unsecured-personal-loan/",
    ]

    institution_name = 'Boa'

    def parse(self, response):
        sel = Selector(response)
        base = sel.xpath('//*[@id="post-619"]')
        benefits_ul, eligibility_ul, requirement_ul, features_ul = base.xpath("div[1]/ul")

        items = []
        item = LoanItem()
        item['loan_name'] = base.xpath('h1/text()').extract()[0]
        items.append(item)

        for loan_item in benefits_ul.xpath('li/text()').extract():
            item = LoanItem()
            item['benefits'] = loan_item
            items.append(item)

        for loan_item in eligibility_ul.xpath('li/text()').extract():
            item = LoanItem()
            item['eligibility'] = loan_item
            items.append(item)
        for loan_item in requirement_ul.xpath('li/text()').extract():
            item = LoanItem()
            item['requirements'] = loan_item
            items.append(item)
        for loan_item in features_ul.xpath('li/text()').extract():
            item = LoanItem()
            item['features'] = loan_item
            items.append(item)

        return items
