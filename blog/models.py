from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    # 文章分类
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)  # 建立时间
    modified_time = models.DateTimeField(auto_now=True)  # 最后一次编辑时间
    excerpt = models.CharField(max_length=200, blank=True)  # 摘要
    category = models.ForeignKey("Category")
    tags = models.ManyToManyField("Tag", blank=True)
    author = models.ForeignKey(User)

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    def get_absolute_url(self):
        #todo:没用过这个reverse函数
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
