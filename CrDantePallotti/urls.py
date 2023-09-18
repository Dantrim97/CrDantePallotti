from django.contrib import admin
from django.urls import path, include
from Appcoder.views import cliente


urlpatterns = [
    path('admin/',admin.site.urls),
    path('app-coder/', include('Appcoder.urls')),
    ]