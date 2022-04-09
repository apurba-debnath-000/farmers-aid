

from django.urls.conf import path
from django.urls.resolvers import URLPattern
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.homeBlog, name='home_Blog'),
    path('blog-detail/<slug>' , blog_detail , name="blog_detail"),
    path('deatils_comment/' , CommentDetailView.as_view() , name="deatils_comment"),
    
    path('blog-detail/<int:pk>/comment/' , AddCommentView.as_view() , name="add_comment"),

    # path('blog-detail/comment/' , CommentTemplate.as_view() , name="comment"),

    path('category/<slug:url>',category),
    path('detail/<slug:slug>',PostDetail),
    path('showblog/',ShowBlogs, name="show_blogs"),
    path('addblog/',AddBlogView.as_view(), name="add_blog"),
    path('showblog/updateblog/<int:pk>',UpdateBlogView.as_view(), name="update_blog"),
    path('showblog/deleteblog/<int:pk>',DeleteBlogView.as_view(), name="delete_blog"),

    path('blog-detail/deleteComment/<int:pk>',DeleteCommentView.as_view(), name="delete_comment"),

]