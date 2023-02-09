# mysite/urls.py

# Import django modules
from django.contrib import admin
from django.urls import path

# Import from locals
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # myapp
    path('', views.index),
]
