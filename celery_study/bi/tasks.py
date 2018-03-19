#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import absolute_import
from bi.celery import app

import MySQLdb
import datetime
import xlwt
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from cStringIO import StringIO
import sys
reload(sys)
sys.setdefaultencoding('utf8')


@app.task
def send_mail(excel_files, recipients):
    username = 'tech@epiclouds.net'
    password = '123Yuanshuju'
    sender = username
    receivers = ", ".join(recipients)

    # 如名字所示： Multipart就是多个部分
    msg = MIMEMultipart()
    msg['Subject'] = 'Daily Data Report'
    msg['From'] = sender
    msg['To'] = receivers

    # 正文
    puretext = MIMEText('Attached please find the latest data report.', _charset='UTF-8')
    msg.attach(puretext)

    # xlsx类型的附件
    # for excel_file in excel_files:
    #     try:
    #         xlsxpart = MIMEApplication(open(excel_file, 'rb').read())
    #         xlsxpart.add_header('Content-Disposition', 'attachment',
    #                             filename=excel_file.split('/')[-1].encode('gbk'))
    #         msg.attach(xlsxpart)
    #     except IOError:
    #         print '要添加的附件本身不存在'

    try:
        host = 'smtp.mxhichina.com'
        port = 465
        client = smtplib.SMTP_SSL(host, port)
        client.login(username, password)
        client.sendmail(sender, receivers, msg.as_string())
        client.quit()
        print 'yeah'
    except smtplib.SMTPRecipientsRefused:
        print 'Recipient refused'
    except smtplib.SMTPAuthenticationError:
        print 'Auth error'
    except smtplib.SMTPSenderRefused:
        print 'Sender refused'
    except smtplib.SMTPException, e:
        print e.message
    except Exception, e:
        print e.message