from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

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