from django.db import models
from django.db.models.signals import pre_save

import re

class BabaYao(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


# Create your models here.
class InstitutionType(BabaYao):
    type_name = models.CharField(max_length=100)

    def __unicode__(self):
        return repr(self.pk) + ". "+ self.type_name


class Institution(BabaYao):
    name = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    webpage = models.CharField(max_length=200)
    typ = models.ForeignKey(InstitutionType)

    def __unicode__(self):
        return repr(self.pk) + ". "+ self.name


class Loan(BabaYao):
    inst = models.ForeignKey(Institution)
    loan_name = models.CharField(max_length=1000)
    desc = models.CharField(max_length=1000)
    link = models.URLField()
    requirements = models.CharField(max_length=1000)
    eligibility = models.CharField(max_length=1000)
    features = models.CharField(max_length = 1000)
    forms = models.CharField(max_length=1000)
    benefits = models.CharField(max_length = 1000)


    def __unicode__(self):
        return repr(self.pk) + ". "+ self.loan_name


class Currency(models.Model):
    name = models.CharField(max_length=100)
    abbr = models.CharField(max_length=20)
    versions = models.TextField()

    def match(self, string):
        regex = "|".join(self.versions.split(","))
        regex_parser = re.compile(regex)

        results = regex_parser.match(string)

        if results:
            return True

        return False

    def __unicode__(self):
        return self.name


class Forex(BabaYao):
    inst = models.ForeignKey(Institution)
    currency_name = models.CharField(max_length = 100)
    buying_price = models.CharField(max_length = 50)
    selling_price = models.CharField(max_length = 50)
    def __unicode__(self):
        return self.currency_name


class Stock(BabaYao):
    name = models.CharField(max_length=100)
    inst = models.ForeignKey(Institution)
    current_price = models.FloatField()
    previous_price = models.FloatField()

    def __unicode__(self):
        return self.name

    @property
    def price_change(self):
        return self.previous_price - self.current_price

    @property
    def perc_change(self):
        return (self.price_change * 100) / self.previous_price

def set_currency(val):
    all_currencies = Currency.objects.all()
    for currency in all_currencies:
        if currency.match(val):
            return currency.name

    raise Exception("Purity: %s, this currency does not exist" % val)

def before_saving_forex(sender, **kwargs):
    kwargs['instance'].currency_name = set_currency(kwargs['instance'].currency_name)

pre_save.connect(before_saving_forex, sender=Forex)