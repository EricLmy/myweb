from django.urls import path 

from . import views 

app_name = 'myblogs'

urlpatterns = [
	path('', views.index, name='index'),
	path('login/', views.login, name="login"),
	path('login/<int:user_id>/', views.writeblog, name="writeblog"),
	path('login/<int:user_id>/save/', views.saveblog, name="saveblog"),
	path('register/register_fun/', views.userregister_fun, name="userregister_fun"),
	path('register/', views.register, name="register"),
	path('<int:blogs_id>/', views.blogsdetail, name="blogsdetail"),
	path('<int:blogs_id>/comment/', views.comment, name="comment"),

]