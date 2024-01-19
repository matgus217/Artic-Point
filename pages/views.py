from django.shortcuts import render
from django.views import generic
from django.shortcuts import render


# Create your views here.


def get_index(request):
    return render(request, 'pages/index.html')


def get_menu(request):
    return render(request, 'pages/menu.html')


def get_about(request):
    return render(request, 'pages/about.html')


def get_book(request):
    return render(request, 'pages/book.html')
