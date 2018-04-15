#Author:Jin_shen
# _*_ coding:utf-8 _*_
#@Time  :2018/4/15 0015下午 10:05
#@Name  :urls.py
#@Software:PyCharm
from django.conf.urls import url
from comments import views

app_name = 'comments'
urlpatterns = [
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$',views.post_comment, name='post_comment'),
]

