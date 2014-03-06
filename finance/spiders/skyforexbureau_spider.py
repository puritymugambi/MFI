from scrapy.selector import Selector

from ..items import ForexItem
from finance.spiders import Nini


class SkyForexSpider(Nini):
    name = "skyforex"
    allowed_domains = ["skyforexbureau.com"]
    start_urls = [
        "http://www.skyforexbureau.com",
    ]

    institution_name = 'SkyBureau'

    def parse(self, response):
        sel = Selector(response)
        base = sel.xpath('//*[@id="exrates"]/table/tr[1]/td/table/tbody')
        currency_tr = base.xpath("tr")


        items = []

        for i in currency_tr:
            item = ForexItem()
            item['currency_name'] = i.xpath('td[2]/text()').extract()[0]
            item['buying_price'] = i.xpath('td[3]/text()').extract()[0]
            item['selling_price'] = i.xpath('td[4]/text()').extract()[0]
            items.append(item)

        return items
