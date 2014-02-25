# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

from scrapy.spider import BaseSpider
from ui.models import Institution


class Nini(BaseSpider):
    #this is bad!!!
    institution_id = None
    institution_name = None

    @property
    def get_institution_id(self):
        if self.institution_name:
            institution = Institution.objects.get(name=self.institution_name)
            institution_id = institution.id
            return institution_id
        return None
