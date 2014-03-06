__author__ = 'purity'

from django.core.management import BaseCommand

from ...models import Institution, InstitutionType, Currency # dont like DIS!

class Command(BaseCommand):
    help = "input initial data to system\nUsage: python manage.py initial all"

    def run_from_argv(self, argv):
        self.argv = argv
        self.execute()

    def handle(self, *args, **options):
        if len(self.argv) < 3:
            self.stdout.write(self.help)
            return

        model = self.argv[2]

        if model == "all":
            institution_types = ['bank', 'forex', 'stock']

            for institution_type in institution_types:
                InstitutionType.objects.create(type_name=institution_type)


            currencies = [
                {
                    "name": "US Dollar",
                    "abbr": "USD",
                    "versions": "USD,USD Dollar,USDollar,US Dollar"
                },

                {
                    "name": "Great British Pound",
                    "abbr": "GBP",
                    "versions": "GBP,British Pound, Sterling Pound"
                },

                {
                    "name": "Euro",
                    "abbr": "EUR",
                    "versions": "EUR, Euro"
                },

                {
                    "name": "South African Rand",
                    "abbr": "ZAR",
                    "versions": "ZAR, South Africa Rand, SA Rand"
                },

                {
                    "name": "Japanese Yen",
                    "abbr": "JPY",
                    "versions": "JPY, Japan Yen"
                },

                {
                    "name": "Swiss Francs",
                    "abbr": "CHF",
                    "versions": "CHF, Swiss Franc"
                },

                {
                    "name": "Canadian Dollar",
                    "abbr": "CAD",
                    "versions": "CAD, Canada Dollar"
                },

                {
                    "name": "Australian Dollar",
                    "abbr": "AUD",
                    "versions": "AUD, Australia Dollar"
                },

                {
                    "name": "Ugandan Shilling",
                    "abbr": "UGX",
                    "versions": "UGX, Uganda Shilling"
                },

                {
                    "name": "Sudanese Pound",
                    "abbr": "SDG",
                    "versions": "SDG, Sudan Pound"
                },

                {
                    "name": "Swedish Krona",
                    "abbr": "SEK",
                    "versions": "Swedish Kroner, Swedish Krone, SEK"
                },

                {
                    "name": "Norwegian Krona",
                    "abbr": "NOK",
                    "versions": "Norwegian Kroner, Norwegian Krone, NOK"
                },

                {
                    "name": "Danish Krona",
                    "abbr": "DKK",
                    "versions": "Danish Kroner, Danish Krone, DKK"
                },

                {
                    "name": "Rwandese Francs",
                    "abbr": "RWF",
                    "versions": "RWF, Rwadese Francs, Rwadese Franc, Rwandese Franc"
                },

                {
                    "name": "Tanzania Shilling",
                    "abbr": "TZS",
                    "versions": "TZS, Tanzanian Shilling, Tanzania Shillings, Tanzanian Shillings"
                },

                {
                    "name": "Chinese Yuan",
                    "abbr": "CNY",
                    "versions": "CNY, China Yuan, Chinese Yuans, China Yuan"
                },

                {
                    "name": "United Arab Emirates Dirham",
                    "abbr": "AED",
                    "versions": "AED, UAE Dirham"
                }

            ]

            for currency in currencies:
                Currency.objects.create(
                    name=currency['name'],
                    abbr=currency['abbr'],
                    versions=currency['versions']
                )

            Institution.objects.create(
                name="Barclays",
                domain="barclays.co.ke",
                webpage="http://www.barclays.co.ke/personal/loan/index.html",
                typ_id=1
            )

            Institution.objects.create(
                name="Boa",
                domain="boakenya.com",
                webpage="http://www.boakenya.com/personal-banking/loans-credit-facilities/",
                typ_id=1
            )

            Institution.objects.create(
                name="Cfc",
                domain="cfcstanbicbank.co.ke",
                webpage="http://www.cfcstanbicbank.co.ke/Kenya/Personal/Borrowing",
                typ_id=1
            )

            Institution.objects.create(
                name="Chase",
                domain="chasebankkenya.co.ke",
                webpage="http://www.chasebankkenya.co.ke/products/loans-1",
                typ_id=1
            )

            Institution.objects.create(
                name="Consolidated",
                domain="http://www.consolidated-bank.com/",
                webpage="http://www.consolidated-bank.com/index.php?option=com_content&view=article&id=43&Itemid=79",
                typ_id=1
            )

            Institution.objects.create(
                name="Eco",
                domain="ecobank.com",
                webpage="http://www.ecobank.com/loans.aspx",
                typ_id=1
            )

            Institution.objects.create(
                name="Equity",
                domain="equitybank.co.ke",
                webpage="http://www.equitybank.co.ke/index.php/loans/consumer-loans",
                typ_id=1
            )

            Institution.objects.create(
                name="Kcb",
                domain="ke.kcbbankgroup.com/",
                webpage="http://ke.kcbbankgroup.com/personal-banking/borrowing/personal-loans/",
                typ_id=1
            )

            Institution.objects.create(
                name="Nic",
                domain="http://www.nic-bank.com/main/",
                webpage="http://www.nic-bank.com/main/borrow/personal/",
                typ_id=1
            )

            Institution.objects.create(
                name="Stanchart",
                domain="sc.com/ke",
                webpage="https://www.sc.com/ke/borrow/loans-personal.html",
                typ_id=1
            )

            Institution.objects.create(
                name="BoaBureau",
                domain="www.boakenya.com/",
                webpage="http://www.boakenya.com/exchange-rates/",
                typ_id=2
            )

            Institution.objects.create(
                name="BobarodaBureau",
                domain="http://bankofbarodakenya.com/",
                webpage="http://bankofbarodakenya.com/",
                typ_id=2
            )

            Institution.objects.create(
                name="DevtBureau",
                domain="http://www.devbank.com/",
                webpage="http://www.devbank.com/",
                typ_id=2
            )

            Institution.objects.create(
                name="DtbBureau",
                domain="www.dtbk.dtbafrica.com",
                webpage="http://www.dtbk.dtbafrica.com/forex.aspx",
                typ_id=2
            )

            Institution.objects.create(
                name="EquityBureau",
                domain="equitybank.co.ke",
                webpage="http://www.equitybank.co.ke/",
                typ_id=2
            )

            Institution.objects.create(
                name="FinaBureau",
                domain="http://gtbank.co.ke/",
                webpage="http://gtbank.co.ke/",
                typ_id=2
            )

            Institution.objects.create(
                name="IMBureau",
                domain="www.imbank.com",
                webpage="https://www.imbank.com/personal/foreign-exchange/",
                typ_id=2
            )

            Institution.objects.create(
                name="NationalBureau",
                domain="nationalbank.co.ke",
                webpage="http://www.nationalbank.co.ke/index.php/2013-05-24-10-08-17/exchange-rates",
                typ_id=2
            )

            Institution.objects.create(
                name="SkyBureau",
                domain="skyforexbureau.com",
                webpage="https://www.skyforexbureau.com",
                typ_id=2
            ),


            Institution.objects.create(
                name="NellyCapital",
                domain="nellydata.com/CapitalFM/livedata.aspm",
                webpage="http://www.nellydata.com/CapitalFM/livedata.asp",
                typ_id=2
            )

            self.stdout.write("Added data")

            return

        self.stdout.write("Sorry that model does not exist")
