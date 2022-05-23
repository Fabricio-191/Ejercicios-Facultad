"""
Herencia y archivos JSON

Una  empresa comercial necesita registrar los datos de los aparatos electrónicos que comercializa. La empresa comercializa tres tipos de aparatos: Televisores, Heladeras y Lavarropas. Para ello cuenta con un archivo, "aparatoselectronicos.json", con la estructura necesaria para almacenar televisores, heladeras y lavarropas.

De todos los aparatos se debe registrar: marca, modelo, color, país de fabricación y precio base.

De un televisor se registra además: tipo de pantalla (crt, vga, svga, plasma, lcd, led, TouchScreen, MultiTouch), pulgadas, tipo de definición (SD, HD, FULL HD), conexión a internet(Verdadero/Falso).

De una heladera: capacidad en litros, freezer (Verdadero/Falso), cíclica (Verdadero/Falso).

De un Lavarropas: capacidad de lavado (5 Kg, 6kg, etc), velocidad de centrifugado (600 rpm, 1200 rpm), cantidad de programas, tipo de carga( Frontal, Superior).

 El importe de venta de cada artefacto se calcula en función del precio base y de sus características. Para ello se deben considerar las siguientes reglas de negocio:

 Importe de venta de los Televisores es el precio base más: el 1% si el tipo de definición es SD, 2% si el tipo de definición es HD, 3% si el tipo de definición es FULL HD, mas 10% si tiene conexión a internet.

Importe de venta de los Lavarropas es el precio base, mas: el 1% si la capacidad de lavado es menor o igual a 5 kg , 3% si la capacidad de lavado supera los 5 kg.

 Importe de venta de las Heladeras es el precio base más: 1% si no tiene freezer, 5% si tiene freezer, 10% si es cíclica.

Nota: Todos los porcentajes se calculan sobre el precio base.

 El analista le solicita a usted que desarrolle una aplicación con las siguientes restricciones.

La colección de aparatos debe implementarse usando una lista definida por el programador, donde los nodos deberán almacenar aparatos.

La lista deberá proveer los métodos y atributos necesarios para que sea un iterable, e implementar  la  interface del ejercicio 5.

Para cumplir con lo solicitado por el analista, usted deberá:

a)  Definir la jerarquía de clases correspondiente a la problemática planteada.    

b) Leer y procesar el archivo “aparatoselectronicos.json” para almacenar en la lista los aparatos  de la empresa.    

c) Implemente un programa que a través de un menú de opciones permita:

    Insertar un aparato en la colección en una posición determinada.
    Agregar un aparato a la colección (solicitar el tipo de aparato, y luego los datos que correspondan).
    Dada una posición de la Lista: Mostrar por pantalla qué tipo de objeto se encuentra almacenado en dicha posición.

       4. Mostrar la cantidad de heladeras, lavarropas y televisores cuya marca sea phillips.

    Mostrar la marca de todos los lavarropas que tienen carga superior .
    Mostrar para todos los aparatos que la empresa tiene a la venta, marca, país de fabricación e importe de venta.
    Almacenar los objetos de la colección Lista en el archivo “aparatoselectronicos.json”.
"""

