#!/usr/bin/env python
# coding=utf-8


class singleton:
    '''
        单例的基类
    '''
    __singletonObject = {}

    def __new__(cls, name, *args, **kwargs):
        if name not in cls.__singletonObject:
            cls.__singletonObject[name] = super(singleton,
                                                cls).__new__(cls,
                                                             *args,
                                                             **kwargs)
        return cls.__singletonObject[name]
