/*
La cadena de comidas rápidas Mostaza necesita información estratégica que permita apoyar la toma de decisiones en
relación a las ventas realizadas en cada una de las 4 sucursales que dispone en la ciudad Autónoma de Buenos Aires.

De cada sucursal se conoce: número, nombre, dirección y teléfono. 
En cuanto a los 10 productos distintos que comercializa, se conoce: código de producto, nombre, calorías y precio. 
Por cada venta realizada, se ingresa el número de sucursal, código de producto y cantidad.

Esta información no tiene ningún orden en particular, y el ingreso termina con número de sucursal 0.

Concretamente necesita conocer:
a) Cantidad de productos vendidos por sucursal.
b) Importe total de productos vendidos por sucursal.
c) Obtener la sucursal (nombre) y el producto (nombre y precio), que registró el mayor importe de venta.
d) Dado un número de sucursal, indicar el producto (todos los datos) que registró el mayor consumo de calorías (suponer único).
e) Dado un número de producto, indicar la sucursal (nombre y teléfono) donde se registró el menor importe vendido
*/
#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#define N 4
#define M 10
#define strLen 30

typedef struct {
	char direccion[strLen];
	char nombre[strLen];
	char telefono[strLen];
	int ventas[M];
} sucursal;

typedef struct {
	int codigo, calorias;
	char nombre[strLen];
	float precio;
} producto;

void cargaSucursales(sucursal sucursales[N], int i){
	//número, nombre, dirección y teléfono
	if(i == N) return;

	printf("Introduzca el nombre, direccion y telefono de la sucursal numero %i\n", i + 1);
	scanf("%s%s%s", sucursales[i].nombre, sucursales[i].direccion, sucursales[i].telefono);

	cargaSucursales(sucursales, i + 1);
}

void cargaProductos(producto productos[M], int i){
	//código de producto, nombre, calorías y precio
	if(i == M) return;

	printf("Introduzca el nombre, calorias y precio del producto numero %i\n", i + 1);
	scanf("%s%i%f", productos[i].nombre, productos[i].calorias, productos[i].precio);

	cargaProductos(productos, i + 1);
}

void cerearVentas(sucursal sucursales[N]){
	for(int i = 0; i < N; i++){
		for(int x = 0; x < M; x++){
			sucursales[i].ventas[x] = 0;
		}
	}
}

void cargaVentas(sucursal sucursales[N]){
	// Por cada venta realizada, se ingresa el número de sucursal, código de producto y cantidad.
	int sucursal, codigoProd, cantidad;

	printf("Introduzca el numero de sucursal (0 para terminar la carga)\n");
	scanf("%i", &sucursal);

	if(sucursal == 0) return;
	
	printf("Introduzca el codigo de producto y la cantidad comprada\n");
	scanf("%i%i", &codigoProd, &cantidad);

	sucursales[sucursal - 1].ventas[codigoProd - 1] += cantidad;

	cargaVentas(sucursales);
}

int main(){
	sucursal sucursales[N];
	producto productos[M];

	cargaSucursales(sucursales, 0);
	cargaProductos(productos, 0);
	cerearVentas(sucursales);
	cargaVentas(sucursales);
}
