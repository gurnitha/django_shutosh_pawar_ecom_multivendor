# myapp/urls.py

# Import django modules
from django.urls import path

# Import from locals
from myapp import views

urlpatterns = [
    path('myapp/', views.index, name='index'),
]