from django.urls import path
from z_organify_app.views import *

urlpatterns = [
    path('', home),
    path('workspaces/', workspaces),
    path('object/', objects),
    path('kanban/', kanban),
    path('addtable/', create_table),
]