from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

name = 'Thalles Augusto Monteiro Martins'


def home(request):
    return render(request, 'organify/partials/head.html', context={
        'name': name,
    })
