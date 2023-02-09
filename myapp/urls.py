# myapp/urls.py

# Import django modules
from django.urls import path

# Import from locals
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('products/<int:id>/', views.product_detail, name='product_detail'),
]