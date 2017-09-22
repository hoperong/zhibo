#!/usr/bin/env python
# coding=utf-8

from urllib import request
import ssl
import json

'''
list/每页数量/页数.json
'''
url = r'http://www.zhanqi.tv/api/static/v2.1/live/list/'
pageNum = 100
sumNumber = 0


def getLastPageIndex():
    response = request.urlopen(
        r'{0}1/1.json'.format(url))
    html = response.read().decode('utf-8')
    zhanqiTV = json.loads(html)
    try:
        total = int(zhanqiTV['data']['cnt'])
        endPage = int(total / pageNum)
        if endPage * pageNum < total:
            endPage += 1
        return endPage
    except Exception:
        return 0


if __name__ == '__main__':
    ssl._create_default_https_context = ssl._create_unverified_context
    endPage = getLastPageIndex()
    print('开始计算，共{0}页数据'.format(endPage))
    for i in range(endPage):
        response = request.urlopen(
            r'{0}/{1}/{2}.json'.format(url, pageNum, i + 1))
        html = response.read().decode('utf-8')
        zhanqiTV = json.loads(html)
        rooms = zhanqiTV['data']['rooms']
        for j in range(len(rooms)):
            sumNumber += int(rooms[j]['online'])
        print('第{0}/{1}页，在线人数累计{2}人'.format(i + 1, endPage, sumNumber))
    print('计算结束，总共有{0}人'.format(sumNumber))
