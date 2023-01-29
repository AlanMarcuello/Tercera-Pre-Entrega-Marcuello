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
from django.contrib.auth.views import LogoutView 


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
    path('login', views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path('logout', LogoutView.as_view(template_name='TercerEntrega/logout.html'), name='Logout'),
    path('eliminarPerfil', views.eliminarusuario, name="EliminarPerfil"),
    path('eliminarMallas/<mall_nombreModelo>/', views.eliminarMallas, name="EliminarMallas"),
    path('eliminarRopa/<ropa_nombreModelo>/', views.eliminarRopainterior, name="EliminarRopaInterior"),
    path('eliminarPijama/<pijam_nombreModelo>/', views.eliminarPijama, name="EliminarPijama"),
    path('editarMallas/<mall_nombreModelo>/', views.editarMallas, name="EditarMallas"),
    path('editarRopainterior/<rop_nombreModelo>/', views.editarRopainterior, name="EditarRopaInterior"),
    path('editarpijamas/<pijam_nombreModelo>/', views.editarPijama, name="EditarPijamas"),
    path('nosotros', views.nosotros, name="Nosotros"),
]
