import unittest
from city_functions import city_country
class CitiesTestCase(unittest.TestCase):
    """Testes para 'city_functions.py'"""
    def test_city_country(self):
        """Messagens do tipo São paulo, Brasil funcionam?"""
        output = city_country('são paulo','brasil')
        self.assertEqual(output,'São Paulo, Brasil')
    def test_city_country_population(self):
        """Messagens do tipo Indaial, Brasil - população 70000 funciona?"""
        output = city_country('indaial','brasil',70000)
        self.assertEqual(output, 'Indaial, Brasil - população 70000')
unittest.main()