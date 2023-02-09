# myqpp/views.py

# Import django modules
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("Hi there ...")


def products(request):
	products = ["iphone", "imac", "ipad"]
	return HttpResponse(products)