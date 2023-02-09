# mysite/urls.py

# Import django modules
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    # myapp
    path('myapp/', include('myapp.urls')),
]
