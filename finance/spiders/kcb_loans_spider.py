from scrapy.selector import Selector
from finance.spiders import Nini

from ..items import LoanItem


class KcbBankLoanSpider(Nini):
    name = "kcbbankloan"
    allowed_domains = ["ke.kcbbankgroup.com/"]
    start_urls = [
        "http://ke.kcbbankgroup.com/personal-banking/borrowing/personal-loans/",
    ]

    institution_name = 'Kcb'

    def parse(self, response):
        sel = Selector(response)
        base = sel.xpath('//*[@id="main"]/div[1]/div[3]/div[1]/div[2]/table')
        #title_tr, loan_tr, loan_tr, loan_tr, loan_tr, loan_tr = base.xpath("tr")

        items = []


        item = LoanItem()
        for loan_item in base.xpath('tr[2]/td[2]/ul/li/text()').extract():
            item = LoanItem()
            item['benefits'] = loan_item
            items.append(item)
        for req in base.xpath('tr[2]/td[3]/ul/li/text()').extract():
            item = LoanItem()
            item['requirements'] = req
            items.append(item)

        item['loan_name'] = base.xpath('tr[2]/td[1]/h3/a/text()').extract()
        item['desc'] = base.xpath('tr[2]/td[1]/p/text()').extract()
        items.append(item)

        #items.append(item)



        item = LoanItem()
        item['loan_name'] = base.xpath('tr[3]/td[1]/h3/a/text()').extract()
        item['desc'] = base.xpath('tr[3]/td[1]/p/text()').extract()
        items.append(item)
        for ben in base.xpath('tr[3]/td[2]/ul/li/text()').extract():
            item = LoanItem()
            item['benefits'] = ben
            items.append(item)
        for req in base.xpath('tr[3]/td[3]/ul/li/text()').extract():
            item = LoanItem()
            item['requirements'] = req
            items.append(item)




        item = LoanItem()
        item['loan_name'] = base.xpath('tr[4]/td[1]/h3/a/text()').extract()
        item['desc'] = base.xpath('tr[4]/td[1]/p/text()').extract()
        items.append(item)
        for ben in base.xpath('tr[4]/td[2]/ul/li/text()').extract():
            item = LoanItem()
            item['benefits'] = ben
            items.append(item)
        for req in base.xpath('tr[4]/td[3]/ul/li/text()').extract():
            item = LoanItem()
            item['requirements'] = req
            items.append(item)




        item = LoanItem()
        item['loan_name'] = base.xpath('tr[5]/td[1]/h3/a/text()').extract()
        item['desc'] = base.xpath('tr[5]/td[1]/p/text()').extract()
        items.append(item)
        for ben in base.xpath('tr[5]/td[2]/ul/li/text()').extract():
            item = LoanItem()
            item['benefits'] = ben
            items.append(item)
        for req in base.xpath('tr[5]/td[3]/ul/li/text()').extract():
            item = LoanItem()
            item['requirements'] = req
            items.append(item)



        item = LoanItem()
        item['loan_name'] = base.xpath('tr[6]/td[1]/h3/a/text()').extract()
        item['desc'] = base.xpath('tr[6]/td[1]/p/text()').extract()
        items.append(item)
        for ben in base.xpath('tr[6]/td[2]/ul/li/text()').extract():
            item = LoanItem()
            item['benefits'] = ben
            items.append(item)
        for req in base.xpath('tr[6]/td[3]/ul/li/text()').extract():
            item = LoanItem()
            item['requirements'] = req
            items.append(item)



        return items