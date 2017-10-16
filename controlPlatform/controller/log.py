#!/usr/bin/env python
# coding=utf-8

import datetime
from controller import path
import os


def write(str=''):
    '''
            log文件输入内容
            str:内容
    '''

    logStr = '''
            time:{0}
            content:{1}\n
            {2}
                     '''.format(datetime.datetime.now(), str, ('*' * 50))
    print(logStr)
    dirPath = path.logPath()
    if not os.path.isdir(dirPath):
        os.makedirs(dirPath)
    with open(os.path.join(dirPath, 'log.txt'),
              'a',
              encoding='utf-8'
              ) as f:
        f.writelines(logStr)


def platformLog(str='', date=datetime.date.today()):
    '''
            平台日志log文件输入内容
            str:内容
            date:日期
    '''

    logStr = '''
            time:{0}
            content:{1}\n
            {2}
                     '''.format(datetime.datetime.now(), str, ('*' * 50))
    print(logStr)
    dirPath = path.logPathPlatform()
    if not os.path.isdir(dirPath):
        os.makedirs(dirPath)
    with open(os.path.join(dirPath, '{0}.txt'.format(date)),
              'a',
              encoding='utf-8'
              ) as f:
        f.writelines(logStr)


def spiderLog(str='', key='unknow', date=datetime.date.today()):
    '''
            爬虫日志log文件输入内容
            str:内容
            key:爬虫标示
            date:日期
    '''

    logStr = '''
            time:{0}
            content:{1}\n
            {2}
                     '''.format(datetime.datetime.now(), str, ('*' * 50))
    print(logStr)
    dirPath = path.logPathSpider(key)
    if not os.path.isdir(dirPath):
        os.makedirs(dirPath)
    with open(os.path.join(dirPath, '{0}.txt'.format(date)),
              'a',
              encoding='utf-8'
              ) as f:
        f.writelines(logStr)
