#include "header.h"
#include <stdio.h>
#include <malloc.h>
const char* ruta = "../Archivos/RESTAURANTES.dat";
/*
Restaurantes
Los datos de los restaurantes asociados a la plataforma se almacenan en un archivo denominado
“Restaurantes.dat”, para una manipulación más ágil de los datos a diario se crea un arreglo con la información del
archivo. Estas estructuras se actualizan cada vez que se da de alta o baja a un restaurante. Observación: un restaurante
comienza a operar desde el momento en que es cargado en el archivo Restaurates.dat. Cada restaurante tiene un
código de identificación (ID del restaurante) que comienza a partir de 1 y se genera automáticamente, permitiendo
acceso directo a su información. Para la actividad diaria de la plataforma, en el arreglo de restaurantes, a cada
componente se le agrega un campo que registra cantidad de pedidos a entregar y otro que acumula los importes de
los pedidos realizados.

struct restaurante {
	char nombre[50], direccion[50], telefono[30];
	int ID, pedidos, tipoEntrega, medioPago;
	float montoAcumulado;
};
*/

static void actualizarArchivo(restaurante* res, int cant) {
	FILE* archivo = fopen(ruta, "w");
	fwrite(res, sizeof(restaurante), cant, archivo);
}

int leerRestaurantes(restaurante* &res) {
	fpos_t size;
	FILE* archivo = fopen(ruta, "r");

	fseek(archivo, 0, SEEK_END);
	fgetpos(archivo, &size);

	res = (restaurante*) malloc(size);

	int cant = size / sizeof(restaurante);
	fread(res, sizeof(restaurante), cant, archivo);

	return cant;
}

void agregarRestaurante(restaurante* &res, int &cant) {
	res = (restaurante*) realloc(res, sizeof(restaurante) * (cant + 1));

	printf("Introduzca los datos del nuevo restaurante\n");
	fgets(res[cant].nombre, 50, stdin);
	fgets(res[cant].direccion, 50, stdin);
	fgets(res[cant].telefono, 30, stdin);
	res[cant].ID = cant + 1;
	res[cant].pedidos = 0;
	res[cant].montoAcumulado = 0;
	scanf("%d", &res[cant].tipoEntrega);
	scanf("%d", &res[cant].medioPago);

	actualizarArchivo(res, ++cant);
}

void eliminarRestaurante(restaurante* &res, int &cant) {
	int ID;
	printf("Introduzca la ID de restaurante a eliminar\n");
	scanf("%d", &ID);

	restaurante* resNuevo = (restaurante*) malloc(sizeof(restaurante) * (cant - 1));
	int y = 0;
	for (int i = 0; i < cant; i++) {
		if (res[i].ID == ID) continue;

		resNuevo[y++] = res[i];
	}

	actualizarArchivo(res, --cant);
}