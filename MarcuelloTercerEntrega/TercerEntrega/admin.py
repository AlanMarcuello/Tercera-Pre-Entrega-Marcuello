from django.contrib import admin
from  .models import * #importamos el archivo models

# Register your models here.
#registramos los modelos

admin.site.register(Mallas)

admin.site.register(Pijamas)

admin.site.register(RopaInterior)
