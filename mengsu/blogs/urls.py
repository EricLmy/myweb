from django.urls import path 

from . import views 

app_name = 'blogs'

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:blogs_id>/', views.blogsdetail, name="blogsdetail"),
	path('<int:blogs_id>/comment/', views.comment, name="comment"),

]