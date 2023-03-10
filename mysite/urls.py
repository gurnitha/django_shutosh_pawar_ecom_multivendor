# mysite/urls.py

# Import django modules
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # myapp
    path('myapp/', include('myapp.urls')),


    # users
    path('users/', include('users.urls')),

]

urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
