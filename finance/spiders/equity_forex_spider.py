from scrapy.selector import Selector

from ..items import ForexItem
from finance.spiders import Nini


class EquityForexSpider(Nini):
    name = "equityforex"
    allowed_domains = ["equitybank.co.ke"]
    start_urls = [
        "http://www.equitybank.co.ke/",
    ]

    institution_name = 'EquityBureau'

    def parse(self, response):
        sel = Selector(response)
        base = sel.xpath('//*[@id="banner"]/div/div[2]/div[2]/div[1]/div/marquee')

        #currency_span = base.xpath("span")



        items = []

        item = ForexItem()
        item['currency_name'] = base.xpath('span[1]/text()').extract()[0]
        item['buying_price'] = base.xpath('strong[1]/text()').extract()[0]
        item['selling_price'] = base.xpath('strong[2]/text()').extract()[0]
        items.append(item)


        item = ForexItem()
        item['currency_name'] = base.xpath('span[2]/text()').extract()[0]
        item['buying_price'] = base.xpath('strong[3]/text()').extract()[0]
        item['selling_price'] = base.xpath('strong[4]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('span[3]/text()').extract()[0]
        item['buying_price'] = base.xpath('strong[5]/text()').extract()[0]
        item['selling_price'] = base.xpath('strong[6]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('span[4]/text()').extract()[0]
        item['buying_price'] = base.xpath('strong[7]/text()').extract()[0]
        item['selling_price'] = base.xpath('strong[8]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('span[5]/text()').extract()[0]
        item['buying_price'] = base.xpath('strong[9]/text()').extract()[0]
        item['selling_price'] = base.xpath('strong[10]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('span[6]/text()').extract()[0]
        item['buying_price'] = base.xpath('strong[11]/text()').extract()[0]
        item['selling_price'] = base.xpath('strong[12]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('span[7]/text()').extract()[0]
        item['buying_price'] = base.xpath('strong[13]/text()').extract()[0]
        item['selling_price'] = base.xpath('strong[14]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('span[8]/text()').extract()[0]
        item['buying_price'] = base.xpath('strong[15]/text()').extract()[0]
        item['selling_price'] = base.xpath('strong[16]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('span[9]/text()').extract()[0]
        item['buying_price'] = base.xpath('strong[17]/text()').extract()[0]
        item['selling_price'] = base.xpath('strong[18]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('span[10]/text()').extract()[0]
        item['buying_price'] = base.xpath('strong[19]/text()').extract()[0]
        item['selling_price'] = base.xpath('strong[20]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('span[11]/text()').extract()[0]
        item['buying_price'] = base.xpath('strong[21]/text()').extract()[0]
        item['selling_price'] = base.xpath('strong[22]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('span[12]/text()').extract()[0]
        item['buying_price'] = base.xpath('strong[23]/text()').extract()[0]
        item['selling_price'] = base.xpath('strong[24]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('span[13]/text()').extract()[0]
        item['buying_price'] = base.xpath('strong[25]/text()').extract()[0]
        item['selling_price'] = base.xpath('strong[26]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('span[14]/text()').extract()[0]
        item['buying_price'] = base.xpath('strong[27]/text()').extract()[0]
        item['selling_price'] = base.xpath('strong[28]/text()').extract()[0]
        items.append(item)

        item['currency_name'] = base.xpath('span[15]/text()').extract()[0]
        item['buying_price'] = base.xpath('strong[29]/text()').extract()[0]
        item['selling_price'] = base.xpath('strong[30]/text()').extract()[0]
        items.append(item)


        return items

