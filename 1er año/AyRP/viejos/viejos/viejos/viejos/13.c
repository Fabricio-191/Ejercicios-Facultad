#include <stdio.h>
#include <stdbool.h>

void cargarObleas(int talleres[15]){
	int cantObl;
	
	for(int taller = 1; taller <= 15; taller++){
		printf("Introduzca la cantidad de obleas emitidas por el taller %i\n", taller);
		scanf("%i", &cantObl);

		talleres[taller - 1] = cantObl;
	}
}

void selector(int talleres[15]){
	int taller;

	printf("\nEntrando el selector\n\n");

	printf("Introduzca el numero del taller para ver sus obleas\n");
	scanf("%i", &taller);

	while(taller != 0){
		if(taller > 15 || taller < 0) 
			printf("Ese taller no existe\n\n");
		else 
			printf("El taller %i emitio %i obleas\n\n", taller, talleres[taller - 1]);

		printf("Introduzca el numero del taller para ver sus obleas (0 para terminar)\n");
		scanf("%i", &taller);
	}
}

int main(){
	bool MAS_500 = false;
	int talleres[15], obleasTotales = 0, 
		MIN_obleas = 100000, MIN_taller,
		MAX_obleas = 0, MAX_taller;

	cargarObleas(talleres);

	for(int taller = 1; taller <= 15; taller++){
		int cantObl = talleres[taller - 1];
		obleasTotales += cantObl;

		if(cantObl < MIN_obleas){
			MIN_obleas = cantObl;
			MIN_taller = taller;
		}
		if(cantObl > MAX_obleas){
			MAX_obleas = cantObl;
			MAX_taller = taller;
		}

		if(cantObl > 500) MAS_500 = true;
	}

	printf("La cantidad total de obleas emitidas fue: %i\n", obleasTotales);
	printf("El taller que menos obleas emitio es el: %i\n", MIN_taller);
	printf("El taller que mas obleas emitio es el: %i\n", MAX_taller);
	if(MAS_500) printf("Hay un taller que emitio mas de 500 obleas\n");
	
	selector(talleres);

	return 0;
}

/*
void cargarObleas(int talleres[15]){
	int taller, cantObl;
	
	printf("Introduzca el numero del taller (0 para terminar)\n");
	scanf("%i", &taller);

	while(taller != 0){
		printf("Introduzca la cantidad de obleas emitidas del taller %i\n", taller);
		scanf("%i", &cantObl);

		talleres[taller] = cantObl;

		printf("Introduzca el numero del taller (0 para terminar)\n");
		scanf("%i", &taller);
	}
}
*/