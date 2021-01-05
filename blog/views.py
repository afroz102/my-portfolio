from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blogs(request):
    blogs = Blog.objects.order_by('-date')[:5]
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})


def details(request, blog_id):
    # Get blog by id or return response 404
    # pk => Primary key(Id of the blog)
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/details.html', {'blog': blog})
