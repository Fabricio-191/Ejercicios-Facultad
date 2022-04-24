/*
Se posee información de 500 abonados al servicio de gas. 
De cada abonado se conoce el número de cliente entre 200 y 700 (200,201,202...700), consumo de gas y el importe mensual a abonar.

Construya un algoritmo que usando subprogramas permita:

1. Generar 2 arreglos uno para almacenar el consumo de gas y otro que almacene el importe mensual a abonar 
(de modo tal que la primera componente del arreglo de consumo de gas se corresponda con la primera componente del arreglo de importe mensual a abonar y así sucesivamente) 
sabiendo que la información se ingresa ordenada de manera ascendente por importe (desde menor hasta el mayor).
2. Decir si algún usuario superó los 5000 pesos de importe en su factura.
3. Ingresar por teclado un consumo de gas y decir el importe mensual a abonar.
4. Generar una nueva estructura con el número de usuario de aquellos que superan el importe promedio de consumo.
5. Mostrar los números de usuarios que fueron almacenados en la nueva estructura.
*/
constante N = 500

void cargar(real consumos[N], real importes[N])
Comienzo
    entero i
    real consumo, importe

    Para i desde 0 hasta N - 1
        Escribir "Introduzca el consumo y importe del cliente: ", i + 200
        Leer consumo, importe

        consumos[i] = consumo
        importes[i] = importe
    FinPara
    retorna()
Fin

void supero5000(real importe[N])
Comienzo
    entero i
    bool band

	band = falso
    i = 0

    Mientras((i < N) y (!band))
        Si(importe[i] > 5000)
            Entonces band = verdadero
            Sino i += 1
        FinSi
    FinMientras

    Si(band)
        Entonces Escribir "Hay un usuario que supero los 5000 pesos de importe"
    FinSi
    retorna()
Fin

real promedio(real arreglo[N])
Comienzo
    entero i
    real acc
    acc = 0

    Para i desde 0 hasta N - 1
        acc += arreglo[i]
    FinPara

    retorna(acc / N)
Fin

void mostrarMayores(real mayoresProm[N], entero NT)
Comienzo
    Para i desde 0 hasta NT - 1
        Escribir "El usuario ", mayoresProm[i], " tiene un importe mayor al promedio"
    FinPara
    retorna()
Fin

void mayorAlPromedio(real importes[N])
Comienzo
    entero i, NT
    real mayoresProm[N], prom

    NT = 0
    prom = promedio(importes)

    Para i desde 0 hasta N - 1
        Si(importes[i] > prom)
            Entonces 
                mayoresProm[NT] = i + 200
                NT += 1
        FinSi
    FinPara

    mostrarMayores(mayoresProm, NT)
    retorna()
Fin

entero encontrarConsumo(real consumos[N], real valor)
Comienzo
    entero i
    bool encontro

    i = 0
    encontro = falso

    Mientras((i < N) y (!encontro))
        Si(consumos[i] == valor)
            Entonces encontro = verdadero
            Sino i += 1
        FinSi
    FinMientras

    Si(!encontro)
        Entonces i = -1
    FinSi
    retorna(i)
Fin

void selector(real consumos[N], real importes[N])
Comienzo
    entero i
    real consumo

    Escribir "Introduzca el consumo de gas (0 para terminar)"
    Leer consumo // 20

    Mientras(consumo != 0)
        i = encontrarConsumo(consumos, consumo)

        Si(i == -1)
            Entonces Escribir "No se encontro ese consumo"
            Sino Escribir "Para ese consumo hay que pagar: ", importes[i]
        FinSi

        Escribir "Introduzca el consumo de gas (0 para terminar)"
        Leer consumo
    FinMientras
	
    retorna()
Fin

// Algoritmo Principal
Comienzo
    real consumos[N], importes[N]

    cargar(consumos, importes)
    supero5000(importes)

    mayorAlPromedio(importes)
    selector(consumos, importes)
Fin

