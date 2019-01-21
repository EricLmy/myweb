from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from myblogs.models import User, BlogsPost, BlogsComment

def index(request):
	return render(request, 'myblogs/index.html')

def login(request):
	user = get_object_or_404(User, user_name=request.POST['username'])
	if user.user_pass == request.POST['pwd']:

		blogs_list = BlogsPost.objects.filter(user_id=user.id)

		# all_blogs_list = BlogsPost.objects.all()
		# blogs_list = []
		# for user_blog in all_blogs_list:
		# 	if user_blog.user.user_name == request.POST['username']:
		# 		blogs_list.append(user_blog)

		context = {'blogs_list':blogs_list}
		
		return render(request, 'myblogs/login.html', context)
	else:
		return render(request, 'myblogs/error.html', {"error":"密码错误"})


def blogsdetail(request, blogs_id):
	blog = get_object_or_404(BlogsPost, pk=blogs_id)
	try:
		# blogs_comment = blog.blogscomment_set.order_by('-timestamp')
		blogs_comment = blog.blogscomment_set.all()
	except (KeyError, BlogsComment.DoesNotExist) as e:
		return render(request, 'myblogs/error.html', {"error":"404"})

	return render(request, 'myblogs/detail.html', {"blog":blog, "comment_list":blogs_comment})


def comment(request, blogs_id):
	blog = get_object_or_404(BlogsPost, pk=blogs_id)
	try:#blogs_blogscomment.blog_id
		comment = BlogsComment(blog=blog,comment_text=request.POST['comment'], goods=0, poors=0)
		comment.save()
	except Exception as e:
		return render(request, 'myblogs/error.html', {"error": str(e)})

	return HttpResponseRedirect(reverse('myblogs:blogsdetail',args=(blog.id,)))# 重定向