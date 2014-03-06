#from scrapy.spider import Spider
from scrapy.selector import Selector
from finance.spiders import Nini

from ..items import StockItem


class NellyCapitalSpider(Nini):
    name = "nellycapital"
    allowed_domains = ["nellydata.com/CapitalFM/livedata.asp"]
    start_urls = [
        "http://www.nellydata.com/CapitalFM/livedata.asp",
    ]

    institution_name = 'NellyCapital'

    def parse(self, response):
        sel = Selector(response)
        base = sel.xpath('//div[@id="livedata"]/table')

        items = []

        item = StockItem()
        item['name'] = base.xpath('tr[3]/td[2]/strong/text()').extract()[0]
        item['previous_price'] = base.xpath('tr[3]/td[3]/text()').extract()[0]
        item['current_price'] = base.xpath('tr[3]/td[4]/text()').extract()[0]
        items.append(item)

        item = StockItem()
        item['name'] = base.xpath('tr[4]/td[2]/strong/text()').extract()[0]
        item['previous_price'] = base.xpath('tr[4]/td[3]/text()').extract()[0]
        item['current_price'] = base.xpath('tr[4]/td[4]/text()').extract()[0]
        items.append(item)

        item = StockItem()
        item['name'] = base.xpath('tr[5]/td[2]/strong/text()').extract()[0]
        item['previous_price'] = base.xpath('tr[5]/td[3]/text()').extract()[0]
        item['current_price'] = base.xpath('tr[5]/td[4]/text()').extract()[0]
        items.append(item)

        item = StockItem()
        item['name'] = base.xpath('tr[6]/td[2]/strong/text()').extract()[0]
        item['previous_price'] = base.xpath('tr[6]/td[3]/text()').extract()[0]
        item['current_price'] = base.xpath('tr[6]/td[4]/text()').extract()[0]
        items.append(item)


        item = StockItem()
        item['name'] = base.xpath('tr[7]/td[2]/strong/text()').extract()[0]
        item['previous_price'] = base.xpath('tr[7]/td[3]/text()').extract()[0]
        item['current_price'] = base.xpath('tr[7]/td[4]/text()').extract()[0]
        items.append(item)

        item = StockItem()
        item['name'] = base.xpath('tr[8]/td[2]/strong/text()').extract()[0]
        item['previous_price'] = base.xpath('tr[8]/td[3]/text()').extract()[0]
        item['current_price'] = base.xpath('tr[8]/td[4]/text()').extract()[0]
        items.append(item)


        item = StockItem()
        item['name'] = base.xpath('tr[9]/td[2]/strong/text()').extract()[0]
        item['previous_price'] = base.xpath('tr[9]/td[3]/text()').extract()[0]
        item['current_price'] = base.xpath('tr[9]/td[4]/text()').extract()[0]
        items.append(item)

        item = StockItem()
        item['name'] = base.xpath('tr[10]/td[2]/strong/text()').extract()[0]
        item['previous_price'] = base.xpath('tr[10]/td[3]/text()').extract()[0]
        item['current_price'] = base.xpath('tr[10]/td[4]/text()').extract()[0]
        items.append(item)

        item = StockItem()
        item['name'] = base.xpath('tr[11]/td[2]/strong/text()').extract()[0]
        item['previous_price'] = base.xpath('tr[11]/td[3]/text()').extract()[0]
        item['current_price'] = base.xpath('tr[11]/td[4]/text()').extract()[0]
        items.append(item)

        item = StockItem()
        item['name'] = base.xpath('tr[12]/td[2]/strong/text()').extract()[0]
        item['previous_price'] = base.xpath('tr[12]/td[3]/text()').extract()[0]
        item['current_price'] = base.xpath('tr[12]/td[4]/text()').extract()[0]
        items.append(item)

        item = StockItem()
        item['name'] = base.xpath('tr[13]/td[2]/strong/text()').extract()[0]
        item['previous_price'] =base.xpath('tr[13]/td[3]/text()').extract()[0]
        item['current_price'] = base.xpath('tr[13]/td[4]/text()').extract()[0]
        items.append(item)

        item = StockItem()
        item['name'] = base.xpath('tr[14]/td[2]/strong/text()').extract()[0]
        item['previous_price'] = base.xpath('tr[14]/td[3]/text()').extract()[0]
        item['current_price'] = base.xpath('tr[14]/td[4]/text()').extract()[0]
        items.append(item)

        item = StockItem()
        item['name'] = base.xpath('tr[15]/td[2]/strong/text()').extract()[0]
        item['previous_price'] = base.xpath('tr[15]/td[3]/text()').extract()[0]
        item['current_price'] = base.xpath('tr[15]/td[4]/text()').extract()[0]
        items.append(item)

        item = StockItem()
        item['name'] = base.xpath('tr[16]/td[2]/strong/text()').extract()[0]
        item['previous_price'] = base.xpath('tr[16]/td[3]/text()').extract()[0]
        item['current_price'] = base.xpath('tr[16]/td[4]/text()').extract()[0]
        items.append(item)

        item = StockItem()
        item['name'] = base.xpath('tr[17]/td[2]/strong/text()').extract()[0]
        item['previous_price'] = base.xpath('tr[17]/td[3]/text()').extract()[0]
        item['current_price'] = base.xpath('tr[17]/td[4]/text()').extract()[0]
        items.append(item)

        item = StockItem()
        item['name'] = base.xpath('tr[18]/td[2]/strong/text()').extract()[0]
        item['previous_price'] = base.xpath('tr[18]/td[3]/text()').extract()[0]
        item['current_price'] = base.xpath('tr[18]/td[4]/text()').extract()[0]
        items.append(item)

        item = StockItem()
        item['name'] = base.xpath('tr[19]/td[2]/strong/text()').extract()[0]
        item['previous_price'] = base.xpath('tr[19]/td[3]/text()').extract()[0]
        item['current_price'] = base.xpath('tr[19]/td[4]/text()').extract()[0]
        items.append(item)

        item = StockItem()
        item['name'] = base.xpath('tr[20]/td[2]/strong/text()').extract()[0]
        item['previous_price'] = base.xpath('tr[20]/td[3]/text()').extract()[0]
        item['current_price'] = base.xpath('tr[20]/td[4]/text()').extract()[0]
        items.append(item)

        item = StockItem()
        item['name'] = base.xpath('tr[21]/td[2]/strong/text()').extract()[0]
        item['previous_price'] = base.xpath('tr[21]/td[3]/text()').extract()[0]
        item['current_price'] = base.xpath('tr[21]/td[4]/text()').extract()[0]
        items.append(item)

        item = StockItem()
        item['name'] = base.xpath('tr[22]/td[2]/strong/text()').extract()[0]
        item['previous_price'] = base.xpath('tr[22]/td[3]/text()').extract()[0]
        item['current_price'] = base.xpath('tr[22]/td[4]/text()').extract()[0]
        items.append(item)

        item = StockItem()
        item['name'] = base.xpath('tr[23]/td[2]/strong/text()').extract()[0]
        item['previous_price'] = base.xpath('tr[23]/td[3]/text()').extract()[0]
        item['current_price'] = base.xpath('tr[23]/td[4]/text()').extract()[0]
        items.append(item)

        item = StockItem()
        item['name'] = base.xpath('tr[24]/td[2]/strong/text()').extract()[0]
        item['previous_price'] = base.xpath('tr[24]/td[3]/text()').extract()[0]
        item['current_price'] = base.xpath('tr[24]/td[4]/text()').extract()[0]
        items.append(item)

        item = StockItem()
        item['name'] = base.xpath('tr[25]/td[2]/strong/text()').extract()[0]
        item['previous_price'] = base.xpath('tr[25]/td[3]/text()').extract()[0]
        item['current_price'] = base.xpath('tr[25]/td[4]/text()').extract()[0]
        items.append(item)

        item = StockItem()
        item['name']= base.xpath('tr[26]/td[2]/strong/text()').extract()[0]
        item['previous_price']= base.xpath('tr[26]/td[3]/text()').extract()[0]
        item['current_price']= base.xpath('tr[26]/td[4]/text()').extract()[0]
        items.append(item)

        item = StockItem()
        item['name']= base.xpath('tr[27]/td[2]/strong/text()').extract()[0]
        item['previous_price']= base.xpath('tr[27]/td[3]/text()').extract()[0]
        item['current_price']= base.xpath('tr[27]/td[4]/text()').extract()[0]
        items.append(item)

        item = StockItem()
        item['name']= base.xpath('tr[28]/td[2]/strong/text()').extract()[0]
        item['previous_price']= base.xpath('tr[28]/td[3]/text()').extract()[0]
        item['current_price']= base.xpath('tr[28]/td[4]/text()').extract()[0]
        items.append(item)

        item = StockItem()
        item['name']= base.xpath('tr[29]/td[2]/strong/text()').extract()[0]
        item['previous_price']= base.xpath('tr[29]/td[3]/text()').extract()[0]
        item['current_price']= base.xpath('tr[29]/td[4]/text()').extract()[0]
        items.append(item)


        item = StockItem()
        item['name']= base.xpath('tr[30]/td[2]/strong/text()').extract()[0]
        item['previous_price']= base.xpath('tr[30]/td[3]/text()').extract()[0]
        item['current_price']= base.xpath('tr[30]/td[4]/text()').extract()[0]
        items.append(item)


        item = StockItem()
        item['name']= base.xpath('tr[31]/td[2]/strong/text()').extract()[0]
        item['previous_price']= base.xpath('tr[31]/td[3]/text()').extract()[0]
        item['current_price']= base.xpath('tr[31]/td[4]/text()').extract()[0]
        items.append(item)


        item = StockItem()
        item['name']= base.xpath('tr[32]/td[2]/strong/text()').extract()[0]
        item['previous_price']= base.xpath('tr[32]/td[3]/text()').extract()[0]
        item['current_price']= base.xpath('tr[32]/td[4]/text()').extract()[0]
        items.append(item)


        item = StockItem()
        item['name']= base.xpath('tr[33]/td[2]/strong/text()').extract()[0]
        item['previous_price']= base.xpath('tr[33]/td[3]/text()').extract()[0]
        item['current_price']= base.xpath('tr[33]/td[4]/text()').extract()[0]
        items.append(item)


        item = StockItem()
        item['name']= base.xpath('tr[34]/td[2]/strong/text()').extract()[0]
        item['previous_price']= base.xpath('tr[34]/td[3]/text()').extract()[0]
        item['current_price']= base.xpath('tr[34]/td[4]/text()').extract()[0]
        items.append(item)


        item = StockItem()
        item['name']= base.xpath('tr[35]/td[2]/strong/text()').extract()[0]
        item['previous_price']= base.xpath('tr[35]/td[3]/text()').extract()[0]
        item['current_price']= base.xpath('tr[35]/td[4]/text()').extract()[0]
        items.append(item)


        item = StockItem()
        item['name']= base.xpath('tr[36]/td[2]/strong/text()').extract()[0]
        item['previous_price']= base.xpath('tr[36]/td[3]/text()').extract()[0]
        item['current_price']= base.xpath('tr[36]/td[4]/text()').extract()[0]
        items.append(item)


        item = StockItem()
        item['name']= base.xpath('tr[37]/td[2]/strong/text()').extract()[0]
        item['previous_price']= base.xpath('tr[37]/td[3]/text()').extract()[0]
        item['current_price']= base.xpath('tr[37]/td[4]/text()').extract()[0]
        items.append(item)


        item = StockItem()
        item['name']= base.xpath('tr[38]/td[2]/strong/text()').extract()[0]
        item['previous_price']= base.xpath('tr[38]/td[3]/text()').extract()[0]
        item['current_price']= base.xpath('tr[38]/td[4]/text()').extract()[0]
        items.append(item)

        item = StockItem()
        item['name']= base.xpath('tr[39]/td[2]/strong/text()').extract()
        item['previous_price']= base.xpath('tr[39]/td[3]/text()').extract()[0]
        item['current_price']= base.xpath('tr[39]/td[4]/text()').extract()[0]
        items.append(item)

        item = StockItem()
        item['name']= base.xpath('tr[40]/td[2]/strong/text()').extract()[0]
        item['previous_price']= base.xpath('tr[40]/td[3]/text()').extract()[0]
        item['current_price']= base.xpath('tr[40]/td[4]/text()').extract()[0]
        items.append(item)

        item = StockItem()
        item['name']= base.xpath('tr[41]/td[2]/strong/text()').extract()[0]
        item['previous_price']= base.xpath('tr[41]/td[3]/text()').extract()[0]
        item['current_price']= base.xpath('tr[41]/td[4]/text()').extract()[0]
        items.append(item)

        item = StockItem()
        item['name']= base.xpath('tr[42]/td[2]/strong/text()').extract()[0]
        item['previous_price']= base.xpath('tr[42]/td[3]/text()').extract()[0]
        item['current_price']= base.xpath('tr[42]/td[4]/text()').extract()[0]
        items.append(item)


        item = StockItem()
        item['name']= base.xpath('tr[43]/td[2]/strong/text()').extract()[0]
        item['previous_price']= base.xpath('tr[43]/td[3]/text()').extract()[0]
        item['current_price']= base.xpath('tr[43]/td[4]/text()').extract()[0]
        items.append(item)

        item = StockItem()
        item['name']= base.xpath('tr[44]/td[2]/strong/text()').extract()[0]
        item['previous_price']= base.xpath('tr[44]/td[3]/text()').extract()[0]
        item['current_price']= base.xpath('tr[44]/td[4]/text()').extract()[0]
        items.append(item)

        item = StockItem()
        item['name']= base.xpath('tr[45]/td[2]/strong/text()').extract()[0]
        item['previous_price']= base.xpath('tr[45]/td[3]/text()').extract()[0]
        item['current_price']= base.xpath('tr[45]/td[4]/text()').extract()[0]
        items.append(item)

        item = StockItem()
        item['name'] = base.xpath('tr[46]/td[2]/strong/text()').extract()[0]
        item['previous_price'] =  base.xpath('tr[46]/td[3]/text()').extract()[0]
        item['current_price'] = base.xpath('tr[46]/td[4]/text()').extract()[0]
        items.append(item)

        item = StockItem()
        item['name'] = base.xpath('tr[47]/td[2]/strong/text()').extract()[0]
        item['previous_price'] = base.xpath('tr[47]/td[3]/text()').extract()[0]
        item['current_price'] = base.xpath('tr[47]/td[4]/text()').extract()[0]
        items.append(item)

        item = StockItem()
        item['name'] = base.xpath('tr[48]/td[2]/strong/text()').extract()[0]
        item['previous_price'] = base.xpath('tr[48]/td[3]/text()').extract()[0]
        item['current_price'] = base.xpath('tr[48]/td[4]/text()').extract()[0]
        items.append(item)

        item = StockItem()
        item['name']= base.xpath('tr[49]/td[2]/strong/text()').extract()[0]
        item['previous_price'] = base.xpath('tr[49]/td[3]/text()').extract()[0]
        item['current_price'] = base.xpath('tr[49]/td[4]/text()').extract()[0]
        items.append(item)

        item = StockItem()
        item['name'] = base.xpath('tr[50]/td[2]/strong/text()').extract()[0]
        item['previous_price'] = base.xpath('tr[50]/td[3]/text()').extract()[0]
        item['current_price'] = base.xpath('tr[50]/td[4]/text()').extract()[0]
        items.append(item)

        item = StockItem()
        item['name']= base.xpath('tr[51]/td[2]/strong/text()').extract()[0]
        item['previous_price'] = base.xpath('tr[51]/td[3]/text()').extract()[0]
        item['current_price'] = base.xpath('tr[51]/td[4]/text()').extract()[0]
        items.append(item)


        item = StockItem()
        item['name'] = base.xpath('tr[52]/td[2]/strong/text()').extract()[0]
        item['previous_price'] =base.xpath('tr[52]/td[3]/text()').extract()[0]
        item['current_price'] = base.xpath('tr[52]/td[4]/text()').extract()[0]
        items.append(item)


        item = StockItem()
        item['name'] = base.xpath('tr[53]/td[2]/strong/text()').extract()[0]
        item['previous_price'] = base.xpath('tr[53]/td[3]/text()').extract()[0]
        item['current_price'] = base.xpath('tr[53]/td[4]/text()').extract()[0]
        items.append(item)


        item = StockItem()
        item['name'] = base.xpath('tr[54]/td[2]/strong/text()').extract()[0]
        item['previous_price'] = base.xpath('tr[54]/td[3]/text()').extract()[0]
        item['current_price'] = base.xpath('tr[54]/td[4]/text()').extract()[0]
        items.append(item)


        item = StockItem()
        item['name'] = base.xpath('tr[55]/td[2]/strong/text()').extract()[0]
        item['previous_price'] = base.xpath('tr[55]/td[3]/text()').extract()[0]
        item['current_price'] = base.xpath('tr[55]/td[4]/text()').extract()[0]
        items.append(item)


        item = StockItem()
        item['name'] = base.xpath('tr[56]/td[2]/strong/text()').extract()[0]
        item['previous_price'] = base.xpath('tr[56]/td[3]/text()').extract()[0]
        item['current_price'] = base.xpath('tr[56]/td[4]/text()').extract()[0]
        items.append(item)


        item = StockItem()
        item['name'] = base.xpath('tr[57]/td[2]/strong/text()').extract()[0]
        item['previous_price'] = base.xpath('tr[57]/td[3]/text()').extract()[0]
        item['current_price'] = base.xpath('tr[57]/td[4]/text()').extract()[0]
        items.append(item)

        item = StockItem()
        item['name'] = base.xpath('tr[58]/td[2]/strong/text()').extract()[0]
        item['previous_price'] = base.xpath('tr[58]/td[3]/text()').extract()[0]
        item['current_price'] = base.xpath('tr[58]/td[4]/text()').extract()[0]
        items.append(item)

        item = StockItem()
        item['name'] = base.xpath('tr[59]/td[2]/strong/text()').extract()[0]
        item['previous_price'] = base.xpath('tr[59]/td[3]/text()').extract()[0]
        item['current_price'] = base.xpath('tr[59]/td[4]/text()').extract()[0]
        items.append(item)

        item = StockItem()
        item['name'] = base.xpath('tr[60]/td[2]/strong/text()').extract()[0]
        item['previous_price'] = base.xpath('tr[60]/td[3]/text()').extract()[0]
        item['current_price'] = base.xpath('tr[60]/td[4]/text()').extract()[0]
        items.append(item)

        item = StockItem()
        item['name'] = base.xpath('tr[61]/td[2]/strong/text()').extract()[0]
        item['previous_price'] = base.xpath('tr[61]/td[3]/text()').extract()[0]
        item['current_price'] = base.xpath('tr[61]/td[4]/text()').extract()[0]
        items.append(item)

        return items
