#include <stdio.h>
#include <string.h>
#include <malloc.h>
/*
Codificar un programa en C que permita leer un archivo de caracteres cualesquiera e indique cuál de las cinco vocales
del abecedario tiene mayor frecuencia. Realice un menú de opciones que permita leer:
a) Archivo de caracteres con extensión. cpp
b) Archivo de caracteres con extensión. dat
c) Archivo de caracteres con extensión. txt
*/

const char vocales[6] = "aeiou";

int numVocal(char c){
	switch(c){
		case 'a': return 0;
		case 'e': return 1;
		case 'i': return 2;
		case 'o': return 3;
		case 'u': return 4;
		default: return -1;
	}
}

int* contarVocales(char* filename, int vocales[5]){
	FILE* archivo = fopen(filename, "r");
	if(archivo == NULL){
		printf("No se pudo abrir el archivo %s\n", filename);;
		return NULL;
	}

	int i;
	char c = fgetc(archivo);
	while(c != EOF){
		i = numVocal(c);
		if(i != -1){
			vocales[i]++;
		}

		c = fgetc(archivo);
	}

	fclose(archivo);
	return vocales;
}

void mostrarVocales(int* v, char* filename){
	printf("\nVocales del archivo %s\n", filename);
	for(int i = 0; i < 5; i++){
		printf("Repeticiones de %c: %d\n", vocales[i], v[i]);
	}
}

char* leerString(){
	char str[200];
 	fgets(str, 200, stdin);

	int len = strlen(str);
	str[len - 1] = '\0';

	char* string = (char*) malloc(sizeof(char) * len);
	strcpy(string, str); 

	return string;
}

int main(){
	int vocales[5] = { 0, 0, 0, 0, 0 };
	printf("Introduzca el nombre del archivo donde contar vocales (fin para terminar)\n");
	char* filename = leerString();

	while(stricmp(filename, "fin") != 0){
		contarVocales(filename, vocales);
		if(vocales != NULL){
			mostrarVocales(vocales, filename);
		}
		
		printf("\nIntroduzca el nombre del archivo donde contar vocales (fin para terminar)\n");
		filename = leerString();
	}

	free(filename);
	return 0;
}