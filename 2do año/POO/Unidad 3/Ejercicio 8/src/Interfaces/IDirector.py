from zope.interface import Interface

class IDirector (Interface): # type: ignore
    def modificarBasico(self, dni, nuevoBasico):
        pass

    def modificarPorcentajeporcargo(self, dni, nuevoPorcentaje):
        pass

    def modificarPorcentajeporcategoría(self, dni, nuevoPorcentaje):
        pass

    def modificarImporteExtra(self, dni, nuevoImporteExtra):
        pass