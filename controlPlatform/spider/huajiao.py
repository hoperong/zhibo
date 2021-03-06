#!/usr/bin/env python
# coding=utf-8

from urllib import request
from bs4 import BeautifulSoup
import json
from model import spider, model
from controller import log
from datetime import datetime


class huajiao(spider.spider):

    url = r'http://www.huajiao.com'
    interfaceUrl = r'http://webh.huajiao.com/live/listcategory?fmt=jsonp'
    pageMount = 100
    name = '花椒直播'

    def getCategoryList(self):
        categoryList = []
        response = request.urlopen('{0}/category/{1}'.format(self.url, 1000))
        html = BeautifulSoup(response.read().decode('utf-8'), 'html.parser')
        result = html.select('.detail-items > dl > dd > a')
        if len(result) > 2:
            targetList = result[1:len(result) - 1]
            for target in targetList:
                attr = target['data-bk']
                attrResult = attr.split('-')
                if len(attrResult) > 1:
                    categoryList.append(attrResult[1])
        return categoryList

    def run(self):
        log.spiderLog('开始爬取...', self.className)
        platform = model.Platform()
        platform.name = self.name
        platform.code = self.className
        data = {'platform': platform, 'list': []}
        try:
            categoryList = self.getCategoryList()
            for i in range(len(categoryList)):
                j = 0
                infoTime = datetime.now()
                isOver = False
                while 1 == 1:
                    response = request.urlopen(
                        '{0}&offset={1}&cateid={2}&nums={3}'.format(
                            self.interfaceUrl,
                            j,
                            categoryList[i],
                            self.pageMount)
                    )
                    html = response.read().decode('utf-8')
                    huajiaoTv = json.loads(html)
                    if len(huajiaoTv['data']) <= 0:
                        break
                    feeds = huajiaoTv['data']['feeds']
                    for feed in feeds:
                        catalogName = feed['feed']['live_cate'] if feed['feed']['game'] == '' else feed['feed']['game']
                        code = feed['feed']['feedid']
                        name = feed['author']['nickname']
                        roomUrl = '{0}/l/{1}'.format(self.url, code)
                        title = feed['feed']['title']
                        imageUrl = feed['feed']['feedid']
                        number = int(feed['feed']['watches'])
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
                    j += self.pageMount
                    if isOver:
                        break
        except Exception as e:
            log.spiderLog(e, self.className, log.logLevel.error)
        log.spiderLog('爬取结束,共爬取{0}条数据...'.format(
            len(data['list'])), self.className)
        return data
