from django.contrib import admin
from .models import Home  # Corrigido para importar o modelo correto

admin.site.register(Home)  # Registrar o modelo Home