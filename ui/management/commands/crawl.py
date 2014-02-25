
"""
The MIT License

Copyright (c) 2014, mbacho (Chomba Ng'ang'a)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.


file : crawl.py
project : proj

"""
from os import chdir

from django.core.management import BaseCommand
from scrapy.cmdline import execute

from ui.management.commands import get_scrapyroot


class Command(BaseCommand):
    help = 'Run scrapy crawlers within django\nUsage : python manage.py crawl [<spidername>]'

    def run_from_argv(self, argv):
        self._argv = argv
        self.execute()

    def handle(self, *args, **options):
        scrapydir = get_scrapyroot()
        chdir(scrapydir)
        default_args = ['scrapy', 'crawl']

        if len(self._argv) == 3:
            default_args.append(self._argv[2])
        else:
            self.stdout.write(self.help)
            return
        try:
            execute(default_args)
        except KeyError, ke:
            self.stdout.write('iyo spider haionekani')
