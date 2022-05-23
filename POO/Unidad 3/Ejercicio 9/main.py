from unittest import TestCase, main
from palindromo import Palindromo
import string
import random
import numpy

numpy.array([]).resize()

def random_string(length):
	return ''.join(
		random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length)
	)

class TestPalindromo(TestCase):
	__palindromo: Palindromo

	def setUp(self):
		self.__palindromo = Palindromo("")

	def test_palindromo_vacio(self):
		self.assertFalse(self.__palindromo.esPalindromo())
	
	def test_palindromo_con_un_caracter(self):
		self.__palindromo.setPalabra("a")
		self.assertTrue(self.__palindromo.esPalindromo())

	def test_palindromo_con_dos_caracteres(self):
		self.__palindromo.setPalabra("aa")
		self.assertTrue(self.__palindromo.esPalindromo())

	def test_palindromo_con_tres_caracteres(self):
		self.__palindromo.setPalabra("aaa")
		self.assertTrue(self.__palindromo.esPalindromo())

	def test_palindromo_con_cuatro_caracteres(self):
		self.__palindromo.setPalabra("aaaa")
		self.assertTrue(self.__palindromo.esPalindromo())

	def generarPalindromo(self, palabra):
		self.__palindromo.setPalabra(palabra)
		return self.__palindromo.esPalindromo()

if __name__ == '__main__':
	main()