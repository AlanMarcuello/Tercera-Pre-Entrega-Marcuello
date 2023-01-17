"""TercerEntrega URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from TercerEntrega import views
#from AppCoder.views import * #Ya no seria necesario :) 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name="Inicio"),
    path('mallas', views.mallas, name="Mallas"),
    path('pijamas', views.pijamas, name="Pijamas"),
    path('ropainterior', views.ropainterior, name="Ropa Interior"),
    path('mallasFormulario', views.mallasFormulario, name="MallasFormulario"),
    path('pijamasFormulario', views.pijamaFormulario, name="PijamasFormulario"),
    path('ropainteriorFormulario', views.ropainteriorFormulario, name="RopaInteriorFormulario"),
    path('buscar/', views.busquedaTalle, name="Buscar"),
    path('resultadoBusqueda/', views.buscar, name="ResultadoBusqueda"),
]
