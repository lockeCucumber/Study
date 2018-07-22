# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
base_path = os.path.dirname(os.path.realpath(__file__))

class LouspiderPipeline(object):
    def process_item(self, item, spider):
        if spider.name == 'lab':
            author = item['author']
            if not author:
                author = 'locke' 
            text = item['text']
            tags = item['tags']
            file_name = base_path + '/output/' + author + '.txt'
            with open(file_name, 'a') as f:
                f.write(tags + '\n' + text +'\n')
        else:
            with open('courses.txt', 'a') as file:
                line = u"course_name: {0}, learned_count: {1}, image: {2}\n".format(
                    item['name'], item['learned'], item['image'])
                file.write(line)
        return item
