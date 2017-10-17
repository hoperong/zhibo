#!/usr/bin/env python
# coding=utf-8

import datetime
from controller import path
import os
from enum import Enum


class logLevel(Enum):
    normal = 0
    success = 1
    warm = 2
    error = 3


def write(str=''):
    '''
            log文件输入内容
            str:内容
    '''

    logStr = '{0}\n{1}\n'.format(str, ('*' * 50))
    print(logStr)
    dirPath = path.logPath()
    if not os.path.isdir(dirPath):
        os.makedirs(dirPath)
    with open(os.path.join(dirPath, 'log.txt'),
              'a',
              encoding='utf-8'
              ) as f:
        f.write(logStr)


def platformLog(str='', level=logLevel.normal, date=datetime.date.today()):
    '''
            平台日志log文件输入内容
            str:内容
            level:日志级别
            date:日期
    '''

    logStr = '{0}\t{1}\t{2}\n'.format(datetime.datetime.now(), level.name, str)
    print(logStr)
    dirPath = path.logPathPlatform()
    if not os.path.isdir(dirPath):
        os.makedirs(dirPath)
    with open(os.path.join(dirPath, '{0}.txt'.format(date)),
              'a',
              encoding='utf-8'
              ) as f:
        f.write(logStr)


def spiderLog(str='', key='unknow',
              level=logLevel.normal, date=datetime.date.today()):
    '''
            爬虫日志log文件输入内容
            str:内容
            key:爬虫标示
            level:日志级别
            date:日期
    '''

    logStr = '{0}\t{1}\t{2}\n'.format(datetime.datetime.now(), level.name, str)
    print(logStr)
    dirPath = path.logPathSpider(key)
    if not os.path.isdir(dirPath):
        os.makedirs(dirPath)
    with open(os.path.join(dirPath, '{0}.txt'.format(date)),
              'a',
              encoding='utf-8'
              ) as f:
        f.write(logStr)
