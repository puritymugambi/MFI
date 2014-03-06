from scrapy.selector import Selector

from ..items import ForexItem
from finance.spiders import Nini


class CbaForexSpider(Nini):
    name = "cbaforex"
    allowed_domains = ["www.cbagroup.com/ke"]
    start_urls = [
        "http://www.cbagroup.com/ke/exchange-rate",
    ]

    institution_name = 'CbaBureau'

    def parse(self, response):
        sel = Selector(response)
        base = sel.xpath('//*[@id="keforex"]/table/tbody')



        items = []

        item = ForexItem()
        item['currency_name'] = base.xpath('tr[3]/td[2]/text()').extract()[0]
        item['buying_price'] = base.xpath('tr[3]/td[7]/text()').extract()[0]
        item['selling_price'] = base.xpath('tr[3]/td[8]/text()').extract()[0]
        items.append(item)


        return items