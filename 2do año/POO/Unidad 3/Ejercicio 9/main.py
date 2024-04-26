from unittest import TestCase, main
from palindromo import Palindromo

class TestPalindromo(TestCase):
	__palindromo: Palindromo

	def setUp(self):
		self.__palindromo = Palindromo("")
		
	def test_palindromo_no_es_str(self):
		with self.assertRaises(TypeError):
			self.__palindromo.setPalabra(123) # type: ignore

		with self.assertRaises(TypeError):
			self.__palindromo.setPalabra(True) # type: ignore

		with self.assertRaises(TypeError):
			self.__palindromo.setPalabra({}) # type: ignore

		with self.assertRaises(TypeError):
			self.__palindromo.setPalabra([]) # type: ignore

	def test_palindromo_vacio(self):
		self.__palindromo.setPalabra('')
		self.assertTrue(self.__palindromo.esPalindromo())
	
	def test_palindromo_con_un_caracter(self):
		self.__palindromo.setPalabra('a')
		self.assertTrue(self.__palindromo.esPalindromo())

		self.__palindromo.setPalabra('#')
		self.assertTrue(self.__palindromo.esPalindromo())

		self.__palindromo.setPalabra('🖖')
		self.assertTrue(self.__palindromo.esPalindromo())

	def test_palindromo_con_dos_caracteres(self):
		self.__palindromo.setPalabra('ab')
		self.assertFalse(self.__palindromo.esPalindromo())

		self.__palindromo.setPalabra('ba')
		self.assertFalse(self.__palindromo.esPalindromo())

		self.__palindromo.setPalabra('aa')
		self.assertTrue(self.__palindromo.esPalindromo())

		self.__palindromo.setPalabra('🖖🖖')
		self.assertTrue(self.__palindromo.esPalindromo())

	def test_palindromo_con_tres_caracteres(self):
		self.__palindromo.setPalabra('aba')
		self.assertTrue(self.__palindromo.esPalindromo())

		self.__palindromo.setPalabra('abb')
		self.assertFalse(self.__palindromo.esPalindromo())

	def test_palindromo_con_cuatro_caracteres(self):
		self.__palindromo.setPalabra('abba')
		self.assertTrue(self.__palindromo.esPalindromo())

		self.__palindromo.setPalabra('abab')
		self.assertFalse(self.__palindromo.esPalindromo())

if __name__ == '__main__':
	main()