/*
Una consultora contable realiza la liquidación de haberes de los empleados de varias PYMES.
Para ello posee un archivo con información de empleados “EMPLEADOS.dat” de diferentes empresas: Nombre del Empleado, Nombre de la Empresa, DNI, CUIT y sueldo neto. El archivo está ordenado por nombre de empresa.

a) Emita un listado ordenado por empresa con la liquidación de haberes de cada empleado. Además, el listado debe incluir el total a pagar en concepto de sueldo por cada empresa.
b) Generar el archivo “EMPRESAS.dat” que almacena para cada empresa la siguiente información: Nombre, total de empleados, total pagado en concepto de liquidación.
*/
#include <stdio.h>
#include <string.h>
#include <malloc.h>

struct empleado_t{
	char DNI[15], CUIT[15], nombre[50], empresa[50];
	float sueldo;
};

int leerEmpleados(FILE* archivo, empleado_t* &empleados){
	fpos_t size;
	fseek(archivo, 0, SEEK_END);
	fgetpos(archivo, &size);

	int cant = size / sizeof(empleado_t);

	empleados = (empleado_t*) malloc(sizeof(empleado_t) * cant);
	fread(empleados, sizeof(empleado_t), cant, archivo);

	return cant;
}

struct empresa_t{
	char nombre[50];
	float totalPagado;
	int cantEmpleados;
	empleado_t* empleados;
	empresa_t* next;
};

empresa_t* leerEmpresa(empleado_t* empleados, int i, int cant){
	if(i == cant) return NULL;

	empresa_t* empresa = (empresa_t*) malloc(sizeof(empresa_t));
	strcpy(empresa->nombre, empleados[i].empresa);
	empresa->totalPagado = 0;
	empresa->cantEmpleados = 0;
	empresa->empleados = NULL;

	while(stricmp(empleados[i].empresa, empresa->nombre) == 0){
		empresa->cantEmpleados++;
		empresa->totalPagado += empleados[i].sueldo;

		if(++i == cant) break;
	}

	empresa->next = leerEmpresa(empleados, i, cant);
}

int main(){
	FILE* archivo = fopen("EMPLEADOS.dat", "r");
	if(archivo == NULL){
		printf("El archivo EMPLEADOS.dat no pudo ser abierto\n");
		return -1;
	}

	empleado_t* empleados = NULL;
	int empleadosTotales = leerEmpleados(archivo, empleados);
	fclose(archivo);

	empresa_t* empresas = leerEmpresa(empleados, 0, empleadosTotales);



	return 0;
}