from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('calc.urls')),  # Changed from url() to path()
    path('admin/', admin.site.urls),
]
