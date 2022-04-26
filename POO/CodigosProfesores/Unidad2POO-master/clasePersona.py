class Persona:
    __dni = 0
    __nombre = ''
    __apellido= ''
    __sueldo = 0.0
    def __init__(self, dni, nombre, apellido, sueldo = 35000.0):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__sueldo = sueldo
    def getSueldo(self):
        return self.__sueldo
    def __str__(self):
        return 'Apellido y nombre: '+self.__apellido+', '+self.__nombre
    def mostrarDatos(self):
        print('Nombre {}, Apellido {}, DNI {}, sueldo {}'.format(self.__nombre, self.__apellido, self.__dni, self.__sueldo))

#### FUNCIONES PARA CARGA DE DATOS DE PERSONA Y LISTA
def crearPersona():
    print('Ingrese los siguientes datos:')
    dni = int(input('DNI:'))
    nombre = input('Nombre: ')
    apellido = input('Apellido: ')
    sueldo = float(input('Sueldo: '))
    persona = Persona(dni, nombre, apellido, sueldo)
    return persona

def cargarPersonas(lista):
    for i in range(5):
        p = crearPersona()
        print(p)
        lista.append(p)
def calcularMaximoSueldo(lista):
    maximo = 0.0
    indiceMaximo = -1
    for i in range(len(lista)):
        if(lista[i].getSueldo()>maximo):
            maximo = lista[i].getSueldo()
            indiceMaximo = i
    return indiceMaximo

if __name__ == '__main__':
    listaPersonas = []
    unaPersona = Persona(11203567,'Nahuel', 'Catanzaro',9996)
    listaPersonas.append(unaPersona)
    otraPersona = Persona(1234533,'Liza', 'Laine', 45678)
    listaPersonas.append(otraPersona)
    for i in range(len(listaPersonas)):
        listaPersonas[i].mostrarDatos()
    #cargarPersonas(listaPersonas)

    for objeto in listaPersonas:
        objeto.mostrarDatos()
    indice = calcularMaximoSueldo(listaPersonas)
    print('La persona que posee el mayor sueldo es {}, con un sueldo de {}'.format(listaPersonas[indice], listaPersonas[indice].getSueldo()))