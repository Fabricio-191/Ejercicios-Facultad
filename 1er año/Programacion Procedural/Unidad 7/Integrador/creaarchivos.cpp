#include "tipos.h"
void crea(){
	FILE *archi;
	if((archi=fopen("Restaurantes.dat", "wb"))==NULL){
		printf("Error al crear el archivo");
	}
	fclose(archi);
	if((archi=fopen("Clientes.dat", "wb"))==NULL){
		printf("Error al crear el archivo");
	}
	fclose(archi);
	if((archi=fopen("Empleados.dat", "wb"))==NULL){
		printf("Error al crear el archivo");
	}
	fclose(archi);
	printf("Archivos creados\n");
	system("pause");
}
