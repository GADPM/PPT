# PPT/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('PPT_app.urls')),  # Redireciona a raiz para as URLs do PPT_app
]
