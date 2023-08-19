import logging
from scrapy import cmdline

logging.basicConfig(filename='log.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

# cmdline.execute("scrapy runspider crawler/creepyCrawlerLinks.py -o resources/links.jsonl".split())
cmdline.execute("scrapy runspider crawler/creepyCrawlerStories.py".split())
