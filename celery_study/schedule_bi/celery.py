#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import absolute_import
from celery import Celery

app = Celery('schedule_bi', include=['schedule_bi.tasks'])

app.config_from_object('schedule_bi.schedule_config')

if __name__ == '__main__':
    app.start()
# celery -A schedule_bi worker -B -l info