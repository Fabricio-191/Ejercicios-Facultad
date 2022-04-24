#include <stdio.h>
#include <malloc.h>
#include <string.h>

struct alumno{
	alumno *next;
	char nombre[30], carrera[4];
};

struct libro{
	libro *next;
	int codigo;
	alumno* cola;
};

void cargaLibros(libro* cabeza){
	int cod;
	printf("Introduzca el codigo de libro (0 para terminar)\n");
	scanf("%d", &cod);

	while(cod != 0){
		libro* temp = (libro*) malloc(sizeof(libro));
		temp->next = cabeza->next;
		temp->codigo = cod;
		temp->cola = NULL;
		cabeza->next = temp;

		printf("Introduzca el codigo de libro (0 para terminar)\n");
		scanf("%d", &cod);
	}
}

libro* cabezaLibros(){
	libro* cabeza = (libro*) malloc(sizeof(libro));
	cabeza->next = NULL;
	cabeza->codigo = -1;
	cabeza->cola = NULL;

	return cabeza;
}

void insertarAlumno(libro* nodo, int codigo){
	if(nodo->next == NULL) return;

	nodo = nodo->next;

	if(nodo->codigo == codigo){
		printf("Introduzca el nombre y carrera del alumno\n");

		alumno* alu = (alumno*) malloc(sizeof(alumno));
		fflush(stdin);
		fgets(alu->nombre, 50, stdin);
		fflush(stdin);
		scanf("%s", alu->carrera);

		alu->next = nodo->cola;

		nodo->cola = alu;

		return;
	}

	insertarAlumno(nodo, codigo);
}

void nuevoLibro(libro* cabeza){
	int cod;
	printf("Introduzca el codigo del libro nuevo\n");
	scanf("%d", &cod);

	libro* nuevo = (libro*) malloc(sizeof(libro));
	nuevo->codigo = cod;
	nuevo->next = cabeza->next;
	nuevo->cola = NULL;
	cabeza->next = nuevo;
}

void eliminarPrestamo(libro* nodo, int cod){
	if(nodo->codigo != cod){
		if(nodo->next != NULL) return eliminarPrestamo(nodo->next, cod);
		return;
	}

	alumno* alu = nodo->cola;
	if(alu == NULL) return;
	else if(alu->next == NULL){
		nodo->cola = NULL;
	}else{
		while(alu->next->next != NULL){
			alu = alu->next;
		}

		alu->next = NULL;
	}
}

void mostrar(libro* nodo, int codigo, char carrera[3]){
	nodo = nodo->next;
	while(nodo != NULL && nodo->codigo != codigo){
		nodo = nodo->next;
	}

	if(nodo == NULL) return;

	alumno* alu = nodo->cola;

	while(alu != NULL){
		if(stricmp(alu->carrera, carrera) == 0){
			printf("nombre: %s\n", alu->nombre);
		}
		alu = alu->next;
	}
}

int main(){
	libro* cabeza = cabezaLibros();
	int opcion, cod;

	printf("Introduzca la opcion a ejecutar (0 para terminar)\n");
	scanf("%d", &opcion);
	while(opcion != 0){
		switch(opcion){
			case 1:{
				cargaLibros(cabeza);
				break;
			}
			case 2:{
				printf("Introduzca el codigo de libro donde insertar\n");
				scanf("%d", &cod);
				insertarAlumno(cabeza, cod);
				break;
			}
			case 3:{
				nuevoLibro(cabeza);
				break;
			}
			case 4:{
				printf("Introduzca el libro devuelto\n");
				scanf("%d", &cod);

				eliminarPrestamo(cabeza, cod);
				break;
			}
			case 5:{
				char carrera[4];

				printf("Introduzca el codigo del libro y la carrera a mostrar\n");
				scanf("%d", &cod);
				scanf("%s", carrera);

				mostrar(cabeza, cod, carrera);
				break;
			}
		}

		printf("Introduzca la opcion a ejecutar (0 para terminar)\n");
		scanf("%d", &opcion);
	}
}

/*
1
100
200
300
0
2
200
Tu mama
LCC
2
200
Fabricio
LCC
2
200
Diego
LCC
3
400
4
300
4
200
5
200
LCC
0

*/








