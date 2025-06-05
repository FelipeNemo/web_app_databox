from django.urls import path
from .views import mostrar_home, mostrar_diagnostico, mostrar_estrategias, mostrar_dashboards, mostrar_login, mostrar_perguntas

urlpatterns = [
    path('', mostrar_home, name='home'),
    path('diagnostico/', mostrar_diagnostico, name='diagnostico'),
    path('estrategias/', mostrar_estrategias, name='estrategias'),
    path('dashboards/', mostrar_dashboards, name='dashboards'),
    path('login/', mostrar_login, name='login'),
    path('perguntas/', mostrar_perguntas, name='perguntas'),
]