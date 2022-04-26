import sys
def cambiar(x):
    print('Direccion de X')
    print(id(x))
    print(x)
    x=40
    print('Direccion de X cambiada')
    print(id(x))
def main():
    i = 300
    j = 300
    print('dirección de i = ', hex(id(i)))
    print('dirección de j =', hex(id(j)))
    print('dirección de 300 =', hex(id(300)))
    i = i + 1
    print('dirección de i incrementado =', hex(id(i)))
    print('dirección de j antes de incrementar =', hex(id(j)))
    j = j + 1
    print('dirección de j incrementado = ', hex(id(j)))
def ejemploRefcount():
    uno = 1
    dos = uno
    tres = uno
    cuatro = 1
    print('Direccion de {}, {}'.format(hex(id(uno)),'uno'))
    for k, v in locals().items():
        print('Direccion de {}, {}'.format(hex(id(v)),k))
    lista=[1,2,3,4,1]
    for i in range(len(lista)):
        print('Dirección {}, valor {}'.format(hex(id(lista[i])),lista[i]))
def objetosPython():
    i = 1
    interes = 2.3
    bandera = False
    cadena = 'CUIL erróneo'
    lista = [1, 2, 3]
    print('Tipo de datos de i', type(i))
    print('Tipo de datos de interes: ', type(interes))
    print('Tipo de datos de bandera: ', type(bandera))
    print('Tipo de datos de cadena: ', type(cadena))
    print('Tipo de datos de lista: ', type(lista))
    print('Tipo de datos de objetosPython(): ', type(objetosPython))

def pasajePorValor(x):
    print('En el interior de la función')
    print('Dirección de x: {}, valor: {} '.format(hex(id(x)), x))
    x = x + ' y muuucho mas'
    print('Dirección de x: {}, valor: {} '.format(hex(id(x)),x))

def main2():
    variable = 'algo mas'
    pasajePorValor(variable)
    print('En el programa principal')
    print('Dirección de x: {}, valor: {} '.format(hex(id(variable)), variable))
def pasajePorReferencia(l):
    print('En el interior de la función')
    print('Dirección de l: {}, valor: {} '.format(hex(id(l)), l))
    l[0] = 100
    l[1] = 200
    l[2] = 300
    print('Dirección de l: {}, valor: {} '.format(hex(id(l)), l))
if __name__ == '__main__':
    main2()
    
    #lista = [1,2,3,4,5]
    #print('En el programa principal')
    #print('Dirección de lista: {}, valor: {} '.format(hex(id(lista)), lista))
    #pasajePorReferencia(lista)
    #print('Luego de probar función pasajePorRerencia')
    #print('Dirección de lista: {}, valor: {} '.format(hex(id(lista)), lista))
