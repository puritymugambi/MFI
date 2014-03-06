from scrapy.selector import Selector

from ..items import ForexItem
from finance.spiders import Nini


class DtbForexSpider(Nini):
    name = "dtbforex"
    allowed_domains = ["www.dtbk.dtbafrica.com"]
    start_urls = [
        "http://www.dtbk.dtbafrica.com/forex.aspx",
    ]

    institution_name = 'DtbBureau'

    def parse(self, response):
        sel = Selector(response)
        base = sel.xpath('//*[@id="rates-table"]')

        #currency_span = base.xpath("span")



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

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[11]/td[1]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[11]/td[2]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[11]/td[3]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[12]/td[1]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[12]/td[2]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[12]/td[3]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[13]/td[1]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[13]/td[2]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[13]/td[3]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[14]/td[1]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[14]/td[2]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[14]/td[3]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[15]/td[1]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[15]/td[2]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[15]/td[3]/text()').extract()[0]
        items.append(item)


        return items