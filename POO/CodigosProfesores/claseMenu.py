from claseManejadorRecepcionProducto import ManejadorRecepcionProducto
from claseManejadorEntregaProducto import ManejadorEntregaProducto

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.salir
                          }
    def opcion(self,op,manejadorRP,manejadorEP):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op=='1' or op=='2':
            func(manejadorRP,manejadorEP)
        else:
            func()
    def salir(self):
        print('Usted salio del programa')
    def opcion1(self,manejadorRP,manejadorEP):
        if type(manejadorRP)==ManejadorRecepcionProducto and type(manejadorEP)==ManejadorEntregaProducto:
            idProductosReparados=manejadorEP.retornaIdProductosReparados()
            manejadorRP.mostrarProductosNoReparados(idProductosReparados)
        else:
            print('Tipo de dato de dato de algun parametro es incorrecto, no se puede llevar a cabo la operacion')
    def opcion2(self,manejadorRP,manejadorEP):
        if type(manejadorRP)==ManejadorRecepcionProducto and type(manejadorEP)==ManejadorEntregaProducto:
            marca=input('Ingrese marca:')
            idProductos=manejadorRP.BuscarIdProductosPorMarca(marca)
            if len(idProductos)>0:
                manejadorEP.calcularMontoTotalPorMarca(idProductos,marca)
            else:
                print('No se encontraron productos para la marca ingresada')
        else:
            print('Tipo de dato de dato de algun parametro es incorrecto, no se puede llevar a cabo la operacion')  
        