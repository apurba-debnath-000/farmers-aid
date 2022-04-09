
from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
    
    path('home/', views.blogHome, name='blogHome'),
    path('blog-detail/<slug>' , blog_detail , name="blog_detail"),
    

]
