from django.shortcuts import render, get_object_or_404

from blogs.models import BlogsPost, BlogsComment
# Create your views here.
def index(request):
	blogs_list = BlogsPost.objects.order_by('-timestamp')
	context = {'blogs_list':blogs_list}
	return render(request, 'blogs/index.html', context)

def blogsdetail(request, blogs_id):
	blog = get_object_or_404(BlogsPost, pk=blogs_id)
	try:
		# blogs_comment = blog.objects.get(id=blogs_id)
		# blogs_comment = blog.blogscomment_set.get(pk=blogs_id)
		blogs_comment = blog.blogscomment_set.all()
	except (KeyError, BlogsComment.DoesNotExist) as e:
		return render(request, 'blogs/index.html', {"error": "ERROR"})
	return render(request, 'blogs/blogdetail.html',{"blog":blog, "comment_list":blogs_comment})


def comment(request, blogs_id):
	blog = get_object_or_404(BlogsPost, pk=blogs_id)
	try:#blogs_blogscomment.blog_id
		comment = BlogsComment(blog=blog,comment_text=request.POST['comment'], goods=0, poors=0)
		comment.save()
	except Exception as e:
		return render(request, 'blogs/index.html', {"error": str(e)})
	# blogsdetail(request, blogs_id)
	return render(request, 'blogs/index.html', {"error": "success"})
	# try:
	# 	blogs_comment = question.blogscomment_set.get(pk=blogs_id)
	# except (KeyError, Choice.DoesNotExist):
	# 	return render(request, 'blogs/index.html', {"error": "ERROR"})
	# 	# return render(request, 'polls/detail.html',{'question':question, 'error_message':"You not Choice!!"})
	# else:
	# 	blogs_comment.votes += 1
	# 	blogs_comment.save()
	# 	return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))