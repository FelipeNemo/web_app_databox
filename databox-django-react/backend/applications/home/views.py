from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import Home  # Corrigido para importar o modelo correto

class HomeView(View):
    def get(self, request):
        context = {
            'logo': 'path/to/logo_databox.png',  # Update with the correct path
            'data_icon': 'path/to/data_icon.png',
            'ia_icon': 'path/to/ia_icon.png',
            'dash_icon': 'path/to/dash_icon.png',
        }
        return render(request, 'home/home.html', context)

class DiagnosticoView(View):
    def get(self, request):
        return render(request, 'home/diagnostico.html')

class EstrategiasView(View):
    def get(self, request):
        return render(request, 'home/estrategias.html')

class DashboardsView(View):
    def get(self, request):
        return render(request, 'home/dashboards.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'home/login.html')

class PerguntasView(View):
    def get(self, request):
        return render(request, 'home/perguntas.html')

    def post(self, request):
        # Handle form submission here
        return redirect('home')  # Redirect to home after submission