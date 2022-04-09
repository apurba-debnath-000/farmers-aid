from django.contrib import admin
from .models import *

class BlogCategoryAdmin(admin.ModelAdmin):
    list_display= ('image_tag', 'title', 'description','add_date', 'url')
    search_fields=('title',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 50
    
    # class Media:
    #     js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js', 'js/script.js',)

admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
