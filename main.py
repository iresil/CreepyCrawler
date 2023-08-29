import logging
from scrapy import cmdline
import definitions


logging.basicConfig(filename='log.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

if definitions.DOWNLOAD_LINKS:
    cmdline.execute("scrapy runspider crawler/creepyCrawlerLinks.py -o resources/links.jsonl".split())
if definitions.DOWNLOAD_STORIES:
    cmdline.execute("scrapy runspider crawler/creepyCrawlerStories.py".split())
