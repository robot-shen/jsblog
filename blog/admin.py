from django.contrib import admin
from .models import Article,Category,Tag
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
    # readonly_fields = ('created_time', 'modified_time',)
    #auto_now和auto_now_add被设置为True后，这样做会导致字段成为editable=False和blank=True的状态
    #想要在admin中看到时间，需引入readonly_fields（只读）

#todo "admin自定制学习"
#后台时间选择插件http://www.nanerbang.com/article/5488/
admin.site.register(Article,ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)


