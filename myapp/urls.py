# myapp/urls.py

# Import django modules
from django.urls import path

# Import from locals
from myapp import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    # path('products/', views.products, name='products'),
    path('products/', views.ProductListView.as_view(), name='products'), # GCBV

    # path('products/<int:id>/', views.product_detail, name='product_detail'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),

    # path('products/add/',views.add_product, name='add_product'),
    path('products/add/',views.ProductCreateView.as_view(), name='add_product'),
    
    # path('products/update/<int:id>/',views.update_product ,name='update_product'),
    path('products/update/<int:pk>/',views.ProductUpdateView.as_view() ,name='update_product'),

    path('products/delete/<int:id>/',views.delete_product ,name='delete_product'),
    path('products/mylistings/', views.my_listings, name='mylistings')
]