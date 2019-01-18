from django.db import models

# Create your models here.
class BlogsPost(models.Model):
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
