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

const char* narreras[3] = { "LCC", "LSI", "TUPW" };

alumno_t carga(){
	int nRoReg;
	printf("Introduzca el numero de registro\n");
	scanf("%d", &nRoReg);

	if(nRoReg == 0) return NULL;

	alumno_t alu = (alumno_t) malloc(sizeof(struct alumno));
	alu->nRoReg = nRoReg;
	printf("Introduzca los demas datos del alumno\n");
	fflush(stdin);
	scanf("%c", &alu->sexo);
	scanf("%d", &alu->edad);
	scanf("%d", &alu->carrera);
	fflush(stdin);
	fgets(alu->nombre, 50, stdin);

	alu->next = carga();

	return alu;
	// Error 1 (grave), era "return alu;" y puse "return;"
}

int contador(alumno_t nodo, int &v30, int total){
	if(nodo == NULL) return total;

	if(nodo->sexo == 'V' && nodo->edad > 30) v30++;

	return contador(nodo->next, v30, total + 1);
}

void cambiarCarrera(alumno_t nodo){
	char nombre[50];
	printf("Introduzca el nombre del alumno que cambiara de carrera\n");
	fflush(stdin);
	fgets(nombre, 50, stdin);

	while(nodo != NULL && stricmp(nombre, nodo->nombre) != 0){
		nodo = nodo->next;
	}

	if(nodo == NULL){
		printf("No se encontro el alumno\n");
		return;
	}

	printf("Introduzca la nueva carrera del alumno\n");
	scanf("%d", &nodo->carrera); // Error 2 falto el & en el scanf
}

typedef struct{
	char* nombre;
	int mujeres, varones;
} carrera;

void cargarArreglo(carrera carreras[3], alumno_t cabeza){
	alumno_t temp;

	for(int i = 0; i < 3; i++){
		carreras[i].nombre = (char*) narreras[i];
		/*
		Error 4, const char* no puede ser asignado a char*, 2 soluciones, convertir const char* en char* o declarar narreras como:
		char* narreras[3] = { "LCC", "LSI", "TUPW" };
		*/
		carreras[i].mujeres = 0;
		carreras[i].varones = 0;

		temp = cabeza;

		while(temp != NULL){
			// Error 3 (grave), los contadores no deben contar si no pertenecen a la carrera
			// Falto el "if(temp->carrera == i + 1){...}"
			if(temp->carrera == i + 1){
				if(temp->sexo == 'M') carreras[i].mujeres++;
				else if(temp->sexo == 'V') carreras[i].varones++;
			}

			temp = temp->next;
		}
	}
}

void mostrarArreglo(carrera carreras[3]){
	for(int i = 0; i < 3; i++){
		printf("La carrera %s tiene %d varones y %d mujeres\n", carreras[i].nombre, carreras[i].varones, carreras[i].mujeres);
	}
}

/*
Otros errores:
faltaron los fflush(stdin)
y faltaron los \n en algunos printf
*/

int main(){
	alumno_t cabeza = carga();

	int v30 = 0;
	int total = contador(cabeza, v30, 0);

	cambiarCarrera(cabeza);

	carrera carreras[3];
	cargarArreglo(carreras, cabeza);
	// Error 5 (medio grave) era "cargarArreglo(carreras, cabeza);" y puse "cargarArreglo(carreras);", falto enviar la lista
	mostrarArreglo(carreras);

	return 0;
}

/*
20011
V
31
1
Juan Torres
24341
M
22
2
Alicia Sotelo
19765
V
34
2
Axel Montero
0
Alicia Sotelo
3
*/