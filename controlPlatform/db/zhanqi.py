#!usr/bin/env python
# coding=utf-8

from model import db, model
from sqlalchemy import and_
from controller import log


class zhanqi(db.db):

    def save(self, data):
        log.spiderLog('开始保存数据...', data['platform'].code)
        # 效验平台信息的正确性
        platform = self.db.query(model.Platform).filter(
            model.Platform.code == data['platform'].code).first()
        if platform is None:
            platform = data['platform']
            self.db.add(platform)
        else:
            if(platform.name != data['platform'].name):
                platform.name = data['platform'].name
        self.db.commit()
        log.spiderLog('platform信息保存成功...', data['platform'].code)
        log.spiderLog('开始保存列表数据，总共{0}个...'.format(
            len(data['list'])), data['platform'].code)
        for index, item in enumerate(data['list']):
            try:
                log.spiderLog('{0}/{1}...'.format(index, len(data['list'])),
                              data['platform'].code)
                # catalog信息以前是否存在
                catalog = self.db.query(model.Catalog).filter(
                    and_(model.Catalog.name == item['catalog'].name,
                         model.Catalog.platformId == platform.platformId)
                ).first()
                if catalog is None:
                    catalog = item['catalog']
                    sort = self.db.query(model.Sort).filter_by(
                        name=catalog.name).first()
                    if sort is None:
                        sort = model.Sort()
                        sort.name = catalog.name
                        self.db.add(sort)
                        self.db.commit()
                    catalog.sortId = sort.sortId
                    catalog.platformId = platform.platformId
                    self.db.add(catalog)
                self.db.commit()
                # room信息以前是否存在
                room = self.db.query(model.Room).filter(
                    and_(model.Room.code == item['room'].code,
                         model.Room.platformId == platform.platformId)
                ).first()
                if room is None:
                    room = item['room']
                    room.platformId = platform.platformId
                    room.catalogId = catalog.catalogId
                    self.db.add(room)
                else:
                    room.catalogId = catalog.catalogId
                    room.name = item['room'].name
                    room.roomUrl = item['room'].roomUrl
                    room.title = item['room'].title
                    room.imageUrl = item['room'].imageUrl
                self.db.commit()
                # 录入info信息
                info = item['info']
                info.roomId = room.roomId
                info.catalogId = catalog.catalogId
                self.db.add(info)
                self.db.commit()
            except Exception as e:
                self.db.rollback()
                log.spiderLog(e, data['platform'].code)
        log.spiderLog('结束保存数据...', data['platform'].code)
