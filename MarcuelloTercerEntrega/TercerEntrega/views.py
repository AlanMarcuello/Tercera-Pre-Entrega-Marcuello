from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from TercerEntrega.models import Mallas
from TercerEntrega.models import Pijamas
from TercerEntrega.models import RopaInterior



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

def nosotros(request):

      return render(request, "TercerEntrega/nosotros.html")


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

def eliminarMallas(request, mall_nombreModelo):
      mall = Mallas.objects.get(nombreModelo=mall_nombreModelo)
      mall.delete()
      # vuelvo al menú
      mall = Mallas.objects.all() #trae todos las mallas
      contexto= {"mall":mall} 
      return render(request, "TercerEntrega/mallas.html",contexto)

def editarMallas(request, mall_nombreModelo):
    # Recibe el nombre del profesor que vamos a modificar
    mall = Mallas.objects.get(nombreModelo=mall_nombreModelo)
    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':
        # aquí mellega toda la información del html
        miFormulario = MallasFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            mall.nombreModelo = informacion['nombreModelo']
            mall.info = informacion['info']
            mall.talles = informacion['talles']
            mall.colores = informacion['colores']

            mall.save()

            # Vuelvo al inicio o a donde quieran
            mall = Mallas.objects.all() #trae todos las mallas
            contexto= {"mall":mall} 
            return render(request, "TercerEntrega/mallas.html",contexto)
           
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = MallasFormulario(initial={'nombreModelo': mall.nombreModelo, 'info': mall.info,
                                                   'talles': mall.talles, 'colores': mall.colores})

    # Voy al html que me permite editar
    return render(request, "TercerEntrega/editarMallas.html", {"miFormulario": miFormulario, "mall_nombreModelo": mall_nombreModelo})


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

def eliminarRopainterior(request, ropa_nombreModelo):
      ropa = RopaInterior.objects.get(nombreModelo=ropa_nombreModelo)
      ropa.delete()
      # vuelvo al menú
      rop = RopaInterior.objects.all() #trae toda la ropa interior
      contexto = {"rop":rop}
      return render(request, "TercerEntrega/ropainterior.html",contexto)

def editarRopainterior(request, rop_nombreModelo):
    # Recibe el nombre del profesor que vamos a modificar
    rop = RopaInterior.objects.get(nombreModelo=rop_nombreModelo)
    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':
        # aquí mellega toda la información del html
        miFormulario = RopaInteriorFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            rop.nombreModelo = informacion['nombreModelo']
            rop.info = informacion['info']
            rop.talles = informacion['talles']
            rop.colores = informacion['colores']

            rop.save()

            # Vuelvo al inicio o a donde quieran
            rop = RopaInterior.objects.all() #trae toda la ropa interior
            contexto = {"rop":rop}
            return render(request, "TercerEntrega/ropainterior.html",contexto)
           
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = RopaInteriorFormulario(initial={'nombreModelo': rop.nombreModelo, 'info': rop.info,
                                                   'talles': rop.talles, 'colores': rop.colores})

    # Voy al html que me permite editar
    return render(request, "TercerEntrega/editarRopainterior.html", {"miFormulario": miFormulario, "rop_nombreModelo": rop_nombreModelo})

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

def eliminarPijama(request, pijam_nombreModelo):
      pijam = Pijamas.objects.get(nombreModelo=pijam_nombreModelo)
      pijam.delete()
      # vuelvo al menú
      pijam = Pijamas.objects.all() #trae todos los pijamas
      contexto= {"pijam":pijam} 
      return render(request, "TercerEntrega/pijamas.html",contexto)


def editarPijama(request, pijam_nombreModelo):
    # Recibe el nombre del profesor que vamos a modificar
    pijam = Pijamas.objects.get(nombreModelo=pijam_nombreModelo)
    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':
        # aquí mellega toda la información del html
        miFormulario = PijamasFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            pijam.nombreModelo = informacion['nombreModelo']
            pijam.inviernoverano = informacion['inviernoverano']
            pijam.talles = informacion['talles']
            pijam.Colores = informacion['colores']

            pijam.save()

            # Vuelvo al inicio o a donde quieran
            pijam = Pijamas.objects.all() #trae todos los pijamas
            contexto= {"pijam":pijam} 
            return render(request, "TercerEntrega/pijamas.html",contexto)
           
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = PijamasFormulario(initial={'nombreModelo': pijam.nombreModelo, 'inviernoverano': pijam.inviernoverano,
                                                   'talles': pijam.talles, 'Colores': pijam.Colores})

    # Voy al html que me permite editar
    return render(request, "TercerEntrega/editarPijama.html", {"miFormulario": miFormulario, "pijam_nombreModelo": pijam_nombreModelo})







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


#Para el login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "TercerEntrega/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "TercerEntrega/inicio.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "TercerEntrega/inicio.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "TercerEntrega/login.html", {"form": form})



#Para que los usuarios se puedan registar
from TercerEntrega.forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"TercerEntrega/inicio.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"TercerEntrega/registro.html" ,  {"form":form})


#mixin
from django.contrib.auth.decorators import login_required

@login_required
def inicio(request):

    return render(request, "TercerEntrega/inicio.html")

from TercerEntrega.forms import UserEditForm

@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "TercerEntrega/inicio.html")

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "TercerEntrega/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})



def eliminarusuario(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            usuario.delete()

            return render(request, "TercerEntrega/inicio.html")

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "TercerEntrega/eliminarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})
