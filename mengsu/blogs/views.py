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
