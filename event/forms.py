from django import forms
from django.contrib.auth.models import User
from users.models import *
from event.models import Event



class EventForm(forms.ModelForm):
	class Meta:
		model = Event
		fields = ('title', 'start_date', 'end_date')