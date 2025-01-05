#Variáveis personalizadas que vou ter acesso dentro das páginas

from .models import Anuncio

def lista_anuncios_recentes(request):
    lista_anuncios = Anuncio.objects.all().order_by('-data_criacao')[0:3]
    return {"lista_anuncios_recentes": lista_anuncios }

