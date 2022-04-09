from django import forms
from django.db import models
from django.forms import fields, widgets
from .models import *
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ( "name", "body" )

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),

        }
class AddBlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ( "title", "content", "cat" , "slug","image")

        widgets = {

            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'cat': forms.Select(attrs={'class':'regDropDown'}),
            'slug': forms.TextInput(attrs={'class':'form-control'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),

        }




class UpdateBlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ( "title", "content", "cat" , "slug","image")

        widgets = {

            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'cat': forms.Select(attrs={'class':'regDropDown'}),
            'slug': forms.TextInput(attrs={'class':'form-control'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),

        }