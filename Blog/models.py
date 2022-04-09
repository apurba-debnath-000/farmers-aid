from django.db import models
from froala_editor.fields import FroalaField
from .helpers import *
from django.utils.html import format_html
# Create your models here.
class BlogCategory(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    def image_tag(self):
        return format_html(
            '<img src="/abcd/show/{}" style="width:40px;height:40px;border-radius:50%;"  />'.format(self.image))

    def __str__(self):
        return self.title


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = FroalaField()
    cat = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to = 'upload/blog/postImg/')
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    
    def save(self , *args, **kwargs): 
        self.slug = generate_slug_post(self.title)
        super(Post, self).save(*args, **kwargs)

    

