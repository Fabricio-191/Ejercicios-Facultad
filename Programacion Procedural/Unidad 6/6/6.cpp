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
	char *DNI, *CUIT, *nombre, *empresa;
	float sueldo;
	empleado_t* next;
};

struct empresa_t{
	char* nombre;
	float totalPagado;
	int cantEmpleados;
	empleado_t* empleados;
	empresa_t* next;
};

// https://en.cppreference.com/w/c/io/fscanf
// https://en.cppreference.com/w/c/io/vfscanf
// https://en.cppreference.com/w/c/experimental/dynamic/getline
char* leerString(FILE* archivo){
	char str[200];
 	fgets(str, 200, archivo);

	int len = strlen(str);
	str[len - 1] = '\0';

	char* string = (char*) malloc(sizeof(char) * len);
	strcpy(string, str); 

	return string;
}

empleado_t* leerEmpleado(FILE* archivo){
	if(feof(archivo)) return NULL;
	empleado_t* empleado = (empleado_t*) malloc(sizeof(empleado_t));

	empleado->nombre = leerString(archivo);
	empleado->empresa = leerString(archivo);
	empleado->DNI = leerString(archivo);
	empleado->CUIT = leerString(archivo);
	fscanf(archivo, "%f\n\n", &empleado->sueldo);

	return empleado;
}

empresa_t* leerEmpresa(FILE* archivo, empleado_t* empleado){
	if(empleado == NULL) return NULL;

	empresa_t* empresa = (empresa_t*) malloc(sizeof(empresa_t));
	empresa->nombre = empleado->empresa;
	empresa->cantEmpleados = 0;
	empresa->totalPagado = 0;
	empresa->empleados = NULL;

	while(
		empleado != NULL &&
		stricmp(empleado->empresa, empresa->nombre) == 0
	){
		empresa->cantEmpleados++;
		empresa->totalPagado += empleado->sueldo;

		empleado->next = empresa->empleados;
		empresa->empleados = empleado;

		empleado = leerEmpleado(archivo);
	}

	empresa->next = leerEmpresa(archivo, empleado);

	return empresa;
}

void emitirListado(empresa_t* nodo){
	empleado_t* temp;
	printf("******************* LISTADO DE LIQUIDACION *********************\n");

	while(nodo != NULL){
		int i = 1;
		printf("\nLista de empleados de %s\n", nodo->nombre);
		printf("		DNI 			Nombre 			Sueldo\n");
		
		temp = nodo->empleados;
		while(temp != NULL){
			printf("%d		%s 		%s 		$ %.2f\n", i++, temp->DNI, temp->nombre, temp->sueldo);
			temp = temp->next;
		}

		printf("Total pagado por %s es $ %.2f\n", nodo->nombre, nodo->totalPagado);
		nodo = nodo->next;
	}
}

void generarArchivo(empresa_t* nodo){
	FILE* archivo = fopen("EMPRESAS.dat", "w");

	while(nodo != NULL){
		fprintf(archivo, "Nombre de la empresa: %s\n", nodo->nombre);
		fprintf(archivo, "Empleados: %d\n", nodo->cantEmpleados);
		fprintf(archivo, "Total pagado: $ %.2f\n\n", nodo->totalPagado);
		nodo = nodo->next;
	}

	fclose(archivo);
}

void liberar(empresa_t* empresa, empleado_t* empleado){
	if(empresa == NULL) return;
	if(empleado != NULL){
		liberar(empresa, empleado->next);
		free(empleado->nombre);
		free(empleado->CUIT);
		free(empleado->DNI);
		free(empleado->empresa);
		free(empleado);
	}else{
		liberar(empresa->next, NULL);
		free(empresa);
	}
}

int main(){
	FILE* archivo = fopen("EMPLEADOS.txt", "r");
	if(archivo == NULL){
		printf("El archivo EMPLEADOS.txt no pudo ser abierto\n");
		return -1;
	}

	empresa_t* cabeza = leerEmpresa(archivo, leerEmpleado(archivo));
	fclose(archivo);

	emitirListado(cabeza);
	generarArchivo(cabeza);

	liberar(cabeza, NULL);
	return 0;
}