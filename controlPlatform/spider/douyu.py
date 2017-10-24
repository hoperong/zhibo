#!/usr/bin/env python
# coding=utf-8

from bs4 import BeautifulSoup
from urllib import request
import ssl
import re
from model import spider, model
from datetime import datetime
from controller import log


class douyu(spider.spider):

    root = r'https://www.douyu.com'
    url = '{0}/directory/all'.format(root)
    name = '斗鱼'

    def getLastPageIndex(self):
        '''
        获取页数
        '''
        req = request.Request(self.url, headers=self.headers)
        response = request.urlopen(req)
        page = response.read().decode('utf-8')
        html = BeautifulSoup(page, 'html.parser')
        endPage = html.select('script')
        re_result = ''
        for i in range(len(endPage)):
            if '$PAGE' in endPage[i].get_text():
                re_result = re.findall(
                    'count: "(.+?)",', endPage[i].get_text())
        try:
            return int(re_result[0])
        except Exception:
            return 1

    def run(self):
        log.spiderLog('开始爬取...', self.className)
        platform = model.Platform()
        platform.name = self.name
        platform.code = self.className
        data = {'platform': platform, 'list': []}
        try:
            ssl._create_default_https_context = ssl._create_unverified_context
            endPage = self.getLastPageIndex()
            for i in range(endPage):
                reUrl = '{0}?page={1}'.format(self.url, i + 1)
                req = request.Request(reUrl, headers=self.headers)
                response = request.urlopen(req)
                page = response.read().decode('utf-8')
                html = BeautifulSoup(page, 'html.parser')
                lis = html.select('#live-list-contentbox > li')
                infoTime = datetime.now()
                isOver = False
                for li in lis:
                    catalogName = li.select('a > div > div > span')[
                        0].get_text()
                    code = li['data-rid']
                    name = li.select('a > div > p > span')[0].get_text()
                    roomUrl = '{0}{1}'.format(self.root, li.a['href'])
                    title = li.a['title']
                    imageUrl = li.select('a > span > img')[0]['src']
                    numberStr = li.select('a > div > p > span')[1].get_text()
                    number = 0
                    if '万' in numberStr:
                        newNumber = numberStr[:len(numberStr) - 1]
                        number = int((float(newNumber) * 10000))
                    else:
                        number = int(numberStr)
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
