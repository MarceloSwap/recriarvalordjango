# url - view - template

from django.urls import path, reverse_lazy
from .views import Anuncios, Home, Detalhes, PesquisaAnuncio, PaginaPerfil, CriarConta
from django.contrib.auth import views as auth_view

app_name='anuncio'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('anuncios/', Anuncios.as_view(), name='anuncios'),
    path('anuncios/<int:pk>', Detalhes.as_view(), name='detalhes'),
    path('pesquisa/', PesquisaAnuncio.as_view(), name='pesquisaanuncio'),
    path('login/' , auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editarperfil/<int:pk>', PaginaPerfil.as_view(), name='editarperfil'),
    path('criarconta/', CriarConta.as_view(), name='criarconta'),
    path('mudarsenha/', auth_view.PasswordChangeView.as_view(template_name='editarperfil.html', success_url=reverse_lazy('anuncio:anuncios')), name='mudarsenha'),
]
