from django.shortcuts import render

from usermanage.models import  User, Manager
# Create your views here.

def userregister(request):
	manager_list = Manager.objects.order_by('-user_time')
	# print(manager_list)
	context = {'manager_list':manager_list}
	return render(request, 'user/register.html', context)

def userregister_fun(request):
	# print(request.POST['username'])
	# print(request.POST['pwd'])
	# print(request.POST['datetime'])
	try:
		user = User(user_name=request.POST['username'], user_pass=request.POST['pwd'],user_time=request.POST['datetime'])
		user.save()
		return render(request, 'user/register.html', {'register_ok':"register success"})
	except Exception as e:
		return render(request, 'user/register.html', {'register_ok':str(e)})