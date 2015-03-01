from pdfcreator import runconvert
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
#from testspiders.spiders.followall import FollowAllSpider
from scrapy.utils.project import get_project_settings
from poptop.spiders.stackoverflow_spider import MySpider
import sys
import os

settings = get_project_settings()
crawler = Crawler(settings)	
crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
crawler.configure()
d=raw_input('Enter the date with this format (d-m-Y) : ')
q_number=raw_input('What number of question you want to get? : ')
spider=MySpider(date=d)
crawler.crawl(spider)
crawler.start()
log.start()
reactor.run() # the script will block here until the spider_closed signal was sent

try:
    os.makedirs(sys.path[0]+'/questions')
except OSError:
    pass

for url in open('url{}.txt'.format(d),'r') :
	runconvert('http://stackoverflow.com'+url.strip())
sys.exit()