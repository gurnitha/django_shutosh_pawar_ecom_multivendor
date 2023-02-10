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
	return render(request, 'myapp/addproduct.html')