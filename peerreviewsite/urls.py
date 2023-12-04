from django.contrib import admin
from django.urls import path, include  # Don't forget to import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reviewApp.urls')),  # Include the urls from your app here
]
