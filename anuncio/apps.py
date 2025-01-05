from django.apps import AppConfig


class AnuncioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'anuncio'

    def ready(self):
        from .models import Usuario
        import os

        #pegando as variaveis de ambiente do servidor railway
        email = os.getenv('EMAIL_ADMIN')
        senha = os.getenv('SENHA_ADMIN')

        # Pesquisar se tem o usuario com o email acima
        #Usuario tá sendo puchado do banco
        usuarios = Usuario.objects.filter(email=email)
        if not usuarios:
            Usuario.objects.create_superuser(username="admin", email=email, password=senha, is_active=True, is_staff=True)