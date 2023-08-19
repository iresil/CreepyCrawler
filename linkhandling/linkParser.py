import json
import definitions
from database.storyReader import StoryReader


class LinkParser:
    """ Parses the JSON list that contains the story links. """

    @staticmethod
    def parse():
        """ Parses the JSON list that contains the story links and returns a list of URLs. """

        urls = None
        with open(definitions.JSON_LIST, 'r') as json_file:
            json_list = list(json_file)
        for json_str in json_list:
            result = json.loads(json_str)
            if result['link'] is not None:
                if StoryReader.get_object(result['link']) is not None:
                    print("Story %s already in database. Skipping...", result['link'], "\n")
                elif urls is None:
                    urls = [{"link": result['link'], "rating": result['rating']}]
                else:
                    urls.append({"link": result['link'], "rating": result['rating']})
        return urls
