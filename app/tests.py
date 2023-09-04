from django.test import TestCase

# Create your tests here.
environt_path = ' http://127.0.0.1:8000'

'''
# Test de comprobacion de urls
class SimpleTest(TestCase):
    def test_nosotros(self):
        response = self.client.get(environt_path + '/nosotros/')
        self.assertEqual(response.status_code, 200)
    
    def test_home(self):
        response = self.client.get(environt_path + '/home/')
        self.assertEqual(response.status_code, 200)
    
    def test_contacto(self):
        response = self.client.get(environt_path + '/contacto/')
        self.assertEqual(response.status_code, 200)

    def test_contactos(self):
        response = self.client.get(environt_path + '/contactos/')
        self.assertEqual(response.status_code, 404)
'''


 
'''
class HomeViewRequestTestCase(TestCase):
    def test_index_loads_property(self):
        response = self.client.get(environt_path)
        self.assertEqual(response.status_code,404)
'''



