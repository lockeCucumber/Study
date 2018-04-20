# coding: utf8
import os

BASE_URL = 'http://jsonplaceholder.typicode.com'
SKIP_REAL = os.getenv('SKIP_REAL', False) # 一般会考虑本地开发环境一些测试跳过，所以设置一个全局变量