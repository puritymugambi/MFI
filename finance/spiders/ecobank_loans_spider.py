from scrapy.selector import Selector
from finance.spiders import Nini

from ..items import EcobankLoanItem as ELI


class EcobankLoanSpider(Nini):
    name = "ecobankloan"
    allowed_domains = ["ecobank.com"]
    start_urls = [
        "http://www.ecobank.com/loans.aspx",
    ]


    #    def parse(self, response):
    #        sel = Selector(response)
    #        base = sel.xpath('//*[@id="MainArea"]/table/tbody/tr/td[3]/table[2]/tbody/tr[1]')
    #        loan_td = base.xpath("td")
    #        item = ELI()
    #        item['loans']= [{"name":i.xpath('div[1]/text()').extract(),"desc": i.xpath('div[2]/text()').extract()} for i in loan_td]

    #        return item

    def parse(self, response):
        sel = Selector(response)
        defs, defs1 = sel.xpath('//div[@class="def"]/text()'), sel.xpath('//div[@class="def1"]/text()')
        item = ELI()
        loans = []
        loans.append({'name': defs[0].extract(), 'desc': defs1[1].extract()})
        loans.append({
            'name': defs[1].extract(), 'desc': "".join([i.extract() for i in defs1[2:-1]])})
        loans.append({'name': defs[-1].extract(), 'desc': defs1[-1].extract()})
        item['loans'] = loans
        return item


