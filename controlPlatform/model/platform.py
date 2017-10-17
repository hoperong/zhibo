#!/usr/bin/env python
# coding=utf-8

from model import singleton
from controller import config, db, log


class platform(singleton.singleton):

    __config = {}
    __db = None

    @property
    def config(self):
        return self.__config

    @property
    def db(self):
        return self.__db

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, 'platform', *args, **kwargs)

    def __init__(self, *args, **kwargs):
        log.platformLog('platform开始初始化...')
        try:
            # 导入基本配置信息
            log.platformLog('platform开始导入基本配置信息...')
            self.config['redis'] = config.getInitRedis()
            self.config['db'] = config.getInitDb()
            # 导入数据库session
            log.platformLog('platform开始导入数据库session...')
            self.__db = db.createDb(db.getEngine(self.config['db']))
        except Exception as e:
            log.platformLog(e, log.logLevel.error)
        log.platformLog('platform结束初始化...')

    def run(self):
        log.platformLog('platform开始运行...')
        try:
            spiderList = config.getSpiderSpider()
            for spider in spiderList:
                try:
                    log.platformLog('运行{0}爬虫...'.format(spider))
                    m_spider = __import__('spider', fromlist=[spider])
                    c_spider = getattr(getattr(m_spider, spider), spider)
                    i_spider = c_spider()
                    data = i_spider.run()
                    log.platformLog('{0}爬虫爬取结束...'.format(spider))
                    log.platformLog('开始处理{0}爬虫爬取的数据...'.format(spider))
                    m_db = __import__('db', fromlist=[spider])
                    c_db = getattr(getattr(m_db, spider), spider)
                    i_db = c_db(self.db)
                    i_db.save(data)
                    log.platformLog('结束处理{0}爬虫爬取的数据...'.format(spider))
                except Exception as ee:
                    log.platformLog(ee, log.logLevel.error)
        except Exception as e:
            log.platformLog(e, log.logLevel.error)
        log.platformLog('platform结束运行...')

    def close(self):
        log.platformLog('platform即将关闭...')
        try:
            self.db.close()
        except Exception as e:
            log.platformLog(e, log.logLevel.error)
        log.platformLog('platform关闭...', log.logLevel.success)
