#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#define N 5
#define strLen 50

void ordenar1(int arreglo[N]){ //metodo burbuja mejorado
	int k = 1, i, aux, cota = N - 1;

	while(k != -1){
		k = -1;

		for(i = 0; i < cota; i++){
			if(arreglo[i] > arreglo[i + 1]){ //ascendente
				aux = arreglo[i];
				arreglo[i] = arreglo[i + 1];
				arreglo[i + 1] = aux;
				k = i;
			}
		}

		cota = k;
	}
}

void ordenar2(int arreglo[N]){ //metodo seleccion
	int i, j, min, aux;

	for(i = 0; i < (N - 1); i++){
		min = i;
		for(j = (i + 1); j < N; j++){
			if(arreglo[j] < arreglo[min]) min = j; //ascendente
		}

		aux = arreglo[i];
		arreglo[i] = arreglo[min];
		arreglo[min] = aux;
	}
	return;
}

void ordenar3(int arreglo[N]){ //metodo insercion
	int i, j, valor;

	for(i = 1; i < N; i++){
		valor = arreglo[i];
		j = i - 1;
		while((j >= 0) && (valor < arreglo[j])){//ascendente
			arreglo[j+1] = arreglo[j];
			j--;
		}
		arreglo[j+1] = valor;
	}
}

int buscar1(int arreglo[N], int elem){ //Busqueda sin bandera
	int i = 0;

	while((i < N) && (arreglo[i] != elem)) i++;

	return i;
}

int buscar2(int arreglo[N], int elem){ //Busqueda con bandera
	int i = 0;
	bool encontro = false;

	while((i < N) && (!encontro)){
		if(arreglo[i] == elem){
			encontro = true;
		}else i++;
	}

	return i;
}

int buscar3(int arreglo[N+1], int elem){ //Busqueda con elemento sentinela
	int i = 0;
	arreglo[N] = elem;

	while (arreglo[i] != elem) i++;
	return i;
}

int buscar4(int arreglo[N], int elem){ //Busqueda binaria (no secuencial)
	int inf = 0, sup = N - 1, medio = (inf + sup) / 2;

	while ((inf <= sup) && (elem != arreglo[medio])){
		if(elem < arreglo[medio]){
			sup = medio - 1;
		}else inf = medio + 1;
		medio = (inf + sup) / 2;
	}

	if (inf > sup) medio = -1;

	return medio;
}

//https://es.stackoverflow.com/questions/31601/guardar-cadena-de-caracteres-en-c

void removeNewline(char* string){
	char* pos = strchr(string, '\n');
	//strchr recorre la primera string hasta que encuentra el caracter
	//y devuelve la posicion (puntero) donde ocurrio la coincidencia
	if (pos != NULL) *pos = '\0';//Si el puntero no es nulo (hay una coincidencia), lo reemplaza por un caracter nulo, cortando la string y haciendo que termine ahi
	//Si una string toma el salto de linea (\n) usando el fgets, esta funcion lo reemplaza
}

void leerCadena(char* string){
	fflush(stdin);
	fgets(string, strLen, stdin);

	char* pos = strchr(string, '\n');
	if (pos != NULL) *pos = '\0';
}

int main(){
	char cadena[strLen];

	printf("Introduzca la cadena\n");
	leerCadena(cadena);

	printf("Cadena recibida: \"%s\"", cadena);

	return 0;
}


void cadenas(){
	// char* cadena = "abc";
	// char cadena[] = "def";
	char cadena1[50];
	char cadena2[50];
	char cadenaFinal[50];
	
	printf("Introduzca la cadena:\n");
	// scanf("%s", cadena1);
	fgets(cadena1, 50, stdin);
	removeNewline(cadena1);
	
	printf("strlen(\"%s\") => %i\n", cadena1, strlen(cadena1));

	strcpy(cadenaFinal, cadena1); //cadenaFinal = cadena1

	printf("Introduzca la cadena a agregar:\n");
	//scanf("%s", cadena2);
	fgets(cadena2, 50, stdin);
	removeNewline(cadena2);

	strcat(cadenaFinal, cadena2);

	printf("strcat(\"%s\", \"%s\") => \"%s\"", cadena1, cadena2, cadenaFinal);

	/*
	int len = strlen(cadena); //(la longitud de la cadena sin el caracter final 0)

	strcpy(cadenaDestino, cadena); //Copia el contenido de <cadena> en <cadenaDestino>.
	strcat(cadenaDestino, cadena); //cadenaDestino += cadena

	strcmp(cadena, cadena2); //Compara las dos cadenas y:
		Devuelve un 0 si las dos cadenas son iguales
		Un número negativo si <cadena1> es menor que (precede alfabéticamente a) <cadena2> 
		Un número positivo (mayor que cero) si <cadena1> es mayor que <cadena2>.
	*/
}
