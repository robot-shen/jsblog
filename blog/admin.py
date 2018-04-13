from django.contrib import admin
from .models import Article,Category,Tag
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']

#todo "admin自定制学习"
admin.site.register(Article,ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)


