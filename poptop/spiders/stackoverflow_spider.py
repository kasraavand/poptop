import sys
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from datetime import datetime


class MySpider(CrawlSpider):
    name = 'tw'
    def __init__(self, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        self.date = kwargs.get('date')
        if not self.date:
            raise ValueError('No date given')

        dt = datetime.strptime(self.date, "%d-%m-%Y") 
    
        self.allowed_domains = ['stackoverflow.com']
        self.start_urls = ['http://stackoverflow.com/search?tab=votes&q=%5bpython%5d%20is%3aq%20created%3a{dt.year}-{dt.month}-{dt.day}'.format(dt=dt)]
    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="result-link"]/span/a/@href') 
        for question in questions:

            with open('url{}.txt'.format(self.date),'a+') as f:
                f.write(question.extract()+'\n')

