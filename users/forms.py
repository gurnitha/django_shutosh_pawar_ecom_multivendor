# users/forms.py

# Import django modules
from django.contrib.auth.forms Import UserCreationForm
from django.contrib.auth.models import User 
from django import forms  


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	username = forms.CharField(required=True)
	password1 = forms.CharField(required=True)
	password2 = forms.CharField(required=True)

	class Meta:
		model = User 
		fields = ('email','username','password1','password2')