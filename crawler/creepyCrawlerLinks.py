import scrapy
import definitions
from creepyCrawlerRobots import RobotParser


url = definitions.STORIES_SORTED_BY_RATING
robotParser = RobotParser()
i = 213


class LinkSpider(scrapy.Spider):
    """ Discovers story links from the CreepyPasta archive. """

    name = 'creepyCrawlerLinks'
    start_urls = [
        url + '&_page=' + str(i)
    ]
    custom_settings = {
        'DOWNLOAD_DELAY': robotParser.delay
    }

    def parse(self, response, **kwargs):
        """ Parses links to find stories and moves to the next page, recursively. Yields results as it goes. """

        global i
        i = (i + 1)

        for link in response.css('div.pt-cv-ifield'):
            link_href = link.css('a::attr(href)').extract_first()
            link_rating = link.css('div.pt-cv-ctf-value::text').get()
            if link_href is not None:
                yield {
                    'link': link_href,
                    'rating': link_rating
                }

        next_page = url + '&_page=' + str(i)
        # if next_page is not None:
        if i <= definitions.LINK_RETRIEVAL_PAGE_COUNT:
            yield response.follow(next_page, self.parse)
