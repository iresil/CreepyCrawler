import definitions
import mysql.connector


class MysqlPipeline:
    """ Pipeline used by Scrapy, that handles data storage. """

    def __init__(self):
        """ Initializes the connection, defines a cursor and creates the table if it doesn't exist. """

        self.conn = mysql.connector.connect(
            host=definitions.MYSQL_HOST,
            user=definitions.MYSQL_USER,
            password=definitions.MYSQL_PASSWORD,
            database=definitions.MYSQL_DB
        )

        self.cur = self.conn.cursor()

        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS stories (
                id INT NOT NULL auto_increment, 
                link NVARCHAR(2000),
                title NVARCHAR(500),
                rating REAL,
                reading_time REAL,
                categories NVARCHAR(2000),
                content LONGTEXT,
                PRIMARY KEY (id)
            )
        """)

    def process_item(self, item, spider):
        """ Upserts the story in the DB. """

        # Check to see if story is already in database
        self.cur.execute("SELECT * FROM stories WHERE title = %s AND reading_time = %s AND rating = %s",
                         (item['title'], item['reading_time'], item['rating']))
        result = self.cur.fetchone()

        # If it exists, log and continue, if it doesn't, insert it
        if result:
            spider.logger.warn("Item already in database: %s" % item['title'])
        else:
            self.cur.execute(""" INSERT INTO stories (link, title, rating, reading_time, categories, content) 
                                 VALUES (%s,%s,%s,%s,%s,%s)""", (
                item["link"],
                item["title"],
                item["rating"],
                item["reading_time"],
                item["categories"],
                item["text"]
            ))

        self.conn.commit()

    def close_spider(self):
        """ Gracefully closes the cursor and the connection. """

        self.cur.close()
        self.conn.close()
