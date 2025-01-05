from django.apps import AppConfig


class AnuncioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'anuncio'

    def ready(self):
        from django.db.utils import OperationalError
        try:
            from .models import Usuario
            import os
            email = os.getenv('EMAIL_ADMIN')
            senha = os.getenv('SENHA_ADMIN')
            if email and senha:
                usuarios = Usuario.objects.filter(email=email)
                if not usuarios.exists():
                    Usuario.objects.create_superuser(
                        username="admin",
                        email=email,
                        password=senha,
                        is_active=True,
                        is_staff=True
                    )
        except OperationalError:
            # Evita erro se o banco ainda não foi migrado
            pass
