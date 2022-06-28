
class Fraccion:
    __numerador = 0
    __denominador = 0

    def __init__(self, a, b = 1):
        self.__numerador = a
        self.__denominador = b
        self.simplificar()

    def __mul__(self, otro):
        if type(otro) == int:
            otro = Fraccion(otro)

        return Fraccion(
			self.__numerador * otro.__numerador,
            self.__denominador * otro.__denominador
		)

    __rmul__ = __mul__

    def __add__(self, otro):
        if type(otro) == int:
            otro = Fraccion(otro)

        return Fraccion(
			self.__numerador * otro.__denominador +
            self.__denominador * otro.__numerador,
            self.__denominador * otro.__denominador
		)

    __radd__ = __add__

    def __sub__(self, otro):
        if type(otro) == int:
            otro = Fraccion(otro)

        return Fraccion(
			self.__numerador * otro.__denominador - self.__denominador * otro.__numerador,
            self.__denominador * otro.__denominador
		)

    __rsub__ = __sub__

    def __truediv__(self, otro):
        if type(otro) == int:
            otro = Fraccion(otro)

        return Fraccion(
			self.__numerador * otro.__denominador,
            self.__denominador * otro.__numerador
		)

    __rtruediv__ = __truediv__

    def simplificar(self):
        i = self.__numerador

        while i <= self.__numerador and i >= 2:
            if self.__numerador % i == 0 and self.__denominador % i == 0:
                self.__numerador = self.__numerador // i
                self.__denominador = self.__denominador // i
    
            i -= 1

    def __str__(self):
        return(f'{self.__numerador}/{self.__denominador}')
