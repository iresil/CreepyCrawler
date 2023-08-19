import definitions
import requests
from protego import Protego


class RobotParser:
    """ Parses the robots.txt file """

    def __init__(self):
        """ Parses the robots.txt file only once, to retrieve the allowed crawl delay. """

        robotstxt = requests.get(definitions.ROBOTS_TXT)
        rp = Protego.parse(robotstxt.text)
        self.delay = float(rp.crawl_delay("*"))
