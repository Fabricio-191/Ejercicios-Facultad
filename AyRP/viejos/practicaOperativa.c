#include <stdio.h>
#include <string.h>
#define strLen 20
#define N 6

struct prodnulo {
	int codigo;
	float precio;
};
struct producto {
	int codigo, stock;
	float precio;
	char nomprod[strLen];
};

typedef struct prodnulo prodnulo;
typedef struct producto producto;	

void removeNewline(char string[strLen]){
	char *pos = strchr(string, '\n'); 
	//strchr recorre la primera string hasta que encuentra un caracter de la segunda string en la primera string
	//y devuelve la posicion (puntero) donde ocurrio la coincidencia
	if (pos != NULL) *pos = '\0'; //Si el puntero no es nulo (hay una coincidencia), lo reemplaza por un caracter nulo, cortando la string y haciendo que termine ahi
	//Si una string toma el salto de linea (\n) usando el fgets, esta funcion lo reemplaza
}

void inicia (producto xp[N]){
	for(int i = 0; i < N; i++){
		xp[i].codigo = i+100;

		printf("Ingrese el nombre del producto con codigo: %d\n", i + 100);
		fgets(xp[i].nomprod, strLen, stdin);
		removeNewline(xp[i].nomprod);

		printf("Ingrese el precio del producto con codigo: %d\n", i + 100);
		scanf("%f", &xp[i].precio);

		printf("Ingrese el stock del producto con codigo: %d\n", i + 100);
		scanf("%d", &xp[i].stock);

		printf("\n");
		fflush(stdin);
	}
	return;
}

int busqueda (char xnombre[strLen], producto xp[N]){
	int i = 0;

	while((i < N) && (strcmp(xnombre, xp[i].nomprod) != 0)){
		i++;
	}

	if(i < N){
		return i;
	}else{
		return -1;
	}
}

void ventas (producto xp[N]){
	char nombre[strLen];
	int unidades, pos;

	printf("Ingrese el nombre del producto, finalice con \"fin\"\n");
	fflush(stdin);
	fgets(nombre, strLen, stdin);
	removeNewline(nombre);

	while(strcmp(nombre, "fin") != 0){
		pos = busqueda (nombre, xp);

		if(pos != -1){
			printf("Ingrese la cantidad de unidades vendidas\n");
			scanf("%d", &unidades);

			xp[pos].stock = xp[pos].stock - unidades;
		}else{
			printf("Nombre no valido\n");
		}

		printf("\n"); fflush(stdin);

		printf("Ingrese el nombre del producto, finalice con \"fin\"\n");
		fgets(nombre, strLen, stdin);
		removeNewline(nombre);

		printf("\n");
	}
	return;
}

void mostrar1 (producto xp[N]){
	printf("Listado de productos con stock actualizada\n\n");
	for(int i = 0; i < N; i++){
		printf(
			"Codigo: %d\nNombre: %s\nPrecio: %.2f\nStock: %d\n\n", 
			xp[i].codigo, xp[i].nomprod, xp[i].precio, xp[i].stock
		);
	}
	return;
}

int genera (producto xp[N], prodnulo xpn[N]){
	int j = 0;

	for(int i = 0; i < N; i++){
		if(xp[i].stock == 0){
			xpn[j].precio = xp[i].precio;
			xpn[j].codigo = xp[i].codigo;
			j++;
		}
	}
	return j;
}

void mostrar2 (prodnulo xpn[N], int M){
	printf("¬¬¬¬¬¬¬¬¬¬¬¬¬\n");
	printf("Listado de productos con stock nulo\n");
	for(int i = 0; i < M; i++){
		printf(
			"Codigo: %d\nPrecio: %.2f\n", 
			xpn[i].codigo, xpn[i].precio
		);
	}
	return;
}

int main(){
	producto prod[N];
	prodnulo prodn[N];

	inicia (prod);
	ventas (prod);
	mostrar1 (prod);
	int cant = genera (prod, prodn);
	mostrar2 (prodn, cant);
}

/*
Este es el lote de prueba, se puede copiar y pegar en consola:
Notebook
115000
16
Tablet
14500
4
Monitor
18000
7
Mouse
800
6
Router
8500
5
Camara
3000
3
Tablet
1
Notebook
1
Camara
1
Mouse
4
Tablet
2
Notebook
1
Monitor
2
Mouse
2
Tablet
1
Router
5
Camara
2
Notebook
2
fin

*/