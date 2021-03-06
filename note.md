# 博客实战记录
管理员：jinshen
pwd：jinshen123
## 环境配置
#### 安装virtualenv
参考链接：[windows下搭建virtualenv、virtualenvwrapper虚拟环境](https://blog.csdn.net/shaququ/article/details/54292043)
> python3 -m pip install virtualenv

#### 安装virtualenvwrapper
* 命令行安装
> python3 -m pip install virtualenvwrapper-win

* 设置WORK_HOME环境变量
> 在win环境变量里，新建一个变量：
变量名：WORK_HOME
变量值：C:\Py_Vir_Env（以后虚拟环境存放的路径）

![Alt text](https://imghosting-1256211031.cos.ap-beijing.myqcloud.com/note/jsblog01.png
 "不要设错了")

#### 检测及Django安装
* 进入cmd
> mkvirtualenv forblog
这样名为forblog的虚拟环境就建立好了
文件夹在C:\Py_Vir_Env

*  查看安装的所有虚拟环境
> workon

* 进入虚拟环境
> workon forblog

* 查看虚拟环境的pip包
> pip list

* 安装Django
> pip install django==1.10.6 -i https://pypi.tuna.tsinghua.edu.cn/simple

* 退出虚拟环境
> deactivate

## pycharm操作
1. 新建Django工程
2. 配置虚拟环境应用
3. 在Terminal里边验证是不是虚拟环境
>(forblog) D:\BaiduYunDownload\Learn\jsblog>
4. 把项目依赖文件放到工程目录
5. 安装依赖
> pip install -r requirements.txt

## 配置GitHub
为了防止使用git时给自己挖坑，建议初始化项目时：
1. 先建立远程仓库，然后clone到本地，再进行其他操作
2. 如果先建立本地仓库，后建立远程仓库，确保远程库为空，这样push的时候不会有冲突文件
3. 有了冲突文件，就要解决冲突。先把远程pull过来，然后合并解决冲突，再push

在default setting里边 >>> 版本控制 >>> Git
Path to Git:选择git.exe路径
SSH exeutable：选Native，其他默认即可
注意：选Native是应用本地git bash已经设置好的ssh
选built-in则是使用内建的ssh，这个内建是需要你输入name email，pycharm替你生成的

还是Native灵活性比较高，依赖git.exe的git软件都可以用

## 迁移数据库



* 最开始makemigrations时，有如下报错：

应该是Django没能识别出我引用的User模块导致

```
ERRORS:
blog.Article.author: (fields.E300) Field defines a relation with model 'User', which is either not installed, or is abstract.

blog.Article.author: (fields.E307) The field blog.Article.author was declared with a lazy reference to 'blog.user', but app 'blog' doesn't provide model 'user'.
```
* 知识点：关于Fornkey参数值on-delete

> [on-delete参数详解](https://blog.csdn.net/kuangshp128/article/details/78946316)

* 时区转换
> [链接](http://www.jb51.net/article/90802.htm)
在Django的配置文件settings.py中，有两个配置参数是跟时间与时区有关的，分别是TIME_ZONE和USE_TZ

USE_TZ = True，开启Django的时区功能  
当 USE_TZ  为 True  时，在过滤之前，datetime字段将转换为当前时区  
【Django1.8_Cn p906】  
Django 第一次发布时， TIME_ZONE  设置为  'America/Chicago' ,所以默认时间全是它
Django 设置 os.environ['TZ']  变量为你在 TIME_ZONE  设置中指定的时区。   
所以，你的所有视图和模型都将自动在这个时区中运作   

 * [django时区相关链接](https://blog.csdn.net/w6299702/article/details/38782607)  
>建议处理方式：  
>>后端处理的时候统一用UTC时间，忽略本地时间的存在  
模板处理时会自动使用settings.TIME_ZONE帮我们转换  

**django 处理时区需要依赖 pytz 这个模块**

## Django admin使用
### 配置admin
```
from django.contrib import admin
from .models import Post, Category, Tag

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Tag)
```
*在这又遇到Django谎报军情 说是Article已注册过，重启就好了*

* 可以使用以下三个库中的其中一个美化django-admin

1、[star 1426 ](https://github.com/django-admin-bootstrapped/django-admin-bootstrapped)
2、[star 1507 ](https://github.com/darklow/django-suit)
3、[star 2321 ](https://github.com/sehmaschine/django-grappelli)
### admin初步自定制
在admin.py里，写如下内容
``` python
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']

admin.site.register(Article,ArticleAdmin)
```

## 博客详情页
* 关于url的知识点

**url的几个参数，正则，分组**
url(regex, view, kwargs=None, name=None)
```
urlpatterns = [
    url(正则表达式1, views视图函数1，参数1，别名1),
    url(正则表达式2, views视图函数2，参数2，别名2),
]
```

* URL的无命名分组：分组直接指向函数的参数值
*url(r'^articles/([0-9]{4})/$', views.year_archive)*

* URL的有命名分组，Named groups 可以做分组的同时捎带着起个名
*'(?P<id>\d{3})/(?P<name>\w{3})'   >>>   'weeew34ttt123/ooo'*

### blog/url.py中
```
app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^article/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
]
```

**app_name='blog' 告诉 Django 这个 urls.py 模块是属于 blog 应用的，这种技术叫做视图函数命名空间**
*url(r'^article/(?P<pk>[0-9]+)/$',views.detail,name='detail')*
例如 /article/3/  请求将调用函数 views.detail(request, pk='3')

* url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.archives,name='archives'),*
在HTML应用：  
方法一：href="archives/{{ date.year }}/{{ date.month }}"
方法二：href="{% url 'blog:archives' date.year date.month %}"  **推荐**

**注意：**
1. 此处P为大写，固定用法
2. 捕获的参数永远是字符串
3. 若要从URL 中捕获一个值，只需要在它周围放置一对圆括号。
4. 不需要添加一个前导的反斜杠，因为每个URL 都有。例如，应该是 ^articles  而不是  ^/articles  。
5. 起别名的目的是在渲染时url能反向解析：
>是为了让action中的{% url "detail" %}可以顺利的被替换（渲染）成url绑定好的内容  
这样浏览器就能接收到渲染好的代码，直接读出 action:/"article/3/"  
以保证form表单能提交到正确的路径（即该url绑定的那个函数内）  

* from django.urls import reverse

### 支持markdown
```python
extensions = ['markdown.extensions.extra',
              'markdown.extensions.codehilite',
              'markdown.extensions.toc',]
article.body = markdown.markdown(article.body,extensions)
```
> extra 包含好几个扩展  
> codehilite 实现语法高亮，内部依赖 **Pygments** 模块（需要提前安装好）  
> toc 允许我们自己生成目录

## 页面侧边栏
### 模板回顾
```djangotemplate
{% load staticfiles %}  # 加载标签库

 {% static %} 模板标签，这个标签帮助我们在模板中引入静态文件  
 <link rel="stylesheet" href="{% static 'blog/css/pace.css' %}">
 
 <form action="{% url "bieming"%}" >
          <input type="text">
          <input type="submit"value="提交">
          {%csrf_token%}
</form>

{% with hehe='英俊潇洒风流倜傥玉树临风' %} {{ hehe }} {% endwith %}

{% verbatim %}  # 禁止render
         {{ hello }}
{% endverbatim %}
```
### 自定义tag
* a、在app中创建templatetags模块(必须的)  
* b、创建任意 .py 文件，如：my_tags.py  
* c、在使用自定义simple_tag和filter的html文件中  
导入之前创建的 my_tags.py ：{% load my_tags %}  # 首行  
* d、使用simple_tag和filter（如何调用）  
**自定义filter:** {{ num|filter_multi:2 }}   
**自定义tag:** {% simple_tag_multi num 5 %}

注：*filter可以用在if等语句后，simple_tag不可以*

obj = Article.objects.dates('created_time', 'month', order='DESC')  
注：obj的值是QuerySet。本质上是个集合，自带去重功能。所以得到的结果是各个月份  







# 笔记：
* a标签的用法
## href="URL"的作用
```html
<a href="http://baidu.com">超链接</a>  
<a href="#line22">回到最顶端</a> 锚
<a href="#">回到最顶端</a>  可以利用这个特性制作右下角的返回顶部按钮
<a href="css/css1.css">文件链接</a>  
```
**注意：**
```html
<a href="index.html">首页</a>
这种写法，二次点击的时候会指向http://127.0.0.1:8000/index.html/index.html
一定要加上// → <a href="/index.html/">首页</a>
```
## js相关
```JavaScript
<a href="javascript:;" onclick="js_method()"></a>  
执行空js代码，且绑定js_method

a href="javascript:void(0);" onclick="js_method()"
void是一个操作符，void(0)返回undefined，地址不发生跳转，同时绑定js_method

<a href="#" onclick="js_method();return false;"></a>  
这种方法点击执行了js函数后return false，页面不发生跳转，执行后还是在页面的当前位置。
```


 

 

