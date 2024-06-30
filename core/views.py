from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/index.html',)

def productos(request):
    return render(request, 'productos/index.html',)

def ofertas(request):
    return render(request, 'ofertas/index.html',)

def contactos(request):
    return render(request, 'contactos/index.html',)

def aboutUS(request):
    return render(request, 'aboutUS/index.html',)

def iniciarSesion(request):
    return render(request, 'iniciarSesion/index.html',)

def registrarse(request):
    return render(request, 'registrarse/index.html',)