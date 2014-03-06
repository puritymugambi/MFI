from scrapy.selector import Selector

from ..items import ForexItem
from finance.spiders import Nini

class NationalForexSpider(Nini):
    name = "nationalforex"
    allowed_domains = ["nationalbank.co.ke"]
    start_urls = [
        "http://www.nationalbank.co.ke/index.php/2013-05-24-10-08-17/exchange-rates",
    ]

    institution_name = 'NationalBureau'

    def parse(self, response):
        sel = Selector(response)
        base = sel.xpath('//*[@id="nbkMainbodyWrap"]/div/table/tbody/tr[2]/td/table/tbody')
        
        #currency_span = base.xpath("span")

        items = []

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[2]/td[1]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[2]/td[6]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[2]/td[7]/span/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[3]/td[1]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[3]/td[6]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[3]/td[7]/span/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[4]/td[1]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[4]/td[6]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[4]/td[7]/span/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[5]/td[1]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[5]/td[6]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[5]/td[7]/span/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[6]/td[1]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[6]/td[6]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[6]/td[7]/span/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[7]/td[1]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[7]/td[6]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[7]/td[7]/span/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[8]/td[1]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[8]/td[6]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[8]/td[7]/span/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[9]/td[1]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[9]/td[6]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[9]/td[7]/span/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[10]/td[1]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[10]/td[6]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[10]/td[7]/span/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[11]/td[1]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[11]/td[6]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[11]/td[7]/span/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[12]/td[1]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[12]/td[6]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[12]/td[7]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[13]/td[1]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[13]/td[6]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[13]/td[7]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[14]/td[1]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[14]/td[6]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[14]/td[7]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[15]/td[1]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[15]/td[6]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[15]/td[7]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[16]/td[1]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[16]/td[6]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[16]/td[7]/text()').extract()[0]
        items.append(item)

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[17]/td[1]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[17]/td[6]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[17]/td[7]/text()').extract()[0]
        items.append(item)

        return items

