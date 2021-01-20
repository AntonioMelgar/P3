from operationClass import Operacion
import unittest


operation = Operacion()
class TestOperacion(unittest.TestCase):

	def test_sumar(self):
		self.assertEqual(operation.sumar(2,8), 10)
	
	def test_restar(self):
		self.assertEqual(operation.restar(2,8), -6)
	
	def test_multiplicar(self):
		self.assertEqual(operation.multiplicar(2,8), 16)
	
	def test_dividir(self):
		self.assertEqual(operation.dividir(2,8), 2/8)
	
	def test_raiz(self):
		self.assertEqual(operation.raiz(81), 9)

if __name__ == '__main__':
    unittest.main()
