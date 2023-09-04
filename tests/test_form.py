from django.test import TestCase, Client
from django.urls import reverse


'''
Comprobacion de csrf token para el formulario de contacto de django
'''
class test_form_email(TestCase):
    def setUp(self):
        self.client = Client()
        self.email_url = reverse('contacto') # accedemos a la url  a traves de reverse

    def test_csrf_token_present(self):
        # a tarves de client accedemos a post y enviamos esos datos 
        response = self.client.post(self.email_url, data={
            'name': "Matias",
            'phone': "930013748",
            'email': "m@gmail.com",
            'message': "Este es un mensaje" 
        })
        # comprobamos is tiene el csrf token en el formulario
        self.assertContains(response, 'csrfmiddlewaretoken')


