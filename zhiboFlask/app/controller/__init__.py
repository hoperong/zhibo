#!/usr/bin/env python
# coding=utf-8

from flask import Blueprint

controller = Blueprint('controller', __name__)

from . import log, zhibo
