from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from blog import models
from django.utils import timezone
from django.contrib.auth.models import User
import pytz

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
    article_list = models.Article.objects.all().order_by('created_time')
    if request.method == "GET":
        return render(request,"blog/index.html",context={'article_list':article_list})
    else:
        return HttpResponse('askluf ')

def detail(request, pk):
    article = get_object_or_404(models.Article, pk=pk)
    return render(request, 'blog/detail.html', context={'article': article})