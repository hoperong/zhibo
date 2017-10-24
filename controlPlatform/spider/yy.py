#!/usr/bin/env python
# coding=utf-8

from urllib import request
import json
from model import spider, model
from controller import log
from datetime import datetime


class yy(spider.spider):

    root = 'http://www.huya.com'
    url = '{0}/cache.php'.format(root)
    params = '?m=LiveList&do=getLiveListByPage&tagAll=0&page='
    name = '虎牙直播'

    def getLastPageIndex(self):
        response = request.urlopen(
            r'{0}{1}1'.format(self.url, self.params))
        html = response.read().decode('utf-8')
        yyTv = json.loads(html)
        try:
            pages = int(yyTv['data']['totalPage'])
            return pages
        except Exception:
            return 0

    def run(self):
        log.spiderLog('开始爬取...', self.className)
        platform = model.Platform()
        platform.name = self.name
        platform.code = self.className
        data = {'platform': platform, 'list': []}
        try:
            endPage = self.getLastPageIndex()
            for i in range(endPage):
                response = request.urlopen(
                    '{0}{1}{2}'.format(self.url, self.params, i + 1))
                html = response.read().decode('utf-8')
                yyTv = json.loads(html)
                items = yyTv['data']['datas']
                infoTime = datetime.now()
                isOver = False
                for item in items:
                    catalogName = item['gameFullName']
                    code = item['uid']
                    name = item['nick']
                    roomUrl = '{0}/{1}'.format(self.root, item['privateHost'])
                    title = item['roomName']
                    imageUrl = item['screenshot']
                    number = int(item['totalCount'])
                    # 不足100的话，接下来的都不要了
                    if number <= 100:
                        isOver = True
                        break
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
                if isOver:
                    break
        except Exception as e:
            log.spiderLog(e, self.className, log.logLevel.error)
        log.spiderLog('爬取结束,共爬取{0}条数据...'.format(
            len(data['list'])), self.className)
        return data
