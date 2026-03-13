from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def productos(request):
    return render(request, 'productos.html')

def acercade(request):
    return render(request, 'acercade.html')

def contacto(request):
    return render(request, 'contacto.html')