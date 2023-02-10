# myqpp/views.py

# Import django modules
from django.shortcuts import render
from django.http import HttpResponse

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
	product = Product.objects.get(id=id)
	# print(product)
	context = {
		'product':product,
	}
	return render(request, 'myapp/updateproduct.html', context)