#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 16:22
# @Author  : JinShen
# @File    : urls.py
# @Software: PyCharm
# @Site    :
from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$',views.index,name='index')#起个别名
]
