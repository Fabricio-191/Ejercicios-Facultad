/*
La empresa posee en un archivo �EMPRESAS.dat� con informaci�n general de cada una de las empresas: c�digo (n�mero secuencial, generado autom�ticamente a partir de 1200), nombre, CUIT y direcci�n.

M�dulo 1: Genera un archivo con informaci�n de las distintas empresas que trabajan con el estudio contable.
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "header.h"

int generarArchivoEmpresas() {
	srand(time(NULL));
	const int N = rand() % 100;

	FILE* archivo = fopen("EMPRESAS.dat", "w");
	if (archivo == NULL) {
		printf("Error al abrir el archivo EMPRESAS.dat en modo escritura\n");
		return 0;
	}

	for (int i = 0; i < N; i++) {
		fprintf(archivo, "Codigo: %d\n", i + 1200);
		fprintf(archivo, "Nombre: Empresa %d\n", i + 1);
		fprintf(archivo, "CUIT: %02d-%07d-%02d\n", rand() % 100, rand() % 1000000, rand() % 100);
		fprintf(archivo, "Direccion: Yonge Street %d\n\n", rand() % 1000000);
	}
	fclose(archivo);

	return N;
}