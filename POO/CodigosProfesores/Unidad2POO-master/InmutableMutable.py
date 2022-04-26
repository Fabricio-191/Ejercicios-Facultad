def inmutable():
    mi_variable = 'uno, dos'
    print('Dirección de memoria {}, valor almacenado: {}'.format(hex(id(mi_variable)), mi_variable))
    mi_variable += ' y tres'
    print('Dirección de memoria {}, valor almacenado: {}'.format(hex(id(mi_variable)), mi_variable))

def mutable():
    mi_lista = [0,1,2,3,4,5]
    print('Dirección de memoria {}, valor almacenado: {}'.format(hex(id(mi_lista)), mi_lista))
    nuevo_valor = 15
    mi_lista[0]=15
    mi_lista.append(6)
    print('Dirección de memoria {}, valor almacenado: {}'.format(hex(id(mi_lista[0])), mi_lista[0]))
    print('Dirección de memoria {}, valor almacenado: {}'.format(hex(id(nuevo_valor)), nuevo_valor))
if __name__== '__main__':
    mutable()