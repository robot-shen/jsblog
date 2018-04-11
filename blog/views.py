from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from blog import models
from django.utils import timezone
from django.contrib.auth.models import User
import pytz

# Create your views here.


def test(request):
    user = User.objects.get(id=1)
    c = models.Category.objects.get(id=1)

    # p = models.Article(title='title test', body='body test',created_time=timezone.now(), modified_time=timezone.now(),
    #                    category=c, author=user)
    p = models.Article.objects.filter(id=1).values()[0]
    print(p['created_time'].strftime("%Y-%m-%d %H:%M:%S %Z"))
    return HttpResponse(000)