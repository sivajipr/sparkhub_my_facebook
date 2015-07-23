from django import forms
from django.contrib.auth.models import User
from users.models import *
class RegisterForm(forms.Form):
	username = forms.CharField(max_length=200, label='Your name')
	first_name = forms.CharField(max_length=30)
	last_name = forms.CharField(max_length=30)
 	email = forms.EmailField(max_length=200, label='Email id')
 	password1 = forms.CharField(widget=forms.PasswordInput, max_length=50, label='Password')
 	password2 = forms.CharField(widget=forms.PasswordInput, max_length=50, label='Re-enter your password')


class EditUserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name','last_name','email')

 	def clean_username(self):
 		try:
 			user = User.objects.get(username__iexact=self.cleaned_data['username'])
 		except User.DoesNotExist:
 			return self.cleaned_data['username']
 		raise forms.ValidationError('The user already exists')

 	def clean(self):
 		if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
 			if self.cleaned_data['password1'] != self.cleaned_data['password2']:
 				raise forms.ValidationError('passwords does not match')
 			else:
 				return self.cleaned_data

class ProfileForm(forms.ModelForm):
	class Meta:
		model=Profile
		exclude = ['user']
class UserImageForm(forms.ModelForm):
	class Meta:
		model=UserImage
		# fields=('profile_pic', 'cover_pic', 'is_active_profile', 'is_active_cover')
		exclude = ['user']
