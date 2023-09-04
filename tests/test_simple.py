from django.test import TestCase
from django.urls import reverse



# Test de comprobacion de urls
class SimpleTest(TestCase):
    def test_nosotros(self):
        url_nosotros = reverse('nosotros')
        response = self.client.get(url_nosotros)
        self.assertEqual(response.status_code, 200)
    
    def test_home(self):
        url_home = reverse('home')
        response = self.client.get(url_home)
        self.assertEqual(response.status_code, 200)
    
    def test_contacto(self):
        url_contacto = reverse('contacto')
        response = self.client.get(url_contacto)
        self.assertEqual(response.status_code, 200)


