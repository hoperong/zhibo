#!/usr/bin/env python
# coding=utf-8


class spider:

    __headers = {
        'User-Agent': r'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }

    @property
    def headers(self):
        return self.__headers

    @property
    def className(self):
        return self.__class__.__name__

    def run(self):
        return {}
