from django.db import models

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=255)
    url = models.CharField(max_length=64,blank=True,null=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey("blog.Article")

    def __str__(self):
        return self.text[:20]

