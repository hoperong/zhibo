#!/usr/bin/env python
# coding=utf-8

from urllib import request
import json
from model import spider, model
from controller import log
from datetime import datetime


'''
list/每页数量/页数.json
'''


class zhanqi(spider.spider):

    root = 'http://www.zhanqi.tv'
    url = '{0}/api/static/v2.1/live/list/'.format(root)
    name = '战旗直播'

    def getMount(self):
        response = request.urlopen('{0}1/1.json'.format(self.url))
        html = response.read().decode('utf-8')
        zhanqiTV = json.loads(html)
        total = int(zhanqiTV['data']['cnt'])
        return total

    def run(self):
        log.spiderLog('开始爬取...', self.className)
        platform = model.Platform()
        platform.name = self.name
        platform.code = self.className
        data = {'platform': platform, 'list': []}
        try:
            mount = self.getMount()
            response = request.urlopen('{0}{1}/1.json'.format(self.url, mount))
            html = response.read().decode('utf-8')
            zhanqiTV = json.loads(html)
            items = zhanqiTV['data']['rooms']
            infoTime = datetime.now()
            for item in items:
                catalogName = item['newGameName']
                code = item['uid']
                name = item['nickname']
                roomUrl = item['url'] if item['url'].find(
                    'http') > -1 else '{0}{1}'.format(self.root, item['url'])
                title = item['title']
                imageUrl = item['bpic']
                number = int(item['online'])
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
        except Exception as e:
            log.spiderLog(e, self.className, log.logLevel.error)
        log.spiderLog('爬取结束,共爬取{0}条数据...'.format(
            len(data['list'])), self.className)
        return data
