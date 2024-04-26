#include <stdio.h>
#include <string.h>
#include <malloc.h>

struct terremoto_t{
	char hora[20], tipoMagnitud[10];
	int ano, mes, dia;
	float magnitud, prof, longitud, latitud;
};

float convertirMagnitud(float magnitudMB, float magnitudMS){
	if(magnitudMB > 3.5 && magnitudMB < 6.2){
		return 0.85 * magnitudMB + 1.03;
	}else if(magnitudMS > 3 && magnitudMS < 6){
		return 0.67 * magnitudMS + 2.07;
	}else if(magnitudMS > 6.2 && magnitudMS < 8.2){
		return 0.99 * magnitudMS + 0.08;
	}

	return -1;
}

void guardarTerremoto(FILE* archivo, terremoto_t* terremoto, int &ID){
	fprintf(
		archivo,
		"%d %d %d %d %s %f %f %f %f %s\n",
		ID++,
		terremoto->ano,
		terremoto->mes,
		terremoto->dia,
		terremoto->hora,
		terremoto->latitud,
		terremoto->longitud,
		terremoto->prof,
		terremoto->magnitud,
		terremoto->tipoMagnitud
	);
}

void procesarCatalogos(FILE* destino){
	terremoto_t* temp = (terremoto_t*) malloc(sizeof(terremoto_t));
	char pais[30];
	int ID = 1;
	
	FILE *catalogo = fopen("catalogo1.txt", "r");
	if(catalogo == NULL){
		printf("Ocurrio un error abriendo catalogo1.txt");
		return;
	}
	while(!feof(catalogo)){
		float magnitudMB, magnitudMS;

		fscanf(
			catalogo,
			"%s %d %d %d %s %f %f %f %f %f\n",
			&pais,
			&temp->ano,
			&temp->mes,
			&temp->dia,
			&temp->hora,
			&temp->latitud,
			&temp->longitud,
			&temp->prof,
			&magnitudMB,
			&magnitudMS
		);
		
		temp->magnitud = convertirMagnitud(magnitudMB, magnitudMS);
		strcpy(temp->tipoMagnitud, "mw");

		guardarTerremoto(destino, temp, ID);
	}
	fclose(catalogo);
	
	FILE *catalogo2 = fopen("catalogo2.txt", "r");
	if(catalogo2 == NULL){
		printf("Ocurrio un error abriendo catalogo2.txt");
		return;
	}
	while(!feof(catalogo2)){
		fscanf(
			catalogo2,
			"%d %d %d %s %f %f %f %f %s\n",
			&temp->ano,
			&temp->mes,
			&temp->dia,
			&temp->hora,
			&temp->latitud,
			&temp->longitud,
			&temp->prof,
			&temp->magnitud,
			&temp->tipoMagnitud
		);

		guardarTerremoto(destino, temp, ID);
	}
	fclose(catalogo2);
}

char* leerString(FILE* archivo){
	char str[200];
 	fgets(str, 200, archivo);
	int len = strlen(str);

	if(str[len - 1] == '\n') str[len - 1] = '\0';

	char* string = (char*) malloc(sizeof(char) * len);
	strcpy(string, str); 

	return string;
}

void procesarArchivoUnificado(){
	printf("Introduzca el nombre del archivo ya unificado (catalogosUnificados.txt)\n");
	// catalogosUnificados.txt
	char *filename = leerString(stdin);
	FILE *archivo = fopen(filename, "r"),
		 *destino = fopen("catalogosModificados.txt", "w");

	if(archivo == NULL){
		printf("El archivo %s no pudo ser abierto\n", filename);
		return;
	}

	terremoto_t* temp = (terremoto_t*) malloc(sizeof(terremoto_t));
	int ID;

	while(!feof(archivo)){
		fscanf(
			archivo,
			"%d %d %d %d %s %f %f %f %f %s\n",
			&ID,
			&temp->ano,
			&temp->mes,
			&temp->dia,
			&temp->hora,
			&temp->latitud,
			&temp->longitud,
			&temp->prof,
			&temp->magnitud,
			&temp->tipoMagnitud
		);

		temp->prof = -temp->prof;
		guardarTerremoto(destino, temp, ID);
	}

	fclose(archivo);
	fclose(destino);
	free(filename);
	free(temp);
}

int main(){
	FILE *unificado = fopen("catalogosUnificados.txt", "w");

	procesarCatalogos(unificado);
	fclose(unificado);

	procesarArchivoUnificado();
	
	return 0;
}