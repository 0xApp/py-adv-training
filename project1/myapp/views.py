from django.shortcuts import render
from .models import Blog
from .forms import BlogForm

def index(request):
	blogs = Blog.objects.all()
	return render(request, 'index.html', {'blogs': blogs})

def add_blog(request):
	form = BlogForm()
	return render(request, 'add-blog.html', {'form': form})
