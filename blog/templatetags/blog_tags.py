#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/13 16:26
# @Author  : JinShen
# @File    : blog_tags.py
# @Software: PyCharm
# @Site    :

from ..models import Article,Category
from django import template
from django.db.models import Count

register = template.Library()

@register.simple_tag
#最新模板标签
def get_recent_posts(num=5):
    '''
    这里我们首先导入 template 这个模块，然后实例化了一个 template.Library 类，
    并将函数 get_recent_posts 装饰为 register.simple_tag。
    这样就可以在模板中使用语法 {% get_recent_posts %} 调用这个函数了。
    '''

    return Article.objects.all().order_by('-created_time')[:num]


@register.simple_tag
#归档模板标签
def archives():
    # obj = Article.objects.dates('created_time', 'month', order='DESC')
    #想通了，obj的值是QuerySet。本质上是个集合，自带去重功能。所以得到的结果是各个月份
    obj = Article.objects.dates('created_time', 'month', order='DESC')
    # print(obj,obj[0],type(obj[0]))
    # obj ---> QuerySet[datetime.date(2018, 4, 1), datetime.date(2017, 4, 1)]
    # obj[0] ---> 2018 - 04 - 01
    # type(obj[0] ---> class 'datetime.date'
    return obj

@register.simple_tag
#分类模板标签
def get_categories():

    # return Category.objects.all()
    return Category.objects.annotate(num_posts=Count('article')).filter(num_posts__gt=0)

@register.simple_tag
def get_archives_num(year,month):
    #我自己加的，显示每月文章数 自定义tag
    archives_num = Article.objects.filter(created_time__year=year,created_time__month=month).count()
    return archives_num
