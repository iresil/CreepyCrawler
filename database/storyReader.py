import definitions
import mysql.connector
from database.storyItem import StoryItem


class StoryReader:
    """ Retrieves stories from the DB. """

    @staticmethod
    def get_object(link):
        """
        Attempts to retrieve a story from the DB.
        If the story was found, the result is printed to the default output stream.
        """

        story_item = None
        try:
            connection = mysql.connector.connect(host=definitions.MYSQL_HOST, database=definitions.MYSQL_DB,
                                                 user=definitions.MYSQL_USER, password=definitions.MYSQL_PASSWORD)

            sql = "SELECT * FROM stories WHERE link = %s"
            cursor = connection.cursor()
            cursor.execute(sql, (link,))

            # get all records
            records = cursor.fetchall()
            if cursor.rowcount > 0:
                print("Total number of rows in table: ", cursor.rowcount)

            for row in records:
                story_item = StoryItem()
                print("Id = ", row[0])
                story_item["link"] = row[1]
                print("Link = ", row[1])
                story_item["title"] = row[2]
                print("Title = ", row[2])
                story_item["rating"] = row[3]
                print("Rating = ", row[3])
                story_item["reading_time"] = row[4]
                print("Reading Time = ", row[4])
                story_item["categories"] = row[5]
                print("Categories = ", row[5])
                story_item["text"] = row[6]
                print("Content = ", row[6], "\n")
        except mysql.connector.Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if connection.is_connected():
                connection.close()
                cursor.close()
                return story_item
