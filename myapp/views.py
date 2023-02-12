# myqpp/views.py

# Import django modules
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Import from locals
from myapp.models import Product

# Create your views here.

def index(request):
	return HttpResponse("Hi there ...")


def products(request):
	products = Product.objects.all()
	context = {
		'products':products,
	}
	return render(request, 'myapp/index.html', context)


def product_detail(request, id):
	product = Product.objects.get(id=id)
	context = {
		'product':product,
	}
	return render(request, 'myapp/detail.html', context)


@login_required
def add_product(request):
	# 1. Once the form submited,
	#    Get all data (name, price, desc, and image)
	if request.method =='POST':
		name = request.POST.get('name')
		price = request.POST.get('price')
		desc = request.POST.get('desc')
		image = request.FILES['upload']

		# 2. Pass the data or insert the data to Product table
		#    in the db using django ORM
		product = Product(name=name, price=price, desc=desc, image=image)
		product.save()	

	return render(request, 'myapp/addproduct.html')


def update_product(request, id):
	
	# Get an instance of a product
	product = Product.objects.get(id=id)

	# Get data from the updateproduct form
	if request.method == 'POST':
		product.name = request.POST.get('name')
		product.price = request.POST.get('price')
		product.desc = request.POST.get('desc')
		product.image = request.FILES['upload']
		product.save()

		return redirect('/myapp/products')

	context = {
		'product':product,
	}
	return render(request, 'myapp/updateproduct.html', context)


def delete_product(request, id):
	product = Product.objects.get(id=id)
	if request.method == 'POST':
		product.delete()
		return redirect('/myapp/products')

	context = {
		'product':product,
	}

	return render(request, 'myapp/deleteproduct.html', context)