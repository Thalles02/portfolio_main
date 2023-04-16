from django.contrib import admin
from django.urls import path, include
from z_organify_app import *

urlpatterns = [
    path('organify/', include('z_organify_app.urls'))
]
