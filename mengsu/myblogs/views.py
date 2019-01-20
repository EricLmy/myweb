from django.shortcuts import render, get_object_or_404

# Create your views here.
from myblogs.models import User

def index(request):
	return render(request, 'myblogs/index.html')

def login(request):
	print(request.POST['username'])
	print(request.POST['pwd'])
	user_list = User.objects.order_by('-user_time')
	context = {'user_list':user_list}
	uuu = get_object_or_404(User, user_name=request.POST['username'])
	# uuu = User.objects.get(user_name=request.POST['username'])
	print(uuu)
	return render(request, 'myblogs/login.html', context)