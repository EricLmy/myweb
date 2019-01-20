from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=20)
    user_pass = models.CharField(max_length=20)
    user_mail = models.EmailField(max_length=64)
    user_time = models.DateTimeField('date')

    def __str__(self):
        return self.user_name

class BlogsPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 150)  # 博客标题
    body = models.TextField()                   # 博客正文
    timestamp = models.DateTimeField()          # 创建时间

    def __str__(self):
        return self.title

class BlogsComment(models.Model):
    blog = models.ForeignKey(BlogsPost, on_delete=models.CASCADE)
    comment_text = models.TextField() 
    goods = models.IntegerField(default=0)
    poors = models.IntegerField(default=0)

    def __str__(self):
        return self.comment_text
