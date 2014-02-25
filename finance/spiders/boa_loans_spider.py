from scrapy.selector import Selector
from finance.spiders import Nini

from ..items import BankofAfricaLoanItem as BALI


class BankofAfricaLoanSpider(Nini):
    name = "boabankloan"
    allowed_domains = ["boakenya.com"]
    start_urls = [
        "http://www.boakenya.com/?page_id=127",
    ]


    def parse(self, response):
        sel = Selector(response)
        base = sel.xpath('//*[@id="content"]/div')
        benefits_ul, requirement_ul, features_ul = base.xpath("ul")

        item = BALI()
        item['benefits'] = benefits_ul.xpath('li/text()').extract()
        item['requirements'] = requirement_ul.xpath('li/text()').extract()
        item['features'] = features_ul.xpath('li/text()').extract()

        return item

