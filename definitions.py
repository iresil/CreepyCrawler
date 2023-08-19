import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_LIST = os.path.join(ROOT_DIR, 'resources', 'links.jsonl')

ROBOTS_TXT = 'https://creepypasta.com/robots.txt'
STORIES_SORTED_BY_RATING = 'https://www.creepypasta.com/archive/top-ranked/?_orderby=_gdrts_stars-rating_rating%2Cdesc'

LINK_RETRIEVAL_PAGE_COUNT = 216

MYSQL_HOST = 'localhost'
MYSQL_USER = 'python'
MYSQL_PASSWORD = 'python'
MYSQL_DB = 'creepystore'
