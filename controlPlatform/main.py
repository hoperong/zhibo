#!/usr/bin/env python
# coding=utf-8

from model import platform

if __name__ == '__main__':
    app = platform.platform()
    app.run()
    app.close()
