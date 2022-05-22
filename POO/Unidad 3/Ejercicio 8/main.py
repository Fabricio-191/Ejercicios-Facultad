"""
Usar la narrativa del Ejercicio Nº 7

Se ha agregado nuevos requerimientos al sistema, y usted como programador, debe darles solución:

El sistema prevé que los agentes serán administrados a través de una colección. Existen dos interfaces distintas para operar con agentes, la interfaz del Tesorero, que solamente puede acceder a los gastos que la universidad tiene en concepto de sueldos, para ello, dado un número de documento, podrá consultar el gasto de sueldos para el agente al que pertenece dicho número de documento.

La interfaz del Director, permite modificar el sueldo básico de todos los agentes, el porcentaje que se paga por cargo a un docente,  el porcentaje que se paga por categoría a un personal de apoyo, y el porcentaje extra que se paga a un docente investigador; para ello debe proveerse el número de documento del agente, y el valor que corresponda según lo que se quiera modificar.

Usted deberá crear las interfaces mencionadas con las funcionalidades solicitadas.

class ITesorero (Interface)

   def gastosSueldoPorEmpleado ( dni):

       pass

 

class IDirector (Interface)

   def modificarBasico(dni, nuevoBasico):

       pass

   def modificarPorcentajeporcargo(dni, nuevoPorcentaje):

     pass

   def modificarPorcentajeporcategoría(dni, nuevoPorcentaje):

       pass

def modificarImporteExtra(dni, nuevoImporteExtra):

       pass

 

En el programa principal agregue una opción para el Tesorero y un menú de opciones para Director. Para ello deberá autenticar al usuario que quiere acceder, si es tesorero, accederá a las funcionalidades de tesorero y si es director, accederá a las funciones de director. La autenticación del usuario se hace pidiendo nombre de usuario y contraseña.

Usuario/contraseña para Tesorero: uTesoreso/ag@74ck

Usuario/contraseña para Director: uDirector/ufC77#!1
"""