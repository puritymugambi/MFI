from scrapy.selector import Selector

from ..items import ForexItem
from finance.spiders import Nini


class FinaForexSpider(Nini):
    name = "finaforex"
    allowed_domains = ["http://gtbank.co.ke/"]
    start_urls = [
        "http://gtbank.co.ke/",
    ]

    institution_name = 'FinaBureau'

    def parse(self, response):
        sel = Selector(response)
        base = sel.xpath('//*[@id="featured-right"]/div[1]/table')


        items = []

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[1]/td[2]/div/span/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[2]/td[2]/div/span/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[3]/td[2]/div/span/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[1]/td[3]/div/span/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[2]/td[3]/div/span/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[3]/td[3]/div/span/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[1]/td[4]/div/span/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[2]/td[4]/div/span/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[3]/td[4]/div/span/text()').extract()[0]
        items.append(item)

        return items