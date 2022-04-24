/*
Se registran las incripciones de 3 materias del segundo semestre de primer año. Se tiene registrado el nombre de cada una de las 3 carreras (LCC, LSI, TUPW)
Por cada uno de los alumnos se ingresa numero de registro, nombre, sexo (M - mujer, V - varon), edad y codigo de carrera (1 ... 3), ademas se conoce el nombre de las 3 carreras
a) Generar una lista de informacion de los alumnos
b) Realizar una funcion recursiva que devuelva al principal el total de alumnos y la cantidad de varones mayores de 30 años. Hacer una sola funcion donde un resultado debe ser calculado con la funcion y el otro con un parametro
c) Cambiar la carrera de un alumno cuyo nombre se ingresa por teclado
d) generar a partir de la lista un arreglo que contenga para cada carrera su nombre y la cantidad de mujeres y varones. Mostrar la informacion almacenada en el arreglo
*/

#include <stdio.h>
#include <string.h>
#include <malloc.h>

struct alumno{
	struct alumno* next;
	int nRoReg, edad, carrera;
	char sexo, nombre[50];
};
typedef struct alumno* alumno_t;

typedef struct{
	char* nombre;
	int mujeres, varones;
} carrera;

char* nomCarreras[3] = { "LCC", "LSI", "TUPW" };

alumno_t carga(){
	int nRoReg;
	printf("Introduzca el numero de registro (0 para terminar)\n");
	scanf("%d", &nRoReg);

	if(nRoReg == 0) return NULL;

	alumno_t alu = (alumno_t) malloc(sizeof(struct alumno));
	alu->nRoReg = nRoReg;
	printf("  Introduzca el sexo del alumno: ");
	scanf(" %c", &alu->sexo);
	printf("  Introduzca la edad del alumno: ");
	scanf("%d", &alu->edad);
	printf("  Introduzca la carrera del alumno: ");
	scanf("%d", &alu->carrera);
	printf("  Introduzca el nombre del alumno: ");
	fflush(stdin);
	fgets(alu->nombre, 50, stdin);
	printf("\n");

	alu->next = carga();

	return alu;
}

int contador(alumno_t nodo, int &v30, int total){
	if(nodo == NULL) return total;

	if(nodo->sexo == 'V' && nodo->edad > 30) v30++;

	return contador(nodo->next, v30, total + 1);
}

void cambiarCarrera(alumno_t nodo){
	char nombre[50];
	printf("\nIntroduzca el nombre del alumno que cambiara de carrera\n");
	fflush(stdin);
	fgets(nombre, 50, stdin);

	while(nodo != NULL && stricmp(nombre, nodo->nombre) != 0){
		nodo = nodo->next;
	}

	if(nodo == NULL){
		printf("No se encontro el alumno\n");
		return;
	}
	
	printf("La carrera actual del alumno es: %s (%d)\n", nomCarreras[nodo->carrera - 1], nodo->carrera);
	printf("Introduzca la nueva carrera del alumno (1 - 3): ");
	scanf("%d", &nodo->carrera);
}

void cargarArreglo(carrera carreras[3], alumno_t nodo){
	for(int i = 0; i < 3; i++){
		carreras[i].nombre = nomCarreras[i];
		carreras[i].mujeres = 0;
		carreras[i].varones = 0;
	}

	while(nodo != NULL){
		if(nodo->sexo == 'M') carreras[nodo->carrera - 1].mujeres++;
		else if(nodo->sexo == 'V') carreras[nodo->carrera - 1].varones++;

		nodo = nodo->next;
	}
}

void mostrarArreglo(carrera carreras[3]){
	for(int i = 0; i < 3; i++){
		printf(
			"La carrera %s tiene %d varones y %d mujeres\n",
			carreras[i].nombre, carreras[i].varones, carreras[i].mujeres
		);
	}
}

int main(){
	alumno_t cabeza = carga();

	int total = 0, v30 = 0;
	total = contador(cabeza, v30, total);
	printf("Hay un total de %d alumnos y %d varones mayores a 30\n", total, v30);

	cambiarCarrera(cabeza);

	carrera carreras[3];
	cargarArreglo(carreras, cabeza);
	printf("\n");
	mostrarArreglo(carreras);

	printf("\n¬¬¬¬¬¬¬¬¬¬¬¬¬\n");

	return 0;
}

/*
21000
V
30
3
Aballay, G
22000
M
31
2
Calivar, A
23000
M
32
3
Castro, L
24000
V
26
1
Fernandez, M
25000
M
27
1
Funes, G
26000
V
28
3
Gamboa, M
27000
V
29
2
Gonzalez, S
28000
M
33
1
Fuente, M
0
Funes, G
2

*/