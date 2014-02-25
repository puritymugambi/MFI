# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.contrib.djangoitem import DjangoItem
from ui.models import Loan, Forex, Stock


class BankofAfricaLoanItem(DjangoItem):
    #benefits
    #requirements
    #features
    django_model = Loan


class FidelityBankLoanItem(DjangoItem):
    # define the fields for your item here like:
    #name
    #features
    django_model = Loan


class NicBankLoanItem(DjangoItem):
    # define the fields for your item here like:
    # name
    #loans
    #requirements
    #forms
    django_model = Loan


class StanChartBankLoanItem(DjangoItem):
    # define the fields for your item here like:
    # name
    #loans
    #features
    #eligibility
    django_model = Loan


class BasicBankItem(DjangoItem):
    #loans
    django_model = Loan


class BarclaysBankLoanItem(BasicBankItem):
    pass


class CfcstanbicBankLoanItem(BasicBankItem):
    pass


class ChaseBankLoanItem(BasicBankItem):
    pass


class EcobankLoanItem(BasicBankItem):
    pass


class EquityBankLoanItem(BasicBankItem):
    pass


class KcbBankLoanItem(BasicBankItem):
    pass


class BureauForexProjectItem(DjangoItem):
    # define the fields for your item here like:
    # name = Field()
    django_model = Forex


class EquityForexItem(DjangoItem):
    django_model = Forex


class NationalForexItem(DjangoItem):
    django_model = Forex


class NseItem(DjangoItem):
    django_model = Stock


class NellyCapitalItem(DjangoItem):
    django_model = Stock

