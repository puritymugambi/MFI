from scrapy.selector import Selector

from ..items import ForexItem
from finance.spiders import Nini


class PrimeForexSpider(Nini):
    name = "primeforex"
    allowed_domains = ["www.primebank.co.ke/"]
    start_urls = [
        "http://www.primebank.co.ke/",
    ]

    institution_name = 'PrimeBureau'

    def parse(self, response):
        sel = Selector(response)
        base = sel.xpath('/html/body/table/tr[1]/td[1]/table[2]/tr[2]/td/table[1]/tr[2]/td[1]/table/tr/td/table')
        items = []

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[2]/td[1]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[2]/td[2]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[2]/td[3]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[3]/td[1]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[3]/td[2]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[3]/td[3]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[4]/td[1]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[4]/td[2]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[4]/td[3]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[5]/td[1]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[5]/td[2]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[5]/td[3]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[6]/td[1]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[6]/td[2]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[6]/td[3]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[7]/td[1]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[7]/td[2]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[7]/td[3]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[8]/td[1]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[8]/td[2]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[8]/td[3]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[9]/td[1]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[9]/td[2]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[9]/td[3]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[10]/td[1]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[10]/td[2]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[10]/td[3]/text()').extract()[0]
        items.append(item)

        return items