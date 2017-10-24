#!/usr/bin/env python
# coding=utf-8

from flask import jsonify
from ... import api
from .. import versionCode
from ....system import path
import os


def _getNodeList(path, key):
    if os.path.isfile(path):
        date = os.path.basename(os.path.splitext(path)[0])
        if date == 'log':
            date = ''
        return {
            'key': key,
            'date': date
        }
    elif os.path.isdir(path):
        name = os.path.basename(path)
        dirlist = os.listdir(path)
        nodeInfo = {
            'name': name,
            'list': []
        }
        for i in dirlist:
            if i[0] == '.':
                continue
            nodeInfo['list'].append(_getNodeList(os.path.join(path, i), name))
        return nodeInfo
    else:
        return ''


@api.route('/{0}/log/logFile/getTree/'.format(versionCode),
           endpoint='{0}_log_logFile_getTree'.format(versionCode))
def getTree():
    '''
        获取文件目录树结构
        getTree()
        param:
        return:
                type:list
                format:
                        {
                                'name'[string]:名称,
                                'list'[list|opt]:下级结构,
                                'open'[json|opt]:
                                        {
                                        'key'[string|{platform,douyu,huajiao,panda,quanmin,yy,zhanqi}]:查询种类
                                        'date'[string|format:yyyy-MM-dd]:日期
                                        }
                        }
    '''
    return jsonify(_getNodeList(path.logPath(), ''))


@api.route('/{0}/log/logFile/getContent/<string:key>/<string:date>/'.format(
    versionCode),
    endpoint='{0}_log_logFile_getContent'.format(versionCode))
def getContent(key, date):
    '''
        获取文件内容
        getContent(key,date)
        param:
                key[string|{platform,douyu,huajiao,panda,quanmin,yy,zhanqi}]:查询种类
                date[string|format:yyyy-MM-dd]:日期
        return:
                type:json
                format:
                        {
                                'content'[string]:文本内容
                        }
    '''
    txtContent = ''
    # spiderLogRoot = path.
    if key == 'platform':
        fileName = os.path.join(path.logPathPlatform(), '{0}.txt'.format(date))
        if os.path.isfile(fileName):
            with open(fileName, 'r') as f:
                txtContent = f.read()
    else:
        fileName = os.path.join(path.logPathSpider(key),
                                '{0}.txt'.format(date))
        if os.path.isfile(fileName):
            with open(fileName, 'r') as f:
                txtContent = f.read()
    return jsonify(
        {
            'content': txtContent
        }
    )


@api.route('/{0}/log/logFile/getLogContent/'.format(versionCode),
           endpoint='{0}_log_logFile_getLogContent'.format(versionCode))
def getLogContent():
    '''
        获取log文件内容
        getLogContent()
        param:
        return:
                type:json
                format:
                        {
                                'content'[string]:文本内容
                        }
    '''
    logTxt = os.path.join(path.logPath(), 'log.txt')
    txtContent = ''
    if os.path.isfile(logTxt):
        with open(logTxt, 'r') as f:
            txtContent = f.read()
    return jsonify(
        {
            'content': txtContent
        }
    )
