from django.contrib import admin

# Register your models here.
from .models import User, BlogsComment, BlogsPost

class BlogsPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'timestamp']


admin.site.register(User)
admin.site.register(BlogsPost, BlogsPostAdmin)
admin.site.register(BlogsComment)