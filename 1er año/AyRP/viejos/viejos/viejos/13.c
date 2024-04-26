#include <stdio.h>
#include <stdbool.h>
#define N 15

/*
Carga aleatoria: 

void cargarObleas(int talleres[N]){
	int taller, cantObl;
	
	printf("Introduzca el numero del taller (0 para terminar)\n");
	scanf("%i", &taller);

	while(taller != 0){
		if(taller <= 15 || taller > 0){
			printf("Introduzca la cantidad de obleas emitidas del taller %i\n", taller);
			scanf("%i", &cantObl);

			talleres[taller - 1] = cantObl;

			printf("Introduzca el numero del taller (0 para terminar)\n");
			scanf("%i", &taller);
		}else{
			printf("El taller %d no existe", taller);
		}
	}
}
*/

//Deje la carga ordenada por que es mas facil a la hora de ejecutar el programa
void cargarObleas(int talleres[N]){
	int cantObl;
	
	for(int i = 0; i < N; i++){
		printf("Introduzca la cantidad de obleas emitidas por el taller %i\n", i + 1);
		scanf("%i", &cantObl);

		talleres[i] = cantObl;
	}
}

void selector(int talleres[N]){
	int taller;

	printf("\nEntrando el selector\n\n");

	printf("Introduzca el numero del taller para ver sus obleas\n");
	scanf("%i", &taller);

	while(taller != 0){
		if(taller > N || taller < 0) 
			printf("Ese taller no existe\n\n");
		else 
			printf("El taller %i emitio %i obleas\n\n", taller, talleres[taller - 1]);

		printf("Introduzca el numero del taller para ver sus obleas (0 para terminar)\n");
		scanf("%i", &taller);
	}
}


int valorMin(int talleres[N]){
	int min = talleres[0];

	for(int i = 1; i < N; i++){
		if(talleres[i] < min){
			min = talleres[i];
		}
	}

	return min;
}

void talleresMin(int talleres[N], int min){
	for(int i = 0; i < N; i++){
		if(talleres[i] == min) printf("El taller %i es uno de los que emitio menos obleas\n", i + 1);
	}
}


int valorMax(int talleres[N]){
	int max = talleres[0];

	for(int i = 1; i < N; i++){
		if(talleres[i] > max){
			max = talleres[i];
		}
	}

	return max;
}

void talleresMax(int talleres[N], int max){
	for(int i = 0; i < N; i++){
		if(talleres[i] == max){
			printf("El taller %d es uno de los que emitio mas obleas\n", i + 1);
		}
	}
}


void obleasTotales(int talleres[N]){
	int obleasTotales = 0;

	for(int i = 0; i < N; i++){
		obleasTotales += talleres[i];
	}

	printf("Se emitio un total de %d obleas\n", obleasTotales);
}

void mas500(int talleres[N]){
	bool bandera = false;

	for(int i = 0; i < N; i++){
		if(talleres[i] > 500) bandera = true;
	}

	if(bandera) printf("Hay un taller que emitio mas de 500 obleas\n");
}


int main(){
	int talleres[N];

	cargarObleas(talleres);

	printf("\n");

	talleresMin(talleres, valorMin(talleres));
	talleresMax(talleres, valorMax(talleres));
	obleasTotales(talleres);
	mas500(talleres);

	selector(talleres);

	return 0;
}