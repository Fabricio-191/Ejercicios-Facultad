/*
Ejercicio 10
Una fábrica de ropa comercializa 50 prendas que son vendidas a 35 comercios del país.

Por cada venta realizada se cuenta con los siguientes datos: Código de comercio (60..94), Nombre de la prenda vendida y cantidad de unidades.
Las ventas no traen ningún orden en particular.
En una estructura se registra por cada prenda que se comercializa su nombre y precio unitario, ordenado alfabéticamente.
Además, por cada comercio se almacena su CUIL y Nombre.

Se pide realizar un programa en C, que utilizando funciones óptimas y estructuras adecuadas permita (utilizar Menú de opciones):

a) Almacenar los datos de las ventas en una estructura que posea por cada comercio la cantidad de unidades vendidas de cada prenda.
b) Indicar por cada comercio; CUIL, Nombre e importe total a pagar.
c) Realizar un listado que contenga por cada producto, nombre y cantidad de unidades vendidas, este listado debe estar ordenado descendentemente por cantidad de unidades.
d) Mostrar el nombre de los 5 productos que más se vendieron.
*/
#include <stdio.h>
#include <string.h>
#define N 5 //50
#define M 3 //35
#define strLen 20

typedef struct {
	char nombre[strLen];
	float precio;
} prenda;

// a) Almacenar los datos de las ventas en una estructura que posea por cada comercio la cantidad de unidades vendidas de cada prenda.
typedef struct {
	char CUIL[strLen];
	char nombre[strLen];
	int ventas[N];
} comercio;

typedef struct {
	char nombre[strLen];
	int ventas;
} producto;

void leerCadena(char* str){
	fflush(stdin);
	fgets(str, strLen, stdin);

	char* pos = strchr(str, '\n');
	if (pos != NULL) *pos = '\0';
}

void cargarPrendas(prenda prendas[N]){
	for(int i = 0; i < N; i++){
		printf("Introduzca el nombre y luego precio de la prenda %i\n", i + 1);
		leerCadena(prendas[i].nombre);
		scanf("%f", &prendas[i].precio);
	}
}

void ordenarPorNombre(prenda prendas[N]){
	prenda aux;
	int result, fin = N - 1;
	for(int i = 0; i < N; i++){
		for(int i = 0; i < fin; i++){
			if(strcmp(prendas[i].nombre, prendas[i + 1].nombre) == 1){
				aux = prendas[i];
				prendas[i] = prendas[i + 1];
				prendas[i + 1] = aux;
			}
		}

		fin--;
	}
}

void cargarComercios(comercio comercios[M]){
	for(int i = 0; i < M; i++){
		printf("Introduzca el nombre y CUIL del comercio %i\n", i + 60);
		leerCadena(comercios[i].nombre);
		leerCadena(comercios[i].CUIL);
	}
}

void cerearVentasComercios(comercio comercios[M]){
	for(int i = 0; i < M; i++){
		for(int x = 0; x < N; x++){
			comercios[i].ventas[x] = 0;
		}
	}
}

int encontrar(prenda prendas[N], char nombre[strLen]){
	int inf = 0, sup = N - 1, medio = (inf + sup) / 2;

	int res = strcmp(nombre, prendas[medio].nombre);
	while ((inf <= sup) && (res != 0)){
		if(res < 0){
			sup = medio - 1;
		}else inf = medio + 1;
		medio = (inf + sup) / 2;
	}

	if (inf > sup) medio = -1;

	return medio;
}

void cargarVentas(comercio comercios[M], prenda prendas[N]){
	int comercio, unidades;
	char nombre[strLen];

	printf("Introduzca la cantidad de unidades vendidas (0 para terminar)\n");
	scanf("%i", &unidades);
	while(unidades != 0){
		printf("Introduzca el nombre del producto vendido y el codigo del comercio (60 - 94) donde se realizo la venta\n");
		leerCadena(nombre);
		scanf("%i", &comercio);

		int pos = encontrar(prendas, nombre);
		comercios[comercio - 60].ventas[pos] += unidades; 

		printf("Introduzca la cantidad de unidades vendidas (0 para terminar)\n");
		scanf("%i", &unidades);
	}
}

void mostrarComercios(comercio comercios[M], prenda prendas[N]){
	for(int i = 0; i < M; i++){
		float importeTotal = 0;

		for(int x = 0; x < N; x++){
			importeTotal += comercios[i].ventas[x] * prendas[x].precio;
		}

		printf("El comercio %s (CUIL: %s) vendio en total: %.2f\n", comercios[i].nombre, comercios[i].CUIL, importeTotal);
	}
}

void cargaProductos(producto productos[N], comercio comercios[M], prenda prendas[N]){
	for(int i = 0; i < N; i++){
		strcpy(productos[i].nombre, prendas[i].nombre);

		int ventasTotales = 0;

		for(int a = 0; a < M; a++){
			ventasTotales += comercios[a].ventas[i];
		}

		productos[i].ventas = ventasTotales;
	}
}

void ordenarDescendentemente(producto productos[N]){
	int k = 1, i, cota = N - 1;
	producto aux;

	while(k != -1){
		k = -1;

		for(i = 0; i < cota; i++){
			if(productos[i].ventas < productos[i + 1].ventas){
				aux = productos[i];
				productos[i] = productos[i + 1];
				productos[i + 1] = aux;
				k = i;
			}
		}

		cota = k;
	}
}

void mostrarPrimeros5(producto productos[N]){
	for(int i = 0; i < 5; i++){
		printf("El producto %s fue el %i mas vendido\n", productos[i].nombre, i + 1);
	}
}


int main() {
	comercio comercios[M] = {
		{ "20-12301-13", "Pipa's",   { 2, 0, 5, 6, 7  } },
		{ "20-12301-14", "Pipa's 2", { 3, 1, 3, 2, 12 } },
		{ "20-12301-15", "Pipa's 3", { 0, 5, 5, 1, 4  } },
	};
	prenda prendas[N] = {
		{ "Remera", 230 },      //4
		{ "Pantalon", 280.75 }, //3
		{ "Camisa", 320.5 },    //1
		{ "Zapatilla", 240 },   //5
		{ "Corbata", 20.5 },    //2
	};

	// En una estructura se registra por cada prenda que se comercializa su nombre y precio unitario, ordenado alfabéticamente.
	//cargarPrendas(prendas);
	ordenarPorNombre(prendas);

	for(int i = 0; i < 5; i++){
		printf("%s\n", prendas[i].nombre);
	}
	

	// por cada comercio se almacena su CUIL y Nombre.
	//cargarComercios(comercios);

	// Por cada venta realizada se cuenta con los siguientes datos: Código de comercio (60..94), Nombre de la prenda vendida y cantidad de unidades.
	cerearVentasComercios(comercios);
	cargarVentas(comercios, prendas);
	
	// b) Indicar por cada comercio; CUIL, Nombre e importe total a pagar.
	mostrarComercios(comercios, prendas);

	//c) Realizar un listado que contenga por cada producto, nombre y cantidad de unidades vendidas, este listado debe estar ordenado descendentemente por cantidad de unidades.
	producto productos[N];
	cargaProductos(productos, comercios, prendas);
	
	//d) Mostrar el nombre de los 5 productos que más se vendieron.
	ordenarDescendentemente(productos);
	mostrarPrimeros5(productos);

	return 0;
}