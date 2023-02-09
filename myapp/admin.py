# myapp/admin.py

# Import django modules
from django.contrib import admin

# Import from locals
from myapp.models import Product 

# Register your models here.

admin.site.register(Product)