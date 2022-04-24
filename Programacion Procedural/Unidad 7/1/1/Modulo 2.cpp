#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "header.h"

/*
El archivo de empleados �EMPLEADOS.dat� posee la siguiente informaci�n: Nombre del Empleado, c�digo de la empresa donde trabaja, DNI, sueldo b�sico, antig�edad.

M�dulo 2: Generar un archivo con informaci�n de los empleados.
*/

void generarArchivoEmpleados(int cantEmpresas) {
	srand(time(NULL));

	FILE* archivo = fopen("EMPLEADOS.dat", "w");
	if (archivo == NULL) {
		printf("Error al abrir el archivo EMPLEADOS.dat en modo escritura\n");
		return;
	}

	int cont = 1;
	for (int i = 0; i < cantEmpresas; i++) {
		const int N = rand() % 10;
		for (int y = 0; y < N; y++) {
			fprintf(archivo, "Nombre: Empleado %d\n", cont++);
			fprintf(archivo, "Empresa: %d\n", i + 1200);
			fprintf(archivo, "DNI: %d.%03d.%03d\n", rand() % 100, rand() % 1000, rand() % 1000);
			fprintf(archivo, "Sueldo: %f\n", (double) rand() / (double) RAND_MAX * 100000);
			fprintf(archivo, "Antiguedad: %d\n\n", rand() % 25);
		}
	}
	fclose(archivo);
}