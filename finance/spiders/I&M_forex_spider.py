from scrapy.selector import Selector

from ..items import ForexItem
from finance.spiders import Nini


class InMForexSpider(Nini):
    name = "imforex"
    allowed_domains = ["www.imbank.com"]
    start_urls = [
        "https://www.imbank.com/personal/foreign-exchange/",
    ]

    institution_name = 'IMBureau'

    def parse(self, response):
        sel = Selector(response)
        base = sel.xpath('/html/body/div[2]/div/section/article/div[1]/table')

        #currency_span = base.xpath("span")



        items = []

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[2]/th[2]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[2]/td[1]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[2]/td[2]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[3]/th[2]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[3]/td[1]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[3]/td[2]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[4]/th[2]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[4]/td[1]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[4]/td[2]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[5]/th[2]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[5]/td[1]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[5]/td[2]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[6]/th[2]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[6]/td[1]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[6]/td[2]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[7]/th[2]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[7]/td[1]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[7]/td[2]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[8]/th[2]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[8]/td[1]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[8]/td[2]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[9]/th[2]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[9]/td[1]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[9]/td[2]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[10]/th[2]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[10]/td[1]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[10]/td[2]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[11]/th[2]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[11]/td[1]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[11]/td[2]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[12]/th[2]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[12]/td[1]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[12]/td[2]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[13]/th[2]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[13]/td[1]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[13]/td[2]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[14]/th[2]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[14]/td[1]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[14]/td[2]/text()').extract()[0]
        items.append(item)


        item = ForexItem()
        item['currency_name'] = base.xpath('tr[15]/th[2]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[15]/td[1]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[15]/td[2]/text()').extract()[0]
        items.append(item)

        return items
