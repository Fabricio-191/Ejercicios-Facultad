/*
Una empresa comercializa 34 productos (1..34) de plástico en sus 8 sucursales.
De cada sucursal registra para cada uno de sus 34 productos la cantidad de unidades vendidas en el mes de Julio.

1. Almacene en una tabla el total la información de cada producto por sucursal (cada fila debe representar un producto).
2. Indicar la cantidad total de ventas para el producto 25, decir si alguna sucursal no tuvo ventas del mismo y cuantas sucursales vendieron más de 100. (hacer una función que devuelva los tres resultados).
3. Decir cuántos productos vendió cada sucursal.
Nota: hacer al menos una función recursiva.
*/
#include <stdio.h>
#define N 34
#define M 8

void cerear(int ventas[N][M]){
	for(int i = 0; i < N; i++){
		for(int j = 0; j < M; j++){
			ventas[i][j] = 0;
		}
	}
}

void carga(int ventas[N][M], int n, int m){
	if(m == M){ m = 0; n++; }
	if(n == N) return;

	int num;
	printf("Introduzca la cantidad de ventas del producto %i de la sucursal %i.\n", m + 1, n + 1);
	scanf("%i", &num);
	ventas[m][n] = num;
	
	carga(ventas, n, m + 1);
}

void producto25(int ventas[M], int *ventasTotales, int *noVentas, int *mas100){
	for(int i = 0; i < M; i++){
		*ventasTotales += ventas[i];
		if(ventas[i] == 0) *noVentas = 1;
		if(ventas[i] > 100) (*mas100)++;
	}
}

void productosPorSucursal(int ventas[N][M]){
	for(int j = 0; j < M; j++){
		int t = 0;
		for(int i = 0; i < N; i++){
			t += ventas[i][j];
		}

		printf("La sucursal %i vendio %i productos en total\n", j + 1, t);
	}
}

int main(){
	int ventas[N][M];

	cerear(ventas);
	carga(ventas, 0, 0);

	int mas100 = 0, noVentas = 0, ventasTotales = 0;
	producto25(ventas[24], &ventasTotales, &noVentas, &mas100);

	printf("El total de ventas del producto 25 fue %i\n", ventasTotales);
	printf("Hubo %i sucursales que vendieron mas de 100\n", mas100);
	if(noVentas == 1) printf("Hubo una sucursal que no vendio el producto 25\n");

	productosPorSucursal(ventas);
}
