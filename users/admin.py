# users/admin.py

# Import django modules
from django.contrib import admin

# Import from locals
from users.models import Profile

# Register your models here.

admin.site.register(Profile)
