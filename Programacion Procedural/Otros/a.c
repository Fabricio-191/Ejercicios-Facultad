#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

#define LINE_LENGTH 7
#define MAX_ARTICULOS 100

typedef struct {
	int orden, anio;
	float costo, precioVenta;
	char ID[7];
	char descripcion[20];
	char tipo[15];
} Articulo;

int datosValidos(char* datos[LINE_LENGTH]){
	for(int i = 0; i < LINE_LENGTH; i++){
		if(datos[i] == NULL || datos[i][0] == '\0') return 0;
	}

	return 1;
}

int leerArchivo(Articulo* articulos, FILE* archivo){
	char line[200];
	fgets(line, 200, archivo); // para que no lea la primera linea
	int cant = 0;

	while(!feof(archivo)){
		fgets(line, 200, archivo);
		
		char* datos[LINE_LENGTH] = {
			strtok(line, ";"),
			strtok(NULL, ";"),
			strtok(NULL, ";"),
			strtok(NULL, ";"),
			strtok(NULL, ";"),
			strtok(NULL, ";"),
			strtok(NULL, ";")
		};

		if(datosValidos(datos)){
			articulos[cant].orden 		= atoi(	datos[0]);
			strcpy(articulos[cant].ID, 			datos[1]);
			strcpy(articulos[cant].descripcion, datos[2]);
			articulos[cant].costo 		= atof(	datos[3]);
			strcpy(articulos[cant].tipo, 		datos[4]);
			articulos[cant].anio 		= atoi(	datos[5]);
			articulos[cant].precioVenta = atof(	datos[6]);
			cant++;
		}
	}

	return cant;
}

void mostrarArticulos(Articulo* articulos, int cant){
	for(int i = 0; i < cant; i++){
		printf("Orden: %d\n", articulos[i].orden);
		printf("ID Articulo: %s\n", articulos[i].ID);
		printf("Descripcion: %s\n", articulos[i].descripcion);
		printf("Costo: %.2f\n", articulos[i].costo);
		printf("Tipo: %s\n", articulos[i].tipo);
		printf("Anio: %d\n", articulos[i].anio);
		printf("Precio venta: %.2f\n\n", articulos[i].precioVenta);
	}
}

int main(){
	FILE* archivo = fopen("articulos.csv", "r");

	if(archivo == NULL) {
		printf("No fue posible abrir el archivo\n");
		return -1;
	}

	Articulo articulos[MAX_ARTICULOS];
	int cant = leerArchivo(articulos, archivo);
	fclose(archivo);
	
	mostrarArticulos(articulos, cant);

	return 0;
}
