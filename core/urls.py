from django.urls import path
from .views import aboutUS,contactos,home,iniciarSesion,productos,registrarse,ofertas

urlpatterns = [
    path('', home,name="home"),
    path('productos', productos, name="productos"),
    path('contactos', contactos, name="contactos"),
    path('ofertas', ofertas, name="ofertas"),
    path('aboutUS', aboutUS, name="aboutUS"),
    path('iniciarSesion', iniciarSesion, name="iniciarSesion"),
    path('registrarse', registrarse, name="registrarse"),
]