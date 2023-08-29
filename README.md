# Creepy Crawler
### A Python crawler specializing in CreepyPasta stories
___
> [!NOTE]
> This project was built for educational purposes only.
> Crawl rate is automatically set based on what robots.txt allows.

Simple crawler created in **Python 3.10**. Visits the [CreepyPasta](https://www.creepypasta.com) website and does two things, as separate processes:
- Downloads all the story links it finds and stores each one alongside its rating in `resources/links.jsonl`.
- Reads the contents of `resources/links.jsonl`, follows each link and stores its contents in a MySQL DB entry, alongside its rating, reading time and categories.

## Plugin dependencies
- [**scrapy 2.8.0**](https://pypi.org/project/Scrapy/)
- [**mysql 0.0.3**](https://pypi.org/project/mysql/)
- [**mysql-connector-python 8.0.32**](https://pypi.org/project/mysql-connector-python/)
- [**protego 0.2.1**](https://pypi.org/project/Protego/)
- [**requests 2.28.2**](https://pypi.org/project/requests/)
- a locally installed [**MySQL**](https://dev.mysql.com/downloads/installer/) server instance, with a database called `creepystore`

## Finding story links to download
The main entry point for this part of the process is `crawler/creepyCrawlerLinks.py`, which contains the `LinkSpider` class. It uses **scrapy** to retrieve all story links.

It is called from `main.py`, using:
```
cmdline.execute("scrapy runspider crawler/creepyCrawlerLinks.py -o resources/links.jsonl".split())
```

After executing this code for the first time, you can set `DOWNLOAD_LINKS = False` in `definitions.py`, so that you can work with offline data only.

If you want to download the links multiple times, you will need to delete the `resources/links.jsonl` file before each new execution.

## Downloading the stories
The main entry point for this part of the process is `crawler/creepyCrawlerStories.py`, which contains the `StoriesSpider` class. This also uses **scrapy**, this time to download the actual stories. For storing them to the DB, it uses **MySQL Connector (Python)**.

It is called from `main.py`, using:
```
cmdline.execute("scrapy runspider crawler/creepyCrawlerStories.py".split())
```

You can set `DOWNLOAD_STORIES = False` in `definitions.py`, if you only want to download the story links with their ratings.

## Storing data
After the code runs, the stories will be stored in your local MySQL server instance.

You will need to create your `creepystore` database manually. The table on which stories will eventually be stored, will be created by the code in `database/mysqlPipeline.py`, if it does not exist.
