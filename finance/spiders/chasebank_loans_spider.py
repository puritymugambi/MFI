from scrapy.selector import Selector
from finance.spiders import Nini

from ..items import ChaseBankLoanItem as CBLI


class ChaseBankLoanSpider(Nini):
    name = "chasebankloan"
    allowed_domains = ["chasebankkenya.co.ke"]
    start_urls = [
        "http://www.chasebankkenya.co.ke/products/loans-1",
    ]


    def parse(self, response):
        sel = Selector(response)
        base = sel.xpath('//*[@id="content-content"]/div/div/table/tbody/tr')
        loan_td = base.xpath("td")

        item = CBLI()
        item['loans'] = [
            {"name": i.xpath('div[1]/span/a/text()').extract()[0], "desc": i.xpath('div[2]/span/text()').extract(),
             "details": i.xpath('div[3]/span/a/@href').extract()} for i in loan_td]

        return item



