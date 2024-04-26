from zope.interface import Interface

class ITesorero (Interface): # type: ignore
   def gastosSueldoPorEmpleado(self, dni):
       pass