from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from blog import models
from django.utils import timezone
from django.contrib.auth.models import User
import pytz
import markdown
from comments.forms import CommentForm


# Create your views here.


def test(request):
    # user = User.objects.create(username='jinshen')
    user = User.objects.get(id=1)
    # c = models.Category.objects.create(name='Linux')
    c = models.Category.objects.get(id=1)

    # p = models.Article(title='title test', body='body test',created_time=timezone.now(), modified_time=timezone.now(),
    #                    category=c, author=user)
    # p.save()
    p = models.Article.objects.filter(id=1).values()[0]
    print(p['created_time'].strftime("%Y-%m-%d %H:%M:%S %Z"))
    return HttpResponse(000)


def index(request):
    article_list = models.Article.objects.all()
    if request.method == "GET":
        return render(
            request,
            "blog/index.html",
            context={'article_list': article_list})
    else:
        return HttpResponse("错误")


def detail(request, pk):
    article = get_object_or_404(models.Article, pk=pk)

    article.increase_views()#阅读量+1

    extensions = ['markdown.extensions.extra',
                  'markdown.extensions.codehilite',
                  'markdown.extensions.toc', ]
    article.body = markdown.markdown(article.body, extensions)
    form = CommentForm()
    # comment_list = models.Article.objects.get(pk=pk).comment_set
    comment_list = article.comment_set.all()
    context = {
        'post': article,
        'form': form,
        'comment_list': comment_list
    }
    return render(request, 'blog/detail.html', context=context)


def archives(request, year, month):
    #归档函数，在页面右侧做链接用
    article_list = models.Article.objects.filter(
        created_time__year=year,
        created_time__month=month)
    return render(request, 'blog/index.html', context={'article_list': article_list})

# def category(request,pk):
#     #分类函数
#     article_list = models.Article.objects.filter(category__id=pk)
#     return render(request, 'blog/index.html', context={'article_list': article_list})

def category(request, pk):
    # 第二种获取方式，引入404界面并且对结果作了排序
    cate = get_object_or_404(models.Category, pk=pk)
    #print(cate,type(cate))#习近平 <class 'blog.models.Category'>
    #根据传入的 pk 值（id 值）从数据库中获取到这个分类，然后根据类对象查找Article
    article_list = models.Article.objects.filter(category=cate)
    #print(article_list,type(article_list))
    #<QuerySet [<Article: 全国货物贸易>, <Article: 南海局势>]> <class 'django.db.models.query.QuerySet'>
    return render(request, 'blog/index.html', context={'article_list': article_list})

def author_article(request,pk):
    article_list = models.Article.objects.filter(author__id=pk)
    return render(request, 'blog/index.html', context={'article_list': article_list})
