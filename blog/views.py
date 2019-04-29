from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.
# Post.objects.get(pk=pk)

def post_list(request):
	posts= Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(render, pk):
	post=get_object_or_404(Post,pk=pk)
	return render(request, 'blog/post_detail.html',{'post':post})

def index(request):
	return render(request, 'blog/index.html', {})
	

# def post_list(request):
# 	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'blog/post_list.html', {'post' :posts})