#include "header.h"
#include <stdio.h>
const char* ruta = "../Archivos/EMPLEADOS.dat";
/*
Empleados
Los datos de los empleados se almacenan en un archivo llamado “Empleados.dat”. Esta estructura se actualiza
cada vez que se da de alta o baja un empleado.
Cada Empleado tiene un código de identificación (ID del cliente) que comienza a partir de 1 que se genera
automáticamente y permite acceso directo a su información.
Observación: Cada empleado puede acumular hasta 5 pedidos, una vez que realiza la entrega total de los mismos
recién se les podrá agregar más pedidos.
A diario se crea un arreglo con la información de cada uno los empleados adicionando un campo para controlar la
cantidad de pedidos a entregar.

struct empleado {
	char nombre[50], direccion[50], telefono[30], DNI[15];
};
*/

void agregarEmpleado(int cant) {
	FILE* archivo = fopen(ruta, "w+");

	empleado e;
	printf("Introduzca los datos del empleado\n");

	fwrite(&e, sizeof(empleado), 1, archivo);
}