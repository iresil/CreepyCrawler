import scrapy
import json
from database.storyItem import StoryItem
from linkhandling.linkParser import LinkParser
from creepyCrawlerRobots import RobotParser


urls = LinkParser.parse()
robotParser = RobotParser()
i = 0


class StoriesSpider(scrapy.Spider):
    """ Retrieves stories (and their details) from the saved links. """

    name = 'creepyCrawlerStories'
    start_urls = [
        urls[0]["link"]
    ]
    custom_settings = {
        'ITEM_PIPELINES': {
            'database.mysqlPipeline.MysqlPipeline': 300
        },
        'DOWNLOAD_DELAY': robotParser.delay
    }

    def parse(self, response, **kwargs):
        """ Parses HTML elements to retrieve the necessary details, recursively. Yields results as it goes. """

        global i

        story_item = StoryItem()
        for item in response.css('article.post'):
            text_list = [
                ' '.join(
                    line.strip()
                    for line in p.xpath('.//text()').extract()
                    if line.strip()
                )
                for p in response.xpath("//article[contains(@class, 'post')]//p")
            ]

            reading_time = item.css('span.rt-time::text').get()
            if reading_time == " < 1":
                reading_time = 0.5

            story_item["link"] = urls[i]["link"]
            story_item["title"] = item.css('h1.entry-title::text').get()
            story_item["rating"] = urls[i]["rating"]
            story_item["reading_time"] = reading_time
            story_item["categories"] = json.dumps(item.css('span.ast-terms-link a::text').extract())
            story_item["text"] = json.dumps(text_list)

            yield story_item

        i = (i + 1)

        if len(urls) > i:
            next_page = urls[i]["link"]
            if next_page is not None:
                # yield response.follow(next_page, self.parse)
                yield response.follow(next_page, meta={
                    'dont_redirect': True,
                    'handle_httpstatus_list': [301, 302]
                }, callback=self.parse)
