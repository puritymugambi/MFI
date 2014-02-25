from django.db import models

# Create your models here.
class InstitutionType(models.Model):
    type_name = models.CharField(max_length=100)


class Institution(models.Model):
    name = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    webpage = models.CharField(max_length=200)
    typ = models.ForeignKey(InstitutionType)


class Loan(models.Model):
    inst = models.ForeignKey(Institution)
    loan_name = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    link = models.URLField()
    eligibility = models.CharField(max_length=300)


class Currency(models.Model):
    name = models.CharField(max_length=100)
    abbr = models.CharField(max_length=3)


class Forex(models.Model):
    inst = models.ForeignKey(Institution)
    currency = models.ForeignKey(Currency)
    buying_price = models.FloatField()
    selling_price = models.FloatField()


class Stock(models.Model):
    name = models.CharField(max_length=100)
    institution = models.ForeignKey(Institution)
    current_price = models.FloatField()
    previous_price = models.FloatField()

    @property
    def price_change(self):
        return (self.previous_price - self.current_price)

    @property
    def perc_change(self):
        return (self.price_change * 100) / self.previous_price

