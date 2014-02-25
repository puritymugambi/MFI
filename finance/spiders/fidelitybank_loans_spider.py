from scrapy.selector import Selector
from finance.spiders import Nini

from ..items import FidelityBankLoanItem as FBLI


class FidelityBankLoanSpider(Nini):
    name = "fdbankloan"
    allowed_domains = ["fidelitybank.co.ke"]
    start_urls = [
        "http://www.fidelitybank.co.ke/personal_loan.html",
    ]


    def parse(self, response):
        sel = Selector(response)
        base = sel.xpath(
            '//*[@id="3column"]/tbody/tr/td[2]/table/tbody/tr[6]/td/table/tbody/tr[1]/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody')

        #//*[@id="3column"]/tbody/tr/td[2]/table/tbody/tr[6]/td/table/tbody/tr[1]/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody
        #//*[@id="3column"]/tbody/tr/td[2]/table/tbody/tr[6]/td/table/tbody/tr[1]/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody

        #//*[@id="3column"]/tbody/tr/td[2]/table/tbody/tr[6]/td/table/tbody/tr[1]/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td[1]


        item = FBLI()
        item['name'] = base.xpath('tr[1]/td/table/tbody/tr/td[1]/text()').extract()
        item['features'] = base.xpath('tr[4]/td/table/tbody/tr[1]/td[2]/text()').extract()

        #//*[@id="3column"]/tbody/tr/td[2]/table/tbody/tr[6]/td/table/tbody/tr[1]/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr[1]/td[2]


        return item


