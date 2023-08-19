from scrapy.item import Item, Field


class StoryItem(Item):
    """ The set of information that will be stored for each story. """

    link = Field()
    title = Field()
    rating = Field()
    reading_time = Field()
    categories = Field()
    text = Field()
