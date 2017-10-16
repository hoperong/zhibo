#!/usr/bin/env python
# conding=utf-8

from urllib import request
from bs4 import BeautifulSoup
import ssl
import re
from model import spider, model
from controller import log
from datetime import datetime


class quanmin(spider.spider):

    root = 'https://www.quanmin.tv'
    url = '{0}/game/all'.format(root)
    name = '全民直播'

    def getLastPageIndex(self):
        response = request.urlopen(self.url)
        page = response.read().decode('utf-8')
        html = BeautifulSoup(page, 'html.parser')
        result = html.find_all(class_=re.compile('list_w-paging_num'))
        try:
            re_result = result[-1].get_text() if len(result) > 0 else 1
            return int(re_result)
        except Exception:
            return 1

    def run(self):
        log.spiderLog('开始爬取...', self.className)
        platform = model.Platform()
        platform.name = self.name
        platform.code = self.className
        data = {'platform': platform, 'list': []}
        ssl._create_default_https_context = ssl._create_unverified_context
        endPage = self.getLastPageIndex()
        log.spiderLog('总共{0}页...'.format(endPage), self.className)
        for i in range(endPage):
            log.spiderLog('{0}/{1}页...'.format(i + 1, endPage), self.className)
            response = request.urlopen('{0}?p={1}'.format(self.url, i + 1))
            page = response.read().decode('utf-8')
            html = BeautifulSoup(page, 'html.parser')
            items = html.select('.list_w-videos_video-list')[1].select('li')
            infoTime = datetime.now()
            for item in items:
                catalogName = item.select('div > div > a > a')[0].get_text()
                code = item.select('div > div > a')[0]['href'][17:]
                name = item.select('div > div > a > div > div > div > span')[
                    0].get_text()
                roomUrl = '{0}/{1}'.format(self.root, code)
                title = item.select('div > div > a > div > div > p')[
                    0].get_text()
                imageUrl = item.select('div > div > a > div > img')[0]['src']
                number = int(item.select(
                    'div > div > a > div > div > div > span')[1].get_text())
                # catalog
                catalog = model.Catalog()
                catalog.name = catalogName
                # room
                room = model.Room()
                room.code = code
                room.name = name
                room.roomUrl = roomUrl
                room.title = title
                room.imageUrl = imageUrl
                # info
                info = model.Info()
                info.roomId = room.roomId
                info.catalogId = catalog.catalogId
                info.number = number
                info.time = infoTime
                data['list'].append({
                    'catalog': catalog,
                    'room': room,
                    'info': info
                })
        log.spiderLog('爬取结束...', self.className)
        return data
