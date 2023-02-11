# users/views.py

# Import django modules
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Import from locals
from users.forms import NewUserForm

# Create your views here.

def register(request):
	# Handling POST request
    if request.method =='POST':
    	# Get and put all sent data from the NewUserForm to form variable
        form = NewUserForm(request.POST)
        # Make sure data, espesially email is valid
        if form.is_valid():
        	# If data (email) is valid call save_user_data method from within the NewUserForm class
            # user = form.save() # the tutor
            user = form.save_user_data() # ing
            # Redirect to products page
            return redirect('/myapp/products')
    
    # Handling GET request
    form = NewUserForm()

    context={
        'form':form,
    }

    return render(request,'users/register.html',context)


@login_required
def profile(request):
    return render(request, 'users/profile.html')