#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 16:22
# @Author  : JinShen
# @File    : urls.py
# @Software: PyCharm
# @Site    :
from django.conf.urls import url
from blog import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'), # 起个别名
    url(r'^article/(?P<pk>[0-9]+)/$', views.detail,
        name='detail')  # Named groups
]
