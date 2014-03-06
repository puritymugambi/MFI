from scrapy.selector import Selector

from ..items import ForexItem
from finance.spiders import Nini

from ..utils import first


class BoaForexSpider(Nini):
    name = "boaforex"
    allowed_domains = ["www.boakenya.com/"]
    start_urls = [
        "http://www.boakenya.com/exchange-rates/",
    ]

    institution_name = 'BoaBureau'

    def parse(self, response):
        sel = Selector(response)
        base = sel.xpath('//*[@id="post-1088"]/div[1]/table/tbody')

        #currency_span = base.xpath("span")



        items = []

        item = ForexItem()
        item['currency_name'] = first(base.xpath('tr[3]/td[1]/strong/text()').extract())
        item['buying_price'] = first(base.xpath('tr[3]/td[4]/text()').extract())
        item['selling_price'] = first(base.xpath('tr[3]/td[5]/text()').extract())
        items.append(item)

        item = ForexItem()
        item['currency_name'] = first(base.xpath('tr[4]/td[1]/strong/text()').extract())
        item['buying_price'] = first(base.xpath('tr[4]/td[4]/text()').extract())
        item['selling_price'] = first(base.xpath('tr[4]/td[5]/text()').extract())
        items.append(item)

        item = ForexItem()
        item['currency_name'] = first(base.xpath('tr[5]/td[1]/strong/text()').extract())
        item['buying_price'] = first(base.xpath('tr[5]/td[4]/text()').extract())
        item['selling_price'] = first(base.xpath('tr[5]/td[5]/text()').extract())
        items.append(item)

        item = ForexItem()
        item['currency_name'] = first(base.xpath('tr[6]/td[1]/strong/text()').extract())
        item['buying_price'] = first(base.xpath('tr[6]/td[4]/text()').extract())
        item['selling_price'] = first(base.xpath('tr[6]/td[5]/text()').extract())
        items.append(item)

        item = ForexItem()
        item['currency_name'] = first(base.xpath('tr[7]/td[1]/strong/text()').extract())
        item['buying_price'] = first(base.xpath('tr[7]/td[4]/text()').extract())
        item['selling_price'] = first(base.xpath('tr[7]/td[5]/text()').extract())
        items.append(item)

        item = ForexItem()
        item['currency_name'] = first(base.xpath('tr[8]/td[1]/strong/text()').extract())
        item['buying_price'] = first(base.xpath('tr[8]/td[4]/text()').extract())
        item['selling_price'] = first(base.xpath('tr[8]/td[5]/text()').extract())
        items.append(item)

        item = ForexItem()
        item['currency_name'] = first(base.xpath('tr[9]/td[1]/strong/text()').extract())
        item['buying_price'] = first(base.xpath('tr[9]/td[4]/text()').extract())
        item['selling_price'] = first(base.xpath('tr[9]/td[5]/text()').extract())
        items.append(item)

        item = ForexItem()
        item['currency_name'] = first(base.xpath('tr[10]/td[1]/strong/text()').extract())
        item['buying_price'] = first(base.xpath('tr[10]/td[4]/text()').extract())
        item['selling_price'] = first(base.xpath('tr[10]/td[5]/text()').extract())
        items.append(item)

        item = ForexItem()
        item['currency_name'] = first(base.xpath('tr[11]/td[1]/strong/text()').extract())
        item['buying_price'] = first(base.xpath('tr[11]/td[4]/text()').extract())
        item['selling_price'] = first(base.xpath('tr[11]/td[5]/text()').extract())
        items.append(item)

        item = ForexItem()
        item['currency_name'] = first(base.xpath('tr[12]/td[1]/strong/text()').extract())
        item['buying_price'] = first(base.xpath('tr[12]/td[4]/text()').extract())
        item['selling_price'] = first(base.xpath('tr[12]/td[5]/text()').extract())
        items.append(item)

        return items
