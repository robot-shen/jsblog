from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from time import timezone
from datetime import datetime

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
    title = models.CharField(max_length=100,verbose_name='文章标题')
    body = models.TextField()
    # created_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')  # 建立时间
    created_time = models.DateTimeField('创建时间',default =datetime.now() )  # 建立时间

    # modified_time = models.DateTimeField(auto_now=True,verbose_name='修改时间')  # 最后一次编辑时间
    modified_time = models.DateTimeField('修改时间',default =datetime.now())  # 最后一次编辑时间
    excerpt = models.CharField(max_length=200, blank=True)  # 摘要
    category = models.ForeignKey("Category",verbose_name='分类')
    tags = models.ManyToManyField("Tag", blank=True)
    author = models.ForeignKey(User,verbose_name='作者')
    views = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def get_absolute_url(self):
        #todo:没用过这个reverse函数
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def save(self,*args,**kwargs):
        '''通过重写save方法，达到自动生成摘要的目的'''
        if not self.excerpt:
            self.excerpt = self.body[:80]

        super(Article,self).save(*args,**kwargs)


    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     # 如果没有填写摘要
    #     if not self.excerpt:
    #         # 首先实例化一个 Markdown 类，用于渲染 body 的文本
    #         md = markdown.Markdown(extensions=[
    #             'markdown.extensions.extra',
    #             'markdown.extensions.codehilite',
    #         ])
    #         # 先将 Markdown 文本渲染成 HTML 文本
    #         # strip_tags 去掉 HTML 文本的全部 HTML 标签
    #         # 从文本摘取前 54 个字符赋给 excerpt
    #         self.excerpt = strip_tags(md.convert(self.body))[:54]
    #
    #     # 调用父类的 save 方法将数据保存到数据库中
    #     # super(Post, self).save(*args, **kwargs)
