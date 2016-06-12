from pdfcreator import runconvert
from scrapy.crawler import CrawlerProcess
from poptop.spiders.stackoverflow_spider import MySpider
import sys
import os

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

# crawler.configure()
d = raw_input('Enter the date with this format (d-m-Y) : ')
q_number = raw_input('What number of question you want to get? : ')
process.crawl(MySpider, date=d)
process.start()  # the script will block here until the spider_closed signal was sent

try:
    os.makedirs(sys.path[0] + '/questions')
except OSError:
    pass

for url in open('url{}.txt'.format(d), 'r'):
    runconvert('http://stackoverflow.com' + url.strip())
sys.exit()