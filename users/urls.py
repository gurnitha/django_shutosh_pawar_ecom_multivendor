# users/urls.py

# Import django modules
from django.urls import path
from django.contrib.auth import views as authentication_view

# Import from locals
from users import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', authentication_view.LoginView.as_view(template_name='users/login.html'), name='login'),
]
