from django.urls import path 

from . import views 

app_name = 'usermanage'

urlpatterns = [
	path('', views.userregister, name='userregister'),
	path('register/', views.userregister_fun, name='userregister_fun'),
]