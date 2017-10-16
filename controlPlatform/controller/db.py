#!/usr/bin/env python
# conding=utf-8

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model import model


def getEngine(config):
    try:
        engine = create_engine(
            "{0}+{1}://{2}:{3}@{4}:{5}/{6}?charset={7}".format(
                config['dialect'],
                config['driver'],
                config['user'],
                config['password'],
                config['host'],
                config['port'],
                config['db'],
                config['charset']
            ),
            encoding=config['encoding']
        )
        return engine
    except Exception:
        return None


def createDb(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def createTable(engine):
    '''
        test
    '''
    model.Base.metadata.create_all(engine)


def dropTable(engine):
    '''
        test
    '''
    model.Base.metadata.drop_all(engine)
