#!/usr/bin/env python
# coding=utf-8

import os


def rootPath():
    '''
        flask目录(物理地址)
    '''

    return os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    )


def logPath():
    '''
        日志根目录
    '''

    return os.path.join(os.path.dirname(rootPath()), 'controlPlatform', 'log')


def logPathPlatform():
    '''
        platform日志目录
    '''

    return os.path.join(logPath(), 'platform')


def logPathSpider(key='unknow'):
    '''
        spider日志目录
    '''

    return os.path.join(logPath(), 'spider', key)
