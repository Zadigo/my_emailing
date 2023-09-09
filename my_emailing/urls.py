from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/campaigns', include('campaigns.api.urls')),
    path('admin/', admin.site.urls),
]
