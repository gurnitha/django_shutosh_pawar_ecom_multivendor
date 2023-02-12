# myqpp/views.py

# Import django modules
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

# Import from locals
from myapp.models import Product

# Create your views here.

def index(request):
	return HttpResponse("Hi there ...")


# def products(request):
# 	products = Product.objects.all()
# 	context = {
# 		'products':products,
# 	}
# 	return render(request, 'myapp/index.html', context)


# Class based view for the above products view [ListView]
class ProductListView(ListView):
    model = Product
    template_name = 'myapp/index.html'
    context_object_name = 'products'


# def product_detail(request, id):
# 	product = Product.objects.get(id=id)
# 	context = {
# 		'product':product,
# 	}
# 	return render(request, 'myapp/detail.html', context)


# Class Based ListDetailView for the above product_detail
class ProductDetailView(DetailView):
	model = Product
	template_name = 'myapp/detail.html'
	context_object_name = 'product'


@login_required
def add_product(request):
	# 1. Once the form submited,
	#    Get all data (name, price, desc, and image)
	if request.method =='POST':
		name = request.POST.get('name')
		price = request.POST.get('price')
		desc = request.POST.get('desc')
		image = request.FILES['upload']
		seller_name = request.user # the logged in user

		# 2. Pass the data or insert the data to Product table
		#    in the db using django ORM
		product = Product(name=name, price=price, desc=desc, image=image, seller_name=seller_name)
		product.save()	

	return render(request, 'myapp/addproduct.html')


# Class Based View for creating a product
class ProductCreateView(CreateView):
	model = Product
	'''
	About the fields: The fields will authomaticall:
	1. Create instance of form
	2. Looks for a page of product_form.html
	3. product_form.html comes from:
	3.1 product as the name of the model 'Product'
	3.2 form is the insctace of the fields.
	3.3 So, if the model was Category, then --> category_form.html
	'''
	fields = ['name','price','desc','image','seller_name']
	# product_form.html

# def update_product(request, id):
	
# 	# Get an instance of a product
# 	product = Product.objects.get(id=id)

# 	# Get data from the updateproduct form
# 	if request.method == 'POST':
# 		product.name = request.POST.get('name')
# 		product.price = request.POST.get('price')
# 		product.desc = request.POST.get('desc')
# 		product.image = request.FILES['upload']
# 		product.save()

# 		return redirect('/myapp/products')

# 	context = {
# 		'product':product,
# 	}
# 	return render(request, 'myapp/updateproduct.html', context)


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name','price','desc','image','seller_name']
    template_name_suffix = '_update_form'


def delete_product(request, id):
	product = Product.objects.get(id=id)
	if request.method == 'POST':
		product.delete()
		return redirect('/myapp/products')

	context = {
		'product':product,
	}

	return render(request, 'myapp/deleteproduct.html', context)


def my_listings(request):
	products = Product.objects.filter(seller_name=request.user)
	context = {
		'products':products,
	}
	return render(request, 'myapp/mylistings.html', context)