#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/13 16:26
# @Author  : JinShen
# @File    : blog_tags.py
# @Software: PyCharm
# @Site    :

from ..models import Article,Category
from django import template

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
    return Article.objects.dates('created_time','month',order='DESC')

@register.simple_tag
#分类模板标签
def get_categories():
    return Category.objects.all()

