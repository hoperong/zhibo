#!/usr/bin/env python
# coding=utf-8

from flask import render_template
from .. import controller

url_prefix = '/log'


@controller.route('{0}/'.format(url_prefix), endpoint='{0}'.format(url_prefix))
@controller.route('{0}/index/'.format(url_prefix), endpoint='{0}_index'.format(url_prefix))
def index():
    return render_template('log/index.html')


@controller.route('{0}/detail/'.format(url_prefix), endpoint='{0}_detail'.format(url_prefix))
def detail():
    return render_template('log/detail.html')
