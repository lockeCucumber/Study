#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import absolute_import

CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/14'
BROKER_URL = 'redis://127.0.0.1:6379/15'

CELERY_TIMEZONE = 'Asia/Shanghai'

from datetime import timedelta
from celery.schedules import crontab

CELERYBEAT_SCHEDULE = {
    'send-email-every-60-seconds': {
         'task': 'schedule_bi.tasks.send_mail',
         'schedule': timedelta(seconds=60),
         'args': ('', ['lockeCucumber@163.com'])
    },
}

# CELERYBEAT_SCHEDULE = {
#     'send-email-every-60-seconds': {
#          'task': 'schedule_bi.tasks.send_mail',
#          'schedule': crontab(),
#          'args': ('', ['lockeCucumber@163.com'])
#     },
# }
