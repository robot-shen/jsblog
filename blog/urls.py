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

#todo https://www.zmrenwu.com/post/16/
#我弄出来了 blogs\urls.py 里面加 app_name = 'blog'
# 把 blogproject\urls.py 里面的 namespace= blog 删掉
urlpatterns = [
    url(r'^$', views.index, name='index'), # 起个别名
    url(r'^index.html/$', views.index),
    url(r'^article/(?P<pk>[0-9]+)/$', views.detail,
        name='detail'),  # Named groups
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.archives,name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$',views.category,name='category'),
]
