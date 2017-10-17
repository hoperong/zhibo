#!/usr/bin/env python
# coding=utf-8

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, BigInteger, String, DateTime, ForeignKey, text
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()


class Info(Base):
    __tablename__ = 'Info'
    infoId = Column('infoId',
                    Integer,
                    primary_key=True,
                    autoincrement=True)
    roomId = Column('roomId',
                    Integer,
                    ForeignKey('Room.roomId'),
                    nullable=False,
                    default=0,
                    server_default='0')
    catalogId = Column('catalogId',
                       Integer,
                       ForeignKey('Catalog.catalogId'),
                       nullable=False,
                       default=0,
                       server_default='0')
    number = Column('number',
                    BigInteger,
                    nullable=False,
                    default=0,
                    server_default='0')
    time = Column('time',
                  DateTime(),
                  nullable=False,
                  default=datetime.now(),
                  server_default=text('NOW()'))
    # 关系对象
    room = relationship('Room')
    catalog = relationship('Catalog')


class Catalog(Base):
    __tablename__ = 'Catalog'
    catalogId = Column('catalogId',
                       Integer,
                       primary_key=True,
                       autoincrement=True)
    name = Column('name',
                  String(100),
                  unique=True,
                  nullable=False,
                  default='',
                  server_default='')
    platformId = Column('platformId',
                        Integer,
                        ForeignKey('Platform.platformId'),
                        nullable=False,
                        default=0,
                        server_default='0')
    sortId = Column('sortId',
                    Integer,
                    ForeignKey('Sort.sortId'),
                    nullable=False,
                    default=0,
                    server_default='0')
    # 关系对象
    platform = relationship('Platform')
    sort = relationship('Sort')
    infos = relationship('Info')
    rooms = relationship('Room')


class Room(Base):
    __tablename__ = 'Room'
    roomId = Column('roomId', Integer,
                    primary_key=True, autoincrement=True)
    code = Column('code', String(100), nullable=False, server_default='')
    platformId = Column('platformId',
                        Integer,
                        ForeignKey('Platform.platformId'),
                        nullable=False,
                        default=0,
                        server_default='0')
    catalogId = Column('catalogId',
                       Integer,
                       ForeignKey('Catalog.catalogId'),
                       nullable=False,
                       default=0,
                       server_default='0')
    name = Column('name',
                  String(100),
                  nullable=False,
                  default='',
                  server_default='')
    roomUrl = Column('roomUrl',
                     String(500),
                     nullable=False,
                     default='',
                     server_default='')
    title = Column('title',
                   String(100),
                   nullable=False,
                   default='',
                   server_default='')
    imageUrl = Column('imageUrl',
                      String(500),
                      nullable=False,
                      default='',
                      server_default='')
    # 关系对象
    platform = relationship('Platform')
    infos = relationship('Info')
    catalog = relationship('Catalog')


class Platform(Base):
    __tablename__ = 'Platform'
    platformId = Column('platformId',
                        Integer,
                        primary_key=True,
                        autoincrement=True)
    name = Column('name',
                  String(100),
                  unique=True,
                  nullable=False,
                  default='',
                  server_default='')
    code = Column('code',
                  String(100),
                  unique=True,
                  nullable=False,
                  default='',
                  server_default='')
    # 关系对象
    rooms = relationship('Room')
    catalogs = relationship('Catalog')


class Sort(Base):
    __tablename__ = 'Sort'
    sortId = Column('sortId',
                    Integer,
                    primary_key=True,
                    autoincrement=True)
    name = Column('name',
                  String(100),
                  unique=True,
                  nullable=False,
                  default='',
                  server_default='')
    # 关系对象
    catalogs = relationship('Catalog')
