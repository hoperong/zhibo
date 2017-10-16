#!usr/bin/env python
# coding=utf-8


class db:

    __db = None

    @property
    def db(self):
        return self.__db

    def __init__(self, db):
        self.__db = db

    def save(self, data):
        pass
