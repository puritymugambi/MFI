from scrapy.selector import Selector
from finance.spiders import Nini

from ..items import BarclaysBankLoanItem as BBLI


class BarclaysBankLoanSpider(Nini):
    name = "barclaysbankloan"
    allowed_domains = ["barclays.co.ke"]
    start_urls = [
        "http://www.barclays.co.ke/personal/loan/index.html",
    ]

    def parse(self, response):
        sel = Selector(response)
        base = sel.xpath('//*[@id="tabs"]/div[2]/section')
        loan_div = base.xpath("div")
        items = []
        for i in loan_div:
            item = BBLI()
            item["link"] = i.xpath('div/nav/a/@href').extract()[0]
            item["loan_name"] = i.xpath('div/h2/text()').extract()[0]
            item["desc"] = i.xpath('div/div/p/text()').extract()[0]
            items.append(item)

        return items
