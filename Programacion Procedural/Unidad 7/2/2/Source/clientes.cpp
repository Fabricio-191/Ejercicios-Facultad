#include "header.h"
#include <stdio.h>
#include <string.h>
#include <malloc.h>
const char* ruta = "../Archivos/CLIENTES.dat";
/*
Clientes
Los datos de los clientes se almacenan en un archivo llamado “Clientes.dat”. Al momento de hacerse un pedido,
si el cliente no está registrado, se le da de alta en el archivo. Observación: cada Cliente tiene un código de identificación
(ID del cliente) que comienza a partir de 100 que se genera automáticamente y permite acceso directo a su
información.

struct cliente {
	char nombre[50], direccion[50], telefono[30];
	int ID, cupon;
};
*/

int cantClientes() {
	fpos_t size;
	FILE* archivo = fopen(ruta, "r");

	fseek(archivo, 0, SEEK_END);
	fgetpos(archivo, &size);
	fclose(archivo);

	return size / sizeof(cliente);
}

int estaRegistrado(char* nombre){
	FILE* archivo = fopen(ruta, "r");

	cliente c;
	while(!feof(archivo)) {
		fread(&c, sizeof(cliente), 1, archivo);
		if(stricmp(nombre, c.nombre)) return 1;
	}

	return 0;
}

void agregarCliente(char* nombre) {
	FILE* archivo = fopen(ruta, "w+");

	cliente c;
	printf("Introduzca la direccion, telefono y cupon del cliente\n");
	strcpy(c.nombre, nombre);
	fgets(c.direccion, 50, stdin);
	fgets(c.telefono, 30, stdin);
	c.ID = cantClientes() + 100;
	scanf("%d", &c.cupon);

	fwrite(&c, sizeof(cliente), 1, archivo);
}

void eliminarCliente(int &cant) {
	int ID;
	printf("Introduzca la ID del cliente a eliminar\n");
	scanf("%d", &ID);

	FILE* archivo = fopen(ruta, "rw");

	cliente* c;
	fread(c, sizeof(cliente), cant, archivo);
	rewind(archivo);

	int total = cant;
	for(int i = 0; i < total; i++){
		if(c[i].ID == ID){
			cant--;
			continue;
		}
		fwrite(&c[i], sizeof(cliente), 1, archivo);
	}
}



void eliminarCliente(int &cant) {
	int ID;
	printf("Introduzca el nombre del cliente a eliminar\n");
	scanf("%d", &ID);
	//se leyo la ID del cliente a eliminar

	//se abre el archivo en modo de lectura
	FILE* archivo = fopen("../Archivos/CLIENTES.dat", "r");
	cliente* c;
	//se pone en un arreglo dinamico a todos los clientes en el archivo
	fread(c, sizeof(cliente), cant, archivo);
	//se cierra el archivo
	fclose(archivo);

	//se reabre el archivo en modo lectura, como el archivo ya existe, se sobreescribe, quedando un archivo vacio donde escribir
	archivo = fopen("../Archivos/CLIENTES.dat", "w");
	//se recorre el arreglo y en el archivo vacio se ponen los clientes que no tengan esa ID
	int total = cant;
	for(int i = 0; i < total; i++){
		if(c[i].ID != ID){
			fwrite(&c[i], sizeof(cliente), 1, archivo);
		}else cant--;
	}

	free(c);
	fclose(archivo);
}
