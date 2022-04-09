from django.shortcuts import render
from .models import *


def blogHome(request):
    context = {'blogs' : Post.objects.all(),
    'cats': BlogCategory.objects.all(),
    }
    return render(request, 'blog/homeBlog.html', context)



def blog_detail(request , slug):
    context = {}
    try:
        blog_obj = Post.objects.filter(slug = slug).first()
        context['blog_obj'] =  blog_obj
    except Exception as e:
        print(e)
    return render(request , 'blog/blog_detail.html' , context)