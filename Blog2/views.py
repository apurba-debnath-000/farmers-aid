from django.contrib.auth.decorators import login_required, permission_required
from django.db.models.query import QuerySet
from django.urls.base import reverse
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from Blog2.models import Comment, Post, BlogCategory
from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .form import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin

#@login_required(login_url="/login/")
def homeBlog(request):
    blogs = Post.objects.all()
    cats = BlogCategory.objects.all()

    paginator = Paginator(blogs, 4)
    page_number = request.GET.get('page')
    blogs = paginator.get_page(page_number)
    
    context = {
        "blogs":blogs,
        'cats':cats 
    
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


def category(request, url):
    cat = BlogCategory.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    return render(request, "blog/category.html", {'cat': cat, 'posts': posts})

def PostDetail(request, slug):
    cats = BlogCategory.objects.all()
    post = Post.objects.get(slug=slug)
    return render(request, "blog/postdetail.html", {'post': post, 'cats':cats})


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/add_comment.html'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('show_blogs')
    #success_url = reverse_lazy('deatils_comment')
    # def get_absolute_url(self):
    #     return reverse('add_comment', args=[str(self.id =='pk')] )
    #fields = '__all__'

class CommentDetailView(DetailView):
    queryset = Comment.objects.all()
    template_name = 'blog/add_comment.html'



def ShowBlogs(request):
   blogs = Post.objects.all()
   context = {
       "blogs":blogs
   }
   return render(request, 'blog/show_blog.html', context)


class AddBlogView(CreateView):
    # raise_exception = False

    # permission_required = 'Blog2.add_Post'
    # permission_denied_message=''
    # login_url = '/login/'
    # redirect_field_name = 'next'
    model = Post
    form_class = AddBlogForm
    template_name = "blog/add_blog.html"
    #fields = '__all__'

    success_url = reverse_lazy('show_blogs')


class UpdateBlogView(UpdateView):
    model = Post
    form_class = UpdateBlogForm
    template_name = "blog/edit_blog.html"
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('show_blogs')

class DeleteBlogView(DeleteView):
    model = Post
    template_name = 'blog/delete_confirm.html'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('show_blogs')

# class CommentTemplate(ListView):
#     template_name = 'blog/add_comment.html'
#     model = Comment
#     queryset = Comment.objects.all()


class DeleteCommentView(DeleteView):
    model = Comment
    template_name = 'blog/confirm_delete_comment.html'
    def form_valid(self, form):
        form.instance.comment_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('show_blogs')