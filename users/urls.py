# users/urls.py

# Import django modules
from django.urls import path

# Import from locals
from users import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
]