from django.db import models
from django.utils import timezone
from PIL import Image
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Criar lista de Categorias.
LISTA_CATEGORIA = (
    ("ENTULHO", "Entulho"),
    ("PLASTICO", "Plástico"),
    ("FERRO", "Ferro"),
    ("MADEIRA", "Madeira"),
    ("OUTROS", "Outros")
)

# Criar o anuncio
# Criar o anúncio
class Anuncio(models.Model):
    usuario = models.ForeignKey(
        'Usuario',  # Referencia o modelo personalizado
        on_delete=models.CASCADE,
        related_name="anuncios"
    )
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_anuncios')
    descricao = models.TextField(max_length=1000)
    localizacao = models.CharField(max_length=150)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIA)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        # Salva a instância primeiro
        super().save(*args, **kwargs)

        # Abre a imagem salva
        with Image.open(self.thumb.path) as img:
            # Define o tamanho desejado (exemplo: 300x300 pixels)
            tamanho_desejado = (600, 600)

            # Redimensiona a imagem
            img.thumbnail(tamanho_desejado)

            # Salva a imagem redimensionada
            img.save(self.thumb.path)

    def __str__(self):
        return self.titulo

# Modelo personalizado de usuário
class Usuario(AbstractUser):
    anuncios_vistos = models.ManyToManyField("Anuncio", related_name="usuarios_que_visualizaram")