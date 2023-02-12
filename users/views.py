# users/views.py

# Import django modules
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Import from locals
from users.forms import NewUserForm
from users.models import Profile

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


def create_profile(request):

    # Handling POST request if form submited with data
    if request.method == 'POST':

        # Get the image, contact_number, and user
        image = request.FILES['upload']
        contact_number = request.POST.get('contact_number')
        user = request.user 

        # Create profile objecs and save them to the the Profile table in the db
        profile = Profile(image=image,contact_number=contact_number,user=user)
        profile.save()

    return render(request, 'users/createprofile.html')


def seller_profile(request,id):
    seller = User.objects.get(id=id)
    context = {
        'seller':seller
    }
    return render(request, 'users/selllerprofile.html', context)