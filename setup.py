from setuptools import setup, find_packages

setup(
    name='creepyCrawler',
    version='1.0',
    author='Irene Spanou',
    description='Downloads stories from Creepypasta',
    long_description='Downloads Creepypasta stories making one request per minute as requested in robots.txt,'
                     'sorted by rating descending',
    url='https://github.com/iresil',
    keywords='creepypasta, crawler, scraper',
    python_requires='>=3.10, <4',
    packages=find_packages(),
    install_requires=[
        'scrapy~=2.8.0',
        'mysql~=0.0.3',
        'mysql-connector-python~=8.0.32',
        'protego~=0.2.1',
        'requests~=2.28.2'
    ],
    package_data={
    },
    entry_points={
        'runners': [
            'creepyCrawler=creepyCrawler:main',
        ]
    }
)
