# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 21:56:10 2020

@author: morte
"""
"""Cuando hablamos de expresiones regulares, nos referimos (en términos muy 
   generales) a patrones de coincidencia. Patrones que pueden usarse para 
   comparar, extraer, reemplazar o dividir segmentos de un texto particular, 
   en otra cadena, texto largo o documento.
"""
import re
correo='@.'
 
if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',correo.lower()):
	print ("Correo correcto")
else:
	print ("Correo incorrecto")
#Test número entero
numero='123o59'
if re.match('^[0-9]+$', numero):
    print('Número correcto')
else:
    print('Numero incorrecto')
    
#Testeo número flotante
numeroFlotante='12001.98999'
#($[0-9,]+(.[0-9]{2})?)/
if re.match('^[0-9]+(.[0-9]{0,3})$', numeroFlotante):
    print('Número flotante correcto')
else:
    print('Numero flotante incorrecto')

