#!/usr/bin/env python
# coding=utf-8


def create_db():
    '''
    创建数据库
    '''
    from controller import db
    from model import platform
    app = platform.platform()
    db.dropTable(db.getEngine(app.config['db']))
    db.createTable(db.getEngine(app.config['db']))
    app.close()


def test_spider():
    '''
    测试爬虫
    '''
    from model import platform
    from spider import zhanqi
    app = platform.platform()
    d = zhanqi.zhanqi()
    print(d.run())
    app.close()


if __name__ == '__main__':
    create_db()
