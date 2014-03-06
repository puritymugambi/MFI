# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

from scrapy.spider import BaseSpider
from ui.models import Institution


class Nini(BaseSpider):
    #this is bad!!!
    institution = None
    institution_name = None

    @property
    def get_institution(self):
        if self.institution_name:
            institution = Institution.objects.get(name=self.institution_name)
            self.institution = institution
            return institution
        return None

