from django import forms
from Post.models import *



class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'text')

class GalleryForm(forms.ModelForm):
	class Meta:
		model = Gallery
		fields = ('url',)