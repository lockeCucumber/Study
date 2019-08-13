# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from pymongo import MongoClient
base_path = os.path.dirname(os.path.realpath(__file__))


def get_mongo_client():
    mongo_host = "lockecucumber.com"
    mongo_client = MongoClient(mongo_host, 27017)
    mongo_client.admin.authenticate('locke', 'Locke0658')
    return mongo_client

mongo_client = get_mongo_client()
test_col = mongo_client["test_db"]["test_col"]

class LouspiderPipeline(object):
    def process_item(self, item, spider):
        if spider.name == 'lab':
            author = item['author'] if item['author'] else '佚名'
            text = item['text']
            tags = item['tags']
            doc = {
                "author": author,
                "text": text,
                "tags": tags
            }
            test_col.insert(doc)
        else:
            with open('courses.txt', 'a') as file:
                line = u"course_name: {0}, learned_count: {1}, image: {2}\n".format(
                    item['name'], item['learned'], item['image'])
                file.write(line)
        return item
