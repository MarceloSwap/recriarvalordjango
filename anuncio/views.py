from django.shortcuts import render, redirect, reverse

# para pegar o dado do banco (model)
from .models import Anuncio, Usuario
from .forms import CriarContaForm, HomeForm
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
# CBV
class Home(FormView):
    template_name = "home.html"
    form_class = HomeForm

    # a funcao get padrao por padrao retorna o endereço acima
    # caso contrario vc vai redirecionar pra outro lugar
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            #redirecionar pra views anuncios . Obs: os parametros são o nome do app e o link do pah definidos na urls. não é necessarioamente o nome do diretório
            return redirect('anuncio:anuncios')
        else:
            return super().get(request, *args, **kwargs)  # redireciona o usuario para a url final
        # espera um link como resposta. OBS: usar reverse

    # espera um link como resposta. OBS: usar reverse
    def get_success_url(self):
        #pegando o email
        email = self.request.POST.get("email")
        #print(self.request.POST)

        usuarios = Usuario.objects.filter(email=email)
        if usuarios:
            return reverse('anuncio:login')
        else:
            return  reverse('anuncio:criarconta')


class Anuncios(LoginRequiredMixin, ListView):
    template_name = "anuncios.html"
    model = Anuncio
    #passa a lista de anuncio com o nome padrao de "object_list"
    # "object_list" é a lista de itens do modelo

#Cria uma página pra cada item do banco de dados
class Detalhes(LoginRequiredMixin, DetailView):
    template_name = "detalhes.html"
    model = Anuncio
    # Passa um object -> apenas 1 item do modelo

    # para contar visualizações
    def get(self, request, *args, **kwargs):
        anuncio =self.get_object()
        anuncio.visualizacoes += 1
        anuncio.save()
        #para add na lista de anuncios vistos
        usuario = request.user
        #explicacao: o add, filter e orderby são metodos do db
        usuario.anuncios_vistos.add(anuncio)
        return super().get(request, *args, **kwargs) #redireciona o usuario para a url final


    def get_context_data(self, **kwargs):
        context = super(Detalhes, self).get_context_data(**kwargs)
        # filtrar a minha tabela de anuncios pegando os anuncios cuja categoria é igual a categora do filme da pagina (object)
        # para pegar o mesmo objeto: self.get_object()
        anuncios_relacionados = Anuncio.objects.filter(categoria=self.get_object().categoria)[0:5]
        context["anuncios_relacionados"] = anuncios_relacionados
        return context


class PesquisaAnuncio(LoginRequiredMixin, ListView):
    template_name = "pesquisa.html"
    model = Anuncio

    # object_list
    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list = self.model.objects.filter(titulo__icontains=termo_pesquisa)
            return object_list
        else:
            return None



class Anuncios(LoginRequiredMixin, ListView):
    template_name = "anuncios.html"
    model = Anuncio
    #passa a lista de anuncio com o nome padrao de "object_list"
    # "object_list" é a lista de itens do modelo

# alterar dados como senha no fields colocar os campos
class PaginaPerfil(LoginRequiredMixin, UpdateView):
    template_name = "editarperfil.html"
    model = Usuario
    # de acordo com os campos padrões do AbstractUser da classe Usuarios. OBS olhar da tabela dentro do db para ver outros campos
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        return reverse('anuncio:anuncios')

class CriarConta(FormView):
    template_name = "criarconta.html"
    form_class = CriarContaForm

    #salva no banco
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    # espera um link como resposta. OBS: usar reverse
    def get_success_url(self):
        return reverse('anuncio:login')