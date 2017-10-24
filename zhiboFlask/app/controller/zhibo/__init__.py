#!/usr/bin/env python
# coding=utf-8

from flask import render_template
from .. import controller


@controller.route('/')
@controller.route('/index/')
def index():
    return render_template('zhibo/index.html')
