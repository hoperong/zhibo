#!/usr/bin/env python
# coding=utf-8

from urllib import request
from bs4 import BeautifulSoup
import ssl
import json

categoryList = []
url = r'http://www.huajiao.com'
interfaceUrl = r'http://webh.huajiao.com/live/listcategory?offset=0&fmt=jsonp'
sumNumber = 0


def getCategoryList():
    response = request.urlopen('{0}/category/{1}'.format(url, 1000))
    html = BeautifulSoup(response.read().decode('utf-8'), 'html.parser')
    result = html.select('.detail-items > dl > dd > a')
    if len(result) > 2:
        targetList = result[1:len(result) - 1]
        for target in targetList:
            attr = target['data-bk']
            attrResult = attr.split('-')
            if len(attrResult) > 1:
                categoryList.append(attrResult[1])
    return


if __name__ == '__main__':
    ssl._create_default_https_context = ssl._create_unverified_context
    getCategoryList()
    print('开始计算，共{0}个分类'.format(len(categoryList)))
    for i in range(len(categoryList)):
        response = request.urlopen(
            '{0}&cateid={1}&nums={2}'.format(interfaceUrl, categoryList[i], 0))
        html = response.read().decode('utf-8')
        huajiaoTv = json.loads(html)
        total = huajiaoTv['data']['total']
        response = request.urlopen(
            '{0}&cateid={1}&nums={2}'.format(
                interfaceUrl, categoryList[i], total))
        huajiaoTv = json.loads(html)
        feeds = huajiaoTv['data']['feeds']
        for feed in feeds:
            numberStr = feed['feed']['watches']
            sumNumber += int(numberStr)
        print('第{0}/{1}个分类，在线人数累计{2}人'.format(i +
                                              1, len(categoryList), sumNumber))
    print('计算结束，总共有{0}人'.format(sumNumber))
