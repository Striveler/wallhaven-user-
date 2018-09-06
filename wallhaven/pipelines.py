# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings
import os

class ImagesPipeline(ImagesPipeline):
    get_project_settings().get('IMAGES_STORE')

    def get_media_requests(self, item, info):
        image_url = item["urls"]
        yield scrapy.Request(image_url)

    def item_completed(self, result, item, info):
        image_path = [x["path"] for ok, x in result if ok]

        # os.rename(self.IMAGES_STORE + "/" + image_path[0], self.IMAGES_STORE + "/" + item["name"][-6] + ".jpg")

        # item["imagePath"] = self.IMAGES_STORE + "/" + item["name"][-6]

        return item