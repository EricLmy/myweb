from django.urls import path 

from . import views 

app_name = 'myblogs'

urlpatterns = [
	path('', views.index, name='index'),
	path('login/', views.login, name="login"),
	path('<int:blogs_id>/', views.blogsdetail, name="blogsdetail"),
	path('<int:blogs_id>/comment/', views.comment, name="comment"),

]