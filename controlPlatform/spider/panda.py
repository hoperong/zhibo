#!/usr/bin/env python
# coding=utf-8

from urllib import request
import ssl
import json
from model import spider, model
from controller import log
from datetime import datetime

'''
status:0-所有   2-正在
order:person_num
pageno:页数，1开始
pagenum:每页项目数
'''


class panda(spider.spider):

    root = 'https://www.panda.tv'
    url = '{0}/live_lists?status=2&order=person_num'.format(root)
    pageNum = 120
    name = '熊猫直播'

    def getLastPageIndex(self):
        response = request.urlopen(
            r'{0}&pageno=1&pagenum=1'.format(self.url))
        html = response.read().decode('utf-8')
        pandaTv = json.loads(html)
        try:
            total = int(pandaTv['data']['total'])
            endPage = int(total / self.pageNum)
            if endPage * self.pageNum < total:
                endPage += 1
            return endPage
        except Exception:
            return 0

    def run(self):
        log.spiderLog('开始爬取...', self.className)
        platform = model.Platform()
        platform.name = self.name
        platform.code = self.className
        data = {'platform': platform, 'list': []}
        try:
            ssl._create_default_https_context = ssl._create_unverified_context
            endPage = self.getLastPageIndex()
            log.spiderLog('总共{0}页...'.format(endPage), self.className)
            for i in range(endPage):
                log.spiderLog('{0}/{1}页...'.format(i + 1,
                                                   endPage), self.className)
                response = request.urlopen(
                    '{0}&pageno={1}&pagenum={2}'.format(self.url,
                                                        i + 1,
                                                        self.pageNum))
                html = response.read().decode('utf-8')
                pandaTv = json.loads(html)
                items = pandaTv['data']['items']
                infoTime = datetime.now()
                for item in items:
                    catalogName = item['classification']['cname']
                    code = item['id']
                    name = item['userinfo']['nickName']
                    roomUrl = '{0}/{1}'.format(self.root, code)
                    title = item['name']
                    imageUrl = item['pictures']['img']
                    number = int(item['person_num'])
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
        except Exception as e:
            log.spiderLog(e, self.className, log.logLevel.error)
        return data
