#Author:Jin_shen
# _*_ coding:utf-8 _*_
#@Time  :2018/4/15 0015下午 9:09
#@Name  :forms.py
#@Software:PyCharm
from django import forms
from .models import Comment



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','url','text']





