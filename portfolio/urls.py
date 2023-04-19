from django.contrib import admin
from django.urls import path, include
from z_organify_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('organify/', include('z_organify_app.urls')),
]