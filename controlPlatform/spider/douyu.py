#!/usr/bin/env python
# coding=utf-8

from bs4 import BeautifulSoup
from urllib import request
import ssl
import re

url = r'https://www.douyu.com/directory/all'
sumNumber = 0


def getLastPageIndex():
    response = request.urlopen(url)
    page = response.read().decode('utf-8')
    html = BeautifulSoup(page, 'html.parser')
    endPage = html.select('script')
    re_result = ''
    for i in range(len(endPage)):
        if '$PAGE' in endPage[i].get_text():
            re_result = re.findall('count: "(.+?)",', endPage[i].get_text())
    try:
        return int(re_result[0])
    except Exception:
        return 1


if __name__ == '__main__':
    ssl._create_default_https_context = ssl._create_unverified_context
    endPage = getLastPageIndex()
    print('开始计算，共{0}页数据'.format(endPage))
    for i in range(endPage):
        response = request.urlopen('{0}?page={1}'.format(url, i + 1))
        page = response.read().decode('utf-8')
        html = BeautifulSoup(page, 'html.parser')
        number = html.select(
            '#live-list-contentbox > li > a > div > p > .dy-num')
        for j in range(len(number)):
            numberStr = number[j].get_text()
            if '万' in numberStr:
                newNumber = numberStr[:len(numberStr) - 1]
                sumNumber += int((float(newNumber) * 10000))
            else:
                sumNumber += int(numberStr)
        print('第{0}/{1}页，在线人数累计{2}人'.format(i + 1, endPage, sumNumber))
    print('计算结束，总共有{0}人'.format(sumNumber))
