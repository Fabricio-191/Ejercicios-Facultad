"""
Herencia Múltiple, polimorfismo      

En el ámbito universitario los agentes que ahí trabajan se pueden clasificar de la siguiente manera: Docentes, investigadores, docente investigador y personal de apoyo.

La información del personal universitario se encuentra almacenada en un archivo denominado “personal.json”.

El Centro de cómputos de la UNSJ, lo contrata a usted como programador, para que desarrolle una aplicación que permita procesar el archivo .json donde guarda la información del personal que trabaja en la misma. Para ello le provee la siguiente narrativa, que ha sido elaborada por el analista funcional:

Narrativa          

De todo el personal se conoce la siguiente información: cuil, apellido, nombre, sueldo básico y antigüedad.

Si es un docente se registra además carrera en la que dicta clases, cargo y cátedra.

Si es personal de apoyo se registra además categoría.

Si es un investigador se registra además área de investigación y tipo de investigación

Si es un docente investigador se registra además carrera en la que dicta clases, cargo, cátedra, área de investigación y tipo de investigación, categoría en el programa de incentivos de investigación, importe extra por docencia e investigación.

Para cumplir con las tareas solicitadas por el analista, usted deberá:

a) Definir la jerarquía de clases correspondiente a la narrativa dada.

b) Almacenar en una colección tipo Lista definida por el programador, los agentes de la Universidad, obteniendo los datos del archivo “personal.json”, la misma deberá implementar la interfaz definida en el ejercicio 5. Los nodos de la lista, serán referencias a objetos que representen objetos de la clase base de la jerarquía.    

c) Implementar un programa principal con un menú de opciones que permita testear las siguientes acciones:

        Insertar a agentes a la colección.
        Agregar agentes a la colección.
         Dada una posición de la lista: Mostrar por pantalla que tipo de agente se encuentra almacenado en dicha posición.
        Ingresar por teclado el nombre de una carrera y generar un listado ordenado por nombre con todos los datos de los agentes que se desempeñan como docentes investigadores.
         Dada un área de investigación, contar la cantidad de agentes que son docente    investigador, y la cantidad de investigadores que trabajen en ese área.
        Recorrer la colección y generar un listado que muestre nombre y apellido, tipo de Agente y sueldo de todos los agentes, ordenado por apellido.
        Dada una categoría de investigación (I, II, III, IV o V), leída desde teclado, listar apellido, nombre e importe extra por docencia e investigación, de todos los docentes investigadores que poseen esa categoría, al final del listado deberá mostrar el total de dinero que la Secretaría de Investigación debe solicitar al Ministerio en concepto de importe extra que cobran los docentes investigadores de la categoría solicitada.    
        Almacenar los datos de todos los agentes en el archivo “personal.json”    

 Reglas de negocio para el cálculo del sueldo:

Por cada año de antigüedad el sueldo se incrementa en un porcentaje sobre el sueldo básico por ejemplo: si tienen 5 años de antigüedad el sueldo sería sueldo básico + 5%(básico).

Porcentaje por cargo: 10 % si el cargo es simple, 20% si el cargo es semiexclusivo, 50% si el cargo es exclusivo.

Porcentaje por categoría: 10% si la categoría es de 1 a 10, 20 % si la categoría es de 11 a      20, 30% si la categoría es de 21 a 22.

Todos los porcentajes se calculan sobre el sueldo básico.

sueldoPersonalDeApoyo = Sueldo Básico + %antigüedad+% por categorías

sueldoDocente = Sueldo Básico + %antigüedad+% por cargo

sueldoInvestigador = Sueldo básico+% antigüedad

sueldoDocenteInvestigador = sueldoDocente()+importe extra por docencia e investigación.
"""