#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import absolute_import
from proj.celery import app

@app.task
def add(x, y):
    print x + y

@app.task
def mul(x, y):
    return x * y

@app.task
def xsum(numbers):
    return sum(numbers)