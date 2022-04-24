/* 
Ejercicio 5
Construya un algoritmo que usando subprogramas permita:

1. Generar una estructura arreglo que almacene 20 números primos. Debe verificar que cada número que se lea sea primo antes de cargarlo en el arreglo.
2. Ingresar un valor y decir en el algoritmo principal qué lugar ocupa en el arreglo.
3. Generar un subarreglo que contenga los números primos mayores a 1000.
4. Mostrar de los datos del subarreglo que oscilan entre dos valores previamente ingresados por teclado.
*/
constante N = 20

booleno esPrimo(entero num)
Comienzo
    entero i, divs
    
    divs = 0

    Para i desde 1 hasta num
        Si((num % i) == 0)
            Entonces divs++
        FinSi
    FinPara
    
    Si(divs <= 2)
        entonces retorna(verdadero)
        sino retorna(falso)
    FinSi
Fin

void carga(entero nums[N])
Comienzo
    entero num, i

    i = 0

    Mientras(i < N)
        Escribir "Introduzca un numero primo"
        Leer num

        Si(esPrimo(num))
            Entonces
                nums[i] = num
                i++
            Sino Escribir "Ese numero no es primo"
        FinSi
    FinMientras
    retorna()
Fin

entero buscar(entero nums[N], entero num) //inciso 2
Comienzo
    entero i
    booleano encontro

    encontro = falso
    i = 0

    Mientras((i < N) y (!encontro))
        Si(nums[i] == num)
            Entonces encontro = verdadero
            Sino i += 1
        FinSi
    FinMientras

    Si(!encontro)
        Entonces i = -1
    FinSi

    retorna (i)
Fin

// es que el selector y el buscar los re utilice de otro codigo
void selector(entero nums[N]) //inciso 2
Comienzo
    entero indice
    real valor

    Escribir "Introduzca el valor a buscar"
    Leer valor

    indice = buscar(nums, valor)

    Si(indice == -1)
        Entonces Escribir "Ese numero no esta en el arreglo"
        Sino Escribir "Ese numero esta en la posicion ", indice
    FinSi

    retorna()
Fin

entero cargaMayores1000(entero nums[N], entero mayores[N])
Comienzo
    entero NT, i

    NT = 0

    Para i desde 0 hasta N - 1
        Si(nums[i] > 1000)
            Entonces
                mayores[NT] = nums[i]
                NT++
        FinSi
    FinPara

    retorna(NT)
Fin

void mostrarEntre(entero mayores1000[N], entero NT, entero min, entero max)
Comienzo
    entero i, num
    Para i desde 0 hasta NT - 1 
        num = mayores1000[i]
        Si((num >= min) y (num <= max))
            Entonces Escribir num, "esta entre ", min, " y ", max
        FinSi
    FinPara

    retorna()
Fin

// Algoritmo Principal 
comienzo
    entero nums[N], mayores1000[N], min, max, NT

    carga(nums) //1
    selector(nums) //2
    NT = cargaMayores1000(nums, mayores1000) //3

    Escribir "Introduzca el numero menor"
    Leer min
    Escribir "Introduzca el numero mayor"
    Leer max

    Si(max > min)
        Entonces  mostrarEntre(mayores1000, NT, min, max)
        Sino mostrarEntre(mayores1000, NT, max, min)
    FinSi
fin