from scrapy.selector import Selector
from finance.spiders import Nini

from ..items import LoanItem


class ChaseBankLoanSpider(Nini):
    name = "chasebankloan"
    allowed_domains = ["chasebankkenya.co.ke"]
    start_urls = [
        "http://www.chasebankkenya.co.ke/products/loans-1",
    ]

    institution_name = 'Chase'

    def parse(self, response):
        sel = Selector(response)
        base = sel.xpath('//*[@id="content-content"]/div/div/table/tbody/tr')
        loan_td = base.xpath("td")

        items = []

        for i in loan_td:
            item = LoanItem()
            item['loan_name'] = i.xpath('div[1]/span/a/text()').extract()
            item['desc'] = i.xpath('div[2]/span/text()').extract()
            item['link'] = i.xpath('div[3]/span/a/@href').extract()
            items.append(item)

        return items



