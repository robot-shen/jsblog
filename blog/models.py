from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class User(AbstractUser):
#     """
#     Users within the Django authentication system are represented by this
#     model.
#
#     Username, password and email are required. Other fields are optional.
#     """
#     class Meta(AbstractUser.Meta):
#         swappable = 'AUTH_USER_MODEL'

class Category(models.Model):
    #文章分类
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()#最后一次编辑时间
    excerpt = models.CharField(max_length=200, blank=True)#摘要
    category = models.ForeignKey("Category")
    tags = models.ManyToManyField("Tag",blank=True)
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title


