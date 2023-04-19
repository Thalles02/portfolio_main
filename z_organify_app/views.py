from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from z_organify_app.models import *
from django.apps import apps
from django.db import connection
import subprocess


name = 'Thalles Augusto Monteiro Martins'


def home(request):
    return render(request, 'partials/head.html', context={
        'name': name,
    })

def workspaces(request):
    return render(request, 'partials/workspaces.html', context={
        'name': name,
    })

def objects(request):
    return render(request, 'partials/table.html', context={
        'name': name,
    })

def kanban(request):
    return render(request, 'partials/kanban.html', context={
        'name': name,
    })

def create_table(request):

    if request.method == 'POST':
        name_table = request.POST.get('name_table')
        print(name_table)

        with connection.cursor() as cursor:
            #cursor.execute(f"CREATE TABLE {name_table} (id serial PRIMARY KEY, created_at timestamp NOT NULL)")
            cursor.execute('SELECT * from ab')
            command = f"python manage.py inspectdb --table {name_table} > ./z_organify_app/models.py"
            output = subprocess.check_output(command, shell=True)
                        

    return render(request, 'create_table.html')