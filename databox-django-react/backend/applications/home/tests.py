from django.test import TestCase
from django.urls import reverse

class HomePageTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_template_used(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home/home.html')

    def test_home_page_contains_correct_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, "Transforme seu negócio com IA")
        self.assertContains(response, "Mapeie seu cenário atual e encontre oportunidades.")
        self.assertContains(response, "Use IA para escalar suas decisões.")
        self.assertContains(response, "Visualize suas métricas com clareza.")