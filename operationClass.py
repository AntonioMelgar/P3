import math

class Operacion:

	def sumar(self,valor1,valor2):
		suma=valor1+valor2
		return(suma)

	def restar(self,valor1,valor2):
		resta=valor1-valor2
		return(resta)

	def multiplicar(self,valor1,valor2):
		multi=valor1*valor2
		return(multi)

	def dividir(self,valor1,valor2):
		divi=valor1/valor2
		return(divi)

	def raiz(self,valor1):
		raiz=math.sqrt(valor1)
		return(raiz)
     

