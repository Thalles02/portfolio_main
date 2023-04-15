from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

name = 'Thalles Augusto Monteiro Martins'


def home(request):
    return render(request, 'organify/partials/head.html', context={
        'name': name,
    })

def workspaces(request):
    return render(request, 'organify/partials/workspaces.html', context={
        'name': name,
    })

def objects(request):
    return render(request, 'organify/partials/table.html', context={
        'name': name,
    })
