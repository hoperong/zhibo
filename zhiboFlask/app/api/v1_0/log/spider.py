#!/usr/bin/env python
# coding=utf-8

from flask import jsonify
from ... import api
from .. import versionCode


@api.route('/{0}/log/spider/getList/'.format(versionCode), endpoint='{0}_log_spider_getList'.format(versionCode))
def getList():
    '''
        获取爬虫种类
        getList()
        param:
        return:
                type:list
                format:
                        [
                                {
                                        'key'[string]:种类,
                                        'name'[string]:名称
                                },
                                {...}
                        ]
    '''
    return jsonify(
        [
            {
                'key': '种类',
                'name': '名称'
            }
        ]
    )


@api.route('/{0}/log/spider/getRun/<string:key>/<string:type>/<int:offset>/'.format(versionCode), endpoint='{0}_log_spider_getRun'.format(versionCode))
def getRun(key, type, offset):
    '''
        获取各爬虫运行次数
        getRun(key,type,offset)
        param:
                key[string|{all,douyu,huajiao,panda,quanmin,yy,zhanqi}]:种类(all,返回所有)
                type[string|{d,w,m}]:d-天;w-周;m-月;
                offset[int|{0-30}]:0表示今天（这周，这个月），1表示昨天（上周，上个月）
        return:
                type:list
                format:
                        [
                                {
                                        'key'[string]:种类,
                                        'list'[list]:
                                                [
                                                        {
                                                                'date'[string|format:yyyy-MM-dd]:日期,
                                                                'run'[int]:总次数,
                                                                'success'[int]:成功次数,
                                                                'failed'[int]:失败次数
                                                        },
                                                        {...}
                                                ]
                                },
                                {...}
                        ]
    '''
    return jsonify(
        [
            {
                'key': '种类',
                'list':
                [
                    {
                        'date': '2017-10-19',
                                'run': 2,
                        'success': 3,
                        'failed': 1
                    }
                ]
            }
        ]
    )


@api.route('/{0}/log/platform/getInfo/<string:key>/<string:type>/<int:offset>/'.format(versionCode), endpoint='{0}_log_spider_getInfo'.format(versionCode))
def getInfo(key, type, offset):
    '''
        获取各爬虫的爬取处理情况
        getInfo(key,type,offset)
        param:
                key[string|{all,douyu,huajiao,panda,quanmin,yy,zhanqi}]:种类(all,返回所有)
                type[string|{d,w,m}]:d-天;w-周;m-月;
                offset[int|{0-30}]:0表示今天（这周，这个月），1表示昨天（上周，上个月）
        return:
                type:list
                format:
                        [
                                {
                                        'key'[string]:种类,
                                        'list'[list]:
                                                [
                                                        {
                                                                'date'[string|format:yyyy-MM-dd]:日期,
                                                                'mount'[int]:次数,
                                                                'scrapy'[int]:爬取数量
                                                                'success'[int]:成功保存数量
                                                                'failed'[int]:失败保存数量
                                                        },
                                                        {...}
                                                ]
                                },
                                {...}
                        ]
    '''
    return jsonify(
        [
            {
                'key': '种类',
                'list':
                [
                    {
                        'date': '2017-10-19',
                        'mount': 2,
                        'scrapy': 3,
                        'success': 2,
                        'failed': 2
                    }
                ]
            }
        ]
    )


@api.route('/{0}/log/platform/getRunTime/<string:key>/<string:type>/<int:offset>/'.format(versionCode), endpoint='{0}_log_spider_getRunTime'.format(versionCode))
def getRunTime(key, type, offset):
    '''
        获取各爬虫的爬取时间
        getRunTime(key,type,offset)
        param:
                key[string|{all,douyu,huajiao,panda,quanmin,yy,zhanqi}]:种类(all,返回所有)
                type[string|{d,w,m}]:d-天;w-周;m-月;
                offset[int|{0-30}]:0表示今天（这周，这个月），1表示昨天（上周，上个月）
        return:
                type:list
                format:
                        [
                                {
                                        'key'[string]:种类,
                                        'list'[list]:
                                                [
                                                        {
                                                                'date'[string|format:yyyy-MM-dd]:日期,
                                                                'mount'[int]:次数,
                                                                'time'[int]:多少秒
                                                                'scrapyTime'[int]:多少秒
                                                                'saveTime'[int]:多少秒
                                                        },
                                                        {...}
                                                ]
                                },
                                {...}
                        ]
    '''
    return jsonify(
        [
            {
                'key': '种类',
                'list':
                [
                    {
                        'date': '2017-10-19',
                        'mount': 8,
                        'time': 8,
                        'scrapyTime': 8,
                        'saveTime': 8
                    }
                ]
            }
        ]
    )
