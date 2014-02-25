from scrapy.spider import BaseSpider
from scrapy.selector import Selector

from ..items import NseItem


class RichSpider(BaseSpider):
    name = "rich"
    allowed_domains = ["rich.co.ke"]
    start_urls = [
        "http://www.rich.co.ke/",
    ]


    def parse(self, response):
        sel = Selector(response)
        base = sel.xpath('/html/body/center/table[2]/tbody/tr/td[2]/table/tbody/tr/td/iframe')

        item = NseItem()
        item['stocks'] = base.extract()

        return item

