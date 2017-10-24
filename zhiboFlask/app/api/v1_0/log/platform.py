#!/usr/bin/env python
# coding=utf-8

from flask import jsonify
from ... import api
from .. import versionCode


@api.route('/{0}/log/platform/getRun/<string:type>/<int:offset>/'.format(versionCode), endpoint='{0}_log_platform_getRun'.format(versionCode))
def getRun(type, offset):
    '''
        获取平台运行次数
        getRun(type,offset)
        param:
                type[string|{d,w,m}]:d-天;w-周;m-月;
                offset[int|{0-30}]:0表示今天（这周，这个月），1表示昨天（上周，上个月）
        return:
                type:list
                format:
                        [
                                {
                                        'date'[string|format:yyyy-MM-dd]:日期,
                                        'run'[int]:总次数,
                                        'success'[int]:成功次数,
                                        'failed'[int]:失败次数
                                },
                                {...}
                        ]
    '''
    return jsonify(
        [
            {
                'date': '2017-10-19',
                'run': 3,
                'success': 3,
                'failed': 3
            }
        ]
    )


@api.route('/{0}/log/platform/getLogError/<string:key>/<string:date>/'.format(versionCode), endpoint='{0}_log_platform_getLogError'.format(versionCode))
def getLogError(type, offset):
    '''
        获取平台运行存在错误报告次数
        getLogError(type,offset)
        param:
                type[string|{d,w,m}]:d-天;w-周;m-月;
                offset[int|{0-30}]:0表示今天（这周，这个月），1表示昨天（上周，上个月）
        return:
                type:list
                format:
                        [
                                {
                                        'date'[string|format:yyyy-MM-dd]:日期,
                                        'mount'[int]:次数
                                },
                                {...}
                        ]
    '''
    return jsonify(
        [
            {
                'date': '2017-10-19',
                'mount': 3
            }
        ]
    )


@api.route('/{0}/log/platform/getRunTime/<string:key>/<string:date>/'.format(versionCode), endpoint='{0}_log_platform_getRunTime'.format(versionCode))
def getRunTime(type, offset):
    '''
        获取平台每次运行时间
        getRunTime(type,offset)
        param:
                type[string|{d,w,m}]:d-天;w-周;m-月;
                offset[int|{0-30}]:0表示今天（这周，这个月），1表示昨天（上周，上个月）
        return:
                type:list
                format:
                        [
                                {
                                        'date'[string|format:yyyy-MM-dd]:日期,
                                        'mount'[int]:次数,
                                        'time'[int]:多少秒
                                },
                                {...}
                        ]
    '''
    return jsonify(
        [
            {
                'date': '2017-10-19',
                'mount': 3,
                'time': 2
            }
        ]
    )
