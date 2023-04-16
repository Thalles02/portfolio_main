from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('workspaces/', workspaces),
    path('object/', objects),
    path('kanban/', kanban)
]