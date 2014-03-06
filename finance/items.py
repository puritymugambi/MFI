# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.contrib.djangoitem import DjangoItem
from ui.models import Loan, Forex, Stock


class LoanItem(DjangoItem):
    django_model = Loan


class ForexItem(DjangoItem):
    django_model = Forex


class StockItem(DjangoItem):
    django_model = Stock
