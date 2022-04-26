# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 18:51:39 2020

@author: morte
"""
import ctypes
import gc
# We use ctypes moule  to access our unreachable objects by memory address.
class PyObject(ctypes.Structure):
    _fields_ = [("refcnt", ctypes.c_long)]


gc.disable()  # Desactiva el Garbage Collector generacional (gc)
#gc.enable()
lst = []
lst.append(lst)

# Guarda la dirección de lista 
lst_address = id(lst)

#Imprime 2 refencias, lst, y lst dentro de la lista
print('Dirección: ',hex(lst_address), 'Referencias: ',PyObject.from_address(lst_address).refcnt)

# Destruye la refencia lst 
del lst


object_1 = {}
object_2 = {}
object_1['obj2'] = object_2
object_2['obj1'] = object_1

obj_address = id(object_1)

#Imprime 2 referencias, porque object_1 hace referencia a object_2, y viceversa
print('Dirección: ',hex(obj_address), 'Referencias: ',PyObject.from_address(obj_address).refcnt)

# destruye las referencias
del object_1, object_2

# Descomentar para ver resultados de llamar manualmente al recolector de basura
#gc.collect()

# Ver reference count de las direcciones de objetos
print('Dirección: ',hex(obj_address), 'Referencias: ',PyObject.from_address(obj_address).refcnt)
print('Dirección: ',hex(lst_address), 'Referencias: ',PyObject.from_address(lst_address).refcnt)
gc.enable()