from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from TercerEntrega.models import Mallas
from TercerEntrega.models import Pijamas
from TercerEntrega.models import RopaInterior
from TercerEntrega import *

# Create your views here.

def inicio(request):

      return render(request, "TercerEntrega/inicio.html")

def mallas(request):
      mall = Mallas.objects.all() #trae todos las mallas
      contexto= {"mall":mall} 
      return render(request, "TercerEntrega/mallas.html",contexto)

def pijamas(request):

      pijam = Pijamas.objects.all() #trae todos los pijamas
      contexto= {"pijam":pijam} 
      return render(request, "TercerEntrega/pijamas.html",contexto)


def ropainterior(request):
      rop = RopaInterior.objects.all() #trae toda la ropa interior
      contexto = {"rop":rop}
      return render(request, "TercerEntrega/ropainterior.html",contexto)


from TercerEntrega.forms import MallasFormulario

def mallasFormulario(request):

      if request.method == "POST":

            miFormulario = MallasFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  malla = Mallas(nombreModelo=informacion["nombreModelo"], info=informacion["info"], talles=informacion["talles"], colores=informacion["colores"])
                  malla.save()
                  return render(request, "TercerEntrega/inicio.html")
      else:
            miFormulario = MallasFormulario()

      return render(request, "TercerEntrega/mallasFormulario.html", {"miFormulario": miFormulario})

from TercerEntrega.forms import RopaInteriorFormulario

def ropainteriorFormulario(request):

      if request.method == "POST":

            miFormulario = RopaInteriorFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  ropa = RopaInterior(nombreModelo=informacion["nombreModelo"], info=informacion["info"], talles=informacion["talles"], colores=informacion["colores"])
                  ropa.save()
                  return render(request, "TercerEntrega/inicio.html")
      else:
            miFormulario = RopaInteriorFormulario()

      return render(request, "TercerEntrega/ropainteriorFormulario.html", {"miFormulario": miFormulario})


from TercerEntrega.forms import PijamasFormulario

def pijamaFormulario(request):

      if request.method == "POST":

            miFormulario = PijamasFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  pijama = Pijamas(nombreModelo=informacion["nombreModelo"], inviernoverano=informacion["inviernoverano"], talles=informacion["talles"], Colores=informacion["colores"])
                  pijama.save()
                  return render(request, "TercerEntrega/inicio.html")
      else:
            miFormulario = PijamasFormulario()

      return render(request, "TercerEntrega/pijamasFormulario.html", {"miFormulario": miFormulario})


def busquedaTalle(request):
      return render(request, "TercerEntrega/busquedaTalles.html")

def buscar(request):
      if request.GET["info"]:
            
            info = request.GET['info']
            malla = Mallas.objects.filter(info__contains=info)
      
            return render(request, "TercerEntrega/resultadoBusqueda.html", {"malla":malla, "info": info})
      else:
            respuesta = "No enviaste datos"
            return HttpResponse(respuesta)
