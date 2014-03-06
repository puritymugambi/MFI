from scrapy.selector import Selector

from ..items import ForexItem
from finance.spiders import Nini


class DevtForexSpider(Nini):
    name = "devtforex"
    allowed_domains = ["http://www.devbank.com/"]
    start_urls = [
        "http://www.devbank.com/",
    ]

    institution_name = 'DevtBureau'

    def parse(self, response):
        sel = Selector(response)
        base = sel.xpath('/html/body/table/tr/td/table/tr[6]/td/table/tr/td[3]/table/tr[6]/td/table/tr[12]/td[2]/table')

        #currency_span = base.xpath("span")



        items = []

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[2]/td[2]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[2]/td[3]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[2]/td[4]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[3]/td[2]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[3]/td[3]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[3]/td[4]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[4]/td[2]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[4]/td[3]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[4]/td[4]/text()').extract()[0]
        items.append(item)

        return items


