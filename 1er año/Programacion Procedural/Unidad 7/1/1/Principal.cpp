#include <stdio.h>
#include "header.h"

int main() {
	generarArchivoEmpleados(generarArchivoEmpresas());

	FILE* archivoEmpresas = fopen("EMPRESAS.dat", "r");
	empresa* empresas = leerEmpresa(archivoEmpresas);
	fclose(archivoEmpresas);

	FILE* archivoEmpleados = fopen("EMPLEADOS.dat", "r");
	empleado* empleados = leerEmpleado(archivoEmpleados);
	fclose(archivoEmpleados);

	emitirListado(empresas, empleados);
	liberar(empresas, empleados);

	return 0;
}

/*
1
2
3
4
5
6
7
8
9


13
14
15
*/