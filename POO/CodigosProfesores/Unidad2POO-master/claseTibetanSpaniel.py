# -*- coding: utf-8 -*-
class TibetanSpaniel:
    # variables de clase
    '''todos los perros de la raza Spaniel Tibetano
    tienen las mismas características
    '''
    familia = "Companion, herding"
    areaDeOrigen = "Tibet"
    tasaDeAprendizaje = 9
    obediencia = 3
    resolucionDeProblemas = 8
    def __init__(self, nombre, jugueteFavorito, habilidad):
        self.__nombre = nombre
        self.__habilidad = habilidad
        self.__jugueteFavorito = jugueteFavorito
    def getNombre(self):
        return self.__nombre
    #Métodos de clase
    @classmethod
    def getFamilia(cls):
        return cls.familia
    @classmethod
    def getAreaDeOrigen(cls):
        return cls.areaDeOrigen
    @classmethod
    def getTasaDeAprendizaje(cls):
        return cls.tasaDeAprendizaje
    @classmethod
    def getObediencia(cls):
        return cls.obediencia
    @classmethod
    def getResolucionProblemas(cls):
        return cls.resolucionDeProblemas
    @classmethod
    def verRaza(cls):
        print('Características de la Raza')
        print('Familia: '+cls.getFamilia())
        print('Área de Origen: '+cls.getAreaDeOrigen())
        print('Tasa de Aprendizaje:'+str(cls.getTasaDeAprendizaje()))
        print('Obediencia: '+str(cls.getObediencia()))
        print('Tasa de Resolución de problemas: '+str(cls.getResolucionProblemas()))

if __name__ == '__main__':
    TibetanSpaniel.verRaza()
    miSpaniel = TibetanSpaniel('Jhon', 'hueso', 7)
    otroSpaniel = TibetanSpaniel('Coco','minion',8)
    print(miSpaniel.getNombre(),miSpaniel.obediencia)
    print('Cambio de una variable de clase')
    TibetanSpaniel.obediencia = 9
    print(miSpaniel.getNombre(), miSpaniel.obediencia)
    print(otroSpaniel.getNombre(),otroSpaniel.obediencia)