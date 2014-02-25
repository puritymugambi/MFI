from scrapy.spider import BaseSpider
from scrapy.selector import Selector

from ..items import NationalForexItem


class NationalForexSpider(BaseSpider):
    name = "nationalforex"
    allowed_domains = ["nationalbank.co.ke"]
    start_urls = [
        "http://www.nationalbank.co.ke/#",
    ]


    def parse(self, response):
        sel = Selector(response)
        base = sel.xpath('//*[@id="blankBM110"]/div[1]/marquee/span/span/span/a')
        
        #currency_span = base.xpath("span")

        item = NationalForexItem()

        currencies = []
        currencies.append({ 'name':base.xpath('span[1]/text()').extract(), 'prices': base.xpath('span[2]/text()').extract()})
        currencies.append({ 'name':base.xpath('span[3]/text()').extract(), 'prices': base.xpath('span[4]/text()').extract()})
        currencies.append({ 'name':base.xpath('span[5]/text()').extract(), 'prices': base.xpath('span[6]/text()').extract()})
        currencies.append({ 'name':base.xpath('span[7]/text()').extract(), 'prices': base.xpath('span[8]/text()').extract()})
        currencies.append({ 'name':base.xpath('span[9]/text()').extract(), 'prices': base.xpath('span[10]/text()').extract()})
        currencies.append({ 'name':base.xpath('span[11]/text()').extract(), 'prices': base.xpath('span[12]/text()').extract()})
        currencies.append({ 'name':base.xpath('span[13]/text()').extract(), 'prices': base.xpath('span[14]/text()').extract()})
        currencies.append({ 'name':base.xpath('span[15]/text()').extract(), 'prices': base.xpath('span[16]/text()').extract()})
 
        item['currencies'] = currencies
        return item

