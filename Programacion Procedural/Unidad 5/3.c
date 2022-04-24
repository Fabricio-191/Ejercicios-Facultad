/*
Ejercicio 3

El Instituto Provincial de la Vivienda ha implementado un sistema que consta de 5 planes de pago distintos, con el fin de que los adjudicatarios de sus viviendas puedan cancelar sus deudas.
Por cada uno de los 5 planes, se ingresa en forma ordenada la cantidad de adjudicatarios adheridos y por cada uno de ellos el DNI y monto adeudado.

a) Cargar en una estructura de datos adecuada la información que se posee.
b) Para un adjudicatario cuyo DNI se ingresa por teclado, indicar el número de plan al cual se adhirió y el monto adeudado.
c) Mostrar el mapa de memoria, después de ejecutar la función que carga los datos.
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <malloc.h>
#define strLen 15
const int N = 5;

typedef struct {
	char DNI[strLen];
	float deuda;
} deudor;

typedef struct {
	int conteo;
	deudor *deudores;
} plan;

void carga(plan planes[N]){
	int cant;

	for(int i = 0; i < N; i++){
		printf("Introduzca la cantidad de adjudicatarios en el plan \e[31m%d\e[33m\n", i + 1);
		scanf("%i", &cant);
		printf("\e[0m");

		if(cant < 1){
			planes[i].conteo = 0;
			planes[i].deudores = NULL;
			continue;
		}

		deudor *deudores = (deudor*) malloc(sizeof(deudor) * cant);
		planes[i].conteo = cant;
		planes[i].deudores = deudores;

		for(int x = 0; x < cant; x++){
			printf("Introduzca el DNI del adjudicatario\n\e[32m");
			scanf("%s", deudores[x].DNI);
			printf("\e[0mIntroduzca el monto adeudado\n\e[33m");
			scanf("%f", &deudores[x].deuda);
			printf("\e[0m");
		}
	}
}

void mostrar(plan planes[N]){
	for(int i = 0; i < N; i++){
		int deudores = planes[i].conteo;
		if(deudores != 0) printf("\n Adjudicatarios del plan \e[31m%d\e[0m\n", i + 1);
		for(int x = 0; x < deudores; x++){
			printf("{ DNI: \e[32m\"%s\"\e[0m, deuda: \e[33m%.2f\e[0m }\n", planes[i].deudores[x].DNI, planes[i].deudores[x].deuda);
		}
	}
}

void encontrarDNI(plan planes[N]){
	char DNI[strLen];
	printf("\nIntroduzca el DNI a buscar\n\e[32m");
	scanf("%s", DNI);
	printf("\e[0m");

	for(int i = 0; i < N; i++){
		int deudores = planes[i].conteo;
		for(int x = 0; x < deudores; x++){
			if(strcmp(planes[i].deudores[x].DNI, DNI) == 0){
				printf(
					"El adjudicatario con el DNI: \e[32m%s\e[0m\n  Adeuda: \e[33m%.2f\e[0m\n  Plan: \e[31m%i\e[0m\n",
					DNI, planes[i].deudores[x].deuda, i + 1
				);
				return;
			}
		}
	}

	for(int i = 0; i < N; i++){
		int deudores = planes[i].conteo;
		for(int x = 0; x < deudores; x++){
			if(strcmp(planes[i].deudores[x].DNI, DNI) == 0){
				printf(
					"El adjudicatario con el DNI: \e[32m%s\e[0m\n  Adeuda: \e[33m%.2f\e[0m\n  Plan: \e[31m%i\e[0m\n",
					DNI, planes[i].deudores[x].deuda, i + 1
				);
				return;
			}
		}
	}


	printf("No existe ningun adjudicatario con el DNI: \e[32m%s\e[0m\n", DNI);
}

void liberar(plan planes[N]){
	for(int i = 0; i < N; i++){
		free(planes[i].deudores);
	}
}

int main(){
	printf("\e[0m");
	plan planes[N];

	carga(planes);
	mostrar(planes);
	encontrarDNI(planes);

	liberar(planes);
	printf("\e[0m");
}

/* para copiar y pegar
2
3.893.112
893426.94
38.483.292
625183.94
3
85.662.050
434554.72
45.397.995
466320.69
15.558.678
9119.35
0
4
3.084.401
691675.31
11.288.439
820230.75
31.445.992
381362.94
64.086.691
389123.56
4
82.002.921
187959.05
47.619.664
234798.98
66.844.016
112845.10
60.967.402
953235.19

*/