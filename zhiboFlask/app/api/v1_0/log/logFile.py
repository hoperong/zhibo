#!/usr/bin/env python
# coding=utf-8

from flask import jsonify
from ... import api
from .. import versionCode


@api.route('/{0}/log/logFile/getTree/'.format(versionCode), endpoint='{0}_log_logFile_getTree'.format(versionCode))
def getTree():
    '''
        获取文件目录树结构
        getTree()
        param:
        return:
                type:list
                format:
                        [
                                {
                                        'name'[string]:名称,
                                        'list'[list|opt]:下级结构,
                                        'open'[json|opt]:
                                                {
                                                'key'[string|{platform,douyu,huajiao,panda,quanmin,yy,zhanqi}]:查询种类
                                                'date'[string|format:yyyy-MM-dd]:日期
                                                }
                                },
                                {...}
                        ]
    '''
    return jsonify(
        [
            {
                'name': '名称',
                'list': '下级结构',
                'open':
                {
                    'key': 'platform',
                    'date': '2017-10-19'
                }
            }
        ]
    )


@api.route('/{0}/log/logFile/getContent/<string:key>/<string:date>/'.format(versionCode), endpoint='{0}_log_logFile_getContent'.format(versionCode))
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
    return jsonify(
        {
            'content': '文本内容'
        }
    )


@api.route('/{0}/log/logFile/getLogContent/'.format(versionCode), endpoint='{0}_log_logFile_getLogContent'.format(versionCode))
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
    return jsonify(
        {
            'content': '文本内容'
        }
    )
