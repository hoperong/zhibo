#!/usr/bin/env python
# coding=utf-8

from urllib import request
import ssl
import json

'''
status:0-所有   2-正在
order:person_num
pageno:页数，1开始
pagenum:每页项目数
'''
url = r'https://www.panda.tv/live_lists?status=2&order=person_num'
pageNum = 120
sumNumber = 0


def getLastPageIndex():
    response = request.urlopen(
        r'{0}&pageno=1&pagenum=1'.format(url))
    html = response.read().decode('utf-8')
    pandaTv = json.loads(html)
    try:
        total = int(pandaTv['data']['total'])
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
            r'{0}&pageno={1}&pagenum={2}'.format(url, i + 1, pageNum))
        html = response.read().decode('utf-8')
        pandaTv = json.loads(html)
        items = pandaTv['data']['items']
        for j in range(len(items)):
            sumNumber += int(items[j]['person_num'])
        print('第{0}/{1}页，在线人数累计{2}人'.format(i + 1, endPage, sumNumber))
    print('计算结束，总共有{0}人'.format(sumNumber))
