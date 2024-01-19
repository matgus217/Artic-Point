from django.shortcuts import render


# Create your views here.
def get_index(request):
    return render(request, 'pages/index.html')


def get_menu(request):
    return render(request, 'pages/menu.html')
