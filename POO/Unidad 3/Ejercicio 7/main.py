"""
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
