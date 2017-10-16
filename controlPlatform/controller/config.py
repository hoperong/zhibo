#!/usr/bin/env python
# coding=utf-8

from config import init, spider


def getSpiderSpider():
    '''
        返回list
    '''

    return spider.spiderList


def getInitDb():
    '''
        返回dic
    '''

    return init.db


def getInitRedis():
    '''
        返回dic
    '''
    return init.redis
