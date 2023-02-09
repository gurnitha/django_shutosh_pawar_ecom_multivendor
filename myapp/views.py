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
	return HttpResponse(products)