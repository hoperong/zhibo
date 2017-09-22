#!/usr/bin/env python
# coding=utf-8

from urllib import request
import ssl
import json

url = r'http://www.huya.com/cache.php'
params = r'?m=LiveList&do=getLiveListByPage&tagAll=0&page='
sumNumber = 0


def getLastPageIndex():
    response = request.urlopen(
        r'{0}{1}1'.format(url, params))
    html = response.read().decode('utf-8')
    yyTv = json.loads(html)
    try:
        pages = int(yyTv['data']['totalPage'])
        return pages
    except Exception:
        return 0


if __name__ == '__main__':
    ssl._create_default_https_context = ssl._create_unverified_context
    endPage = getLastPageIndex()
    print('开始计算，共{0}页数据'.format(endPage))
    for i in range(endPage):
        response = request.urlopen(
            r'{0}{1}{2}'.format(url, params, i + 1))
        html = response.read().decode('utf-8')
        yyTv = json.loads(html)
        items = yyTv['data']['datas']
        for j in range(len(items)):
            sumNumber += int(items[j]['totalCount'])
        print('第{0}/{1}页，在线人数累计{2}人'.format(i + 1, endPage, sumNumber))
    print('计算结束，总共有{0}人'.format(sumNumber))
