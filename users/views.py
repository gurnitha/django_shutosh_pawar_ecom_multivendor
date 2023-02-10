# users/views.py

# Import django modules
from django.shortcuts import render

# Import from locals
from users.forms import NewUserForm

# Create your views here.

def register(request):
	# Load the NewUserForm and get its instances
	form = NewUserForm()
	context = {
		'form':form,
	}

	return render(request, 'users/register.html', context)