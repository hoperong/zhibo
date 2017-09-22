#!/usr/bin/env python
# conding=utf-8

from urllib import request
from bs4 import BeautifulSoup
import ssl
import re

url = r'https://www.quanmin.tv/game/all'
sumNumber = 0


def getLastPageIndex():
    response = request.urlopen(url)
    page = response.read().decode('utf-8')
    html = BeautifulSoup(page, 'html.parser')
    result = html.find_all(class_=re.compile('list_w-paging_num'))
    try:
        re_result = result[-1].get_text() if len(result) > 0 else 1
        return int(re_result)
    except Exception:
        return 1


if __name__ == '__main__':
    ssl._create_default_https_context = ssl._create_unverified_context
    endPage = getLastPageIndex()
    print('开始计算，共{0}页数据'.format(endPage))
    for i in range(endPage):
        response = request.urlopen('{0}?p={1}'.format(url, i + 1))
        page = response.read().decode('utf-8')
        html = BeautifulSoup(page, 'html.parser')
        number = html.select(
            '.list_w-videos_video-list > li > div > div > a > .common_w-card_bottom > div > div > .common_w-card_views-num')
        for j in range(len(number)):
            numberStr = number[j].get_text()
            sumNumber += int(numberStr)
        print('第{0}/{1}页，在线人数累计{2}人'.format(i + 1, endPage, sumNumber))
    print('计算结束，总共有{0}人'.format(sumNumber))
