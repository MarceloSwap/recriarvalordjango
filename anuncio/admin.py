from django.contrib import admin
from .models import Anuncio, Usuario
from django.contrib.auth.admin import UserAdmin #Gerenciamento de usuario

# só exite pq pra no admin aparecer o campo personalizado anuncios vistos
campos = list(UserAdmin.fieldsets)
campos.append(
    ("Histórico", {'fields': ('anuncios_vistos',)})
)
UserAdmin.fieldsets = tuple(campos)

# Register your models here.
admin.site.register(Anuncio)
admin.site.register(Usuario, UserAdmin)

