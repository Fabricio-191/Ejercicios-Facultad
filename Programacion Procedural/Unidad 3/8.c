/*
Un supermercado ingresa las ventas de los ultimos 6 meses, realizadas en los 8 departamentos de venta que posee.

Por cada venta se ingresa mes (1..12), numero de departamento (1..8) e importe.
Las ventas no traen ningun orden particular.

a) Almacenar la informacion en una tabla que posea por cada mes, el importe total de ventas de cada departamento. La carga finaliza con mes igual a cero.
b) Dado un mes, mostrar en el programa principal el departamento que menos vendio
c) Mostrar importe promedio de venta del supermercado.
d) Dado un mes y un departamento, indicar si supera el importe promedio del item anterior.
*/
#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#define N 12
#define M 8

void cargaAA(float ventas[N][M]){
	srand(time(NULL));

	for (int i = 0; i < 5000; i++) {
		ventas[rand() % N][rand() % M] += (rand() / 32767.0f) * 15;
	}
}

void mostrarTodo(float ventas[N][M]){
	printf("{");
	for (int i = 0; i < N; i++) {
		printf("\n  { ");
		for (int y = 0; y < M - 1; y++) {
			printf("%6.2f, ", ventas[i][y]);
		}
		printf("%6.2f },", ventas[i][M - 1]);
	}
	printf("\n};\n");
}

void cerear(float ventas[N][M]) {
	for (int i = 0; i < N; i++) {
		for (int y = 0; y < M; y++) {
			ventas[i][y] = 0;
		}
	}
}

void cargar(float ventas[N][M]) {
	int	mes, dept;
	float importe;

	printf("Introduzca el mes de la venta (0 para terminar)\n");
	scanf("%i", &mes);
	while (mes != 0) {
		printf("Introduzca el departamento de la venta\n");
		scanf("%i", &dept);

		printf("Introduzca el importe de la venta\n");
		scanf("%f", &importe);

		ventas[mes - 1][dept - 1] += importe;

		printf("Introduzca el mes de la venta (0 para terminar)\n");
		scanf("%i", &mes);
	}
}

void menosVendio(float ventas[N][M]) {
	int mes;

	printf("Introduzca el mes para saber que departamento fue el que menos vendio ese mes\n");
	scanf("%i", &mes);

	int dept = 0;
	int venta = ventas[--mes][0];

	for (int i = 1; i < M; i++) {
		if (ventas[mes][i] < venta) {
			venta = ventas[mes][i];
			dept = i;
		}
	}

	printf("El departamento %i fue el que menos vendio el mes %i\n", dept + 1, mes + 1);
}

float promedioTotal(float ventas[N][M]) {
	float prom = 0;

	for (int i = 0; i < N; i++) {
		for (int y = 0; y < M; y++) {
			prom += ventas[i][y];
		}
	}

	prom /= N * M;

	return prom;
}

void masProm(float ventas[N][M], float prom) {
	int mes, dept;

	printf("Introduzca el mes y departamento\n");
	scanf("%i%i", &mes, &dept);

	if (ventas[mes - 1][dept - 1] > prom) {
		printf("Durante el mes %i el departamento %i supero el promedio de venta\n", mes, dept);
	}else{
		printf("Durante el mes %i el departamento %i no supero el promedio de venta\n", mes, dept);
	}
}

int main() {
	float ventas[N][M];
	cerear(ventas);

	cargar(ventas);
	//cargaAA(ventas);
	mostrarTodo(ventas);

	printf("\n");

	menosVendio(ventas);
	printf("\n");

	float prom = promedioTotal(ventas);
	printf("El importe promedio de venta es: %.2f\n\n", prom);
	masProm(ventas, prom);

	return 0;
}
