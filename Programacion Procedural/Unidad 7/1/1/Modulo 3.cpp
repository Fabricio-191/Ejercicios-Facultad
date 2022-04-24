/*
Una consultora contable trabaja en la liquidación de haberes de los empleados de varias empresas pequeñas.

La empresa posee en un archivo “EMPRESAS.dat” con información general de cada una de las empresas: código (número secuencial, generado automáticamente a partir de 1200), nombre, CUIT y dirección.

Para el cálculo de sueldos de los empleados se realiza de la misma forma, se trabaja con un archivo de empleados ordenado ascendentemente por Código de empresa.

El archivo de empleados “EMPLEADOS.dat” posee la siguiente información: Nombre del Empleado, código de la empresa donde trabaja, DNI, sueldo básico, antigüedad.

Los empleados además tienen descuentos fijos sobre su remuneración (sueldo básico más antigüedad), estos son: Jubilación 11%, Obra Social 3%, Seguro de Vida $ 3,80.

Se pide generar diferentes módulos que permitan:

Módulo 1: Genera un archivo con información de las distintas empresas que trabajan con el estudio contable.

Módulo 2: Generar un archivo con información de los empleados.

Módulo 3: Emita un listado ordenado por empresa con la liquidación de haberes de cada empleado, que incluya además el Total Pagado en concepto de haberes y el Total Pagado en concepto de Descuento:
*/

#include <stdio.h>
#include <string.h>
#include <malloc.h>
#include "header.h"

static char* leerString(FILE* archivo) {
	char str[200];
	fgets(str, 200, archivo);

	int len = strlen(str);
	str[len - 1] = '\0';

	char* string = (char*) malloc(sizeof(char) * len);
	strcpy(string, str);

	return string;
}

empresa* leerEmpresa(FILE* archivo) {
	if (feof(archivo)) return NULL;

	empresa* nuevaEmpresa = (empresa*) malloc(sizeof(empresa));
	fscanf(archivo, "Codigo: %d\n", &nuevaEmpresa->cod);
	fscanf(archivo, "Nombre: ");
	nuevaEmpresa->nombre = leerString(archivo);
	fscanf(archivo, "CUIT: ");
	nuevaEmpresa->CUIT = leerString(archivo);
	fscanf(archivo, "Direccion: ");
	nuevaEmpresa->direccion = leerString(archivo);
	fscanf(archivo, "\n");
	nuevaEmpresa->next = leerEmpresa(archivo);

	return nuevaEmpresa;
}

empleado* leerEmpleado(FILE* archivo) {
	if (feof(archivo)) return NULL;
	
	empleado* nuevoEmpleado = (empleado*)malloc(sizeof(empleado));
	fscanf(archivo, "Nombre: ");
	nuevoEmpleado->nombre = leerString(archivo);
	fscanf(archivo, "Empresa: %d\nDNI: ", &nuevoEmpleado->codEmpresa);
	nuevoEmpleado->DNI = leerString(archivo);
	fscanf(
		archivo, "Sueldo: %f\nAntiguedad: %d\n\n",
		&nuevoEmpleado->sueldo,
		&nuevoEmpleado->antiguedad
	);
	nuevoEmpleado->next = leerEmpleado(archivo);

	return nuevoEmpleado;
}

void emitirListado(empresa* empresa, empleado* empleado) {
	while (empresa != NULL) {
		float acum = 0;
		int cant = 0;
		printf("Empresa: %s\n", empresa->nombre);
		printf("Nombre del empleado\t\tRemuneracion\n");

		while (empleado != NULL && empleado->codEmpresa == empresa->cod) {
			printf("  %s\t\t\t%.2f\n", empleado->nombre, empleado->sueldo);

			cant++;
			acum += empleado->sueldo;
			empleado = empleado->next;
		}

		printf("\n  Total pagado en concepto de haberes: %.2f\n", acum);
		printf("  Total pagado en concepto de descuentos: %.2f\n\n", acum * 0.14 + 3.8 * cant);
		empresa = empresa->next;
	}
}

void liberar(empresa* empresas, empleado* empleados) {
	while (empresas != NULL) {
		empresa* aux = empresas->next;
		free(empresas->nombre);
		free(empresas->CUIT);
		free(empresas->direccion);
		free(empresas);
		empresas = aux;
	}

	while (empleados != NULL) {
		empleado* aux = empleados->next;
		free(empleados->nombre);
		free(empleados->DNI);
		free(empleados);
		empleados = aux;
	}
}