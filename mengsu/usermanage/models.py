from django.db import models

# Create your models here.
class Manager(models.Model): # 管理员
    user_name = models.CharField(max_length=20)
    user_pass = models.CharField(max_length=20)
    user_time = models.DateTimeField('date')

    def __str__(self):
        return self.user_name

class User(models.Model): # 用户
    user_father = models.ForeignKey(Manager, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=20)
    user_pass = models.CharField(max_length=20)
    user_time = models.DateTimeField('date')

    def __str__(self):
        return self.user_name

class Tourist(models.Model): # 游客   
    user_father = models.ForeignKey(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=20)
    user_time = models.DateTimeField('date')

    def __str__(self):
        return self.user_name




