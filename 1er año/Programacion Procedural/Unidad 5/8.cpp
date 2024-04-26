#include <stdio.h>
#include <malloc.h>
#include <string.h>
#define strLen 50

struct inscripcion{
	struct inscripcion *next;
	char nombre[strLen];
	float promedio;
	int curso;
};
typedef struct inscripcion* inscripcion_t;

typedef struct{
	char nombre[strLen];
	inscripcion_t inscripciones;
} facultad_t;

/*
Ejercicio 8
La UNSJ todos los años otorga becas, para lo cual se ingresa el número de facultades participantes, de las misma se
ingresan los nombres y de cada una las inscripciones de los alumnos aspirantes a las becas de ayuda económica. Se
ingresa, en forma ordenada por facultad, los datos de cada alumno: Nombre, promedio y año que cursa.
Se pide, un programa que permita:
a) Realizar un listado ordenado por promedio, de los alumnos inscriptos en una determinada facultad cuyo nombre se ingresa por teclado. (Mostrar nombre del alumno, promedio y año que cursa).
b) Indicar el nombre de la facultad que tiene menos inscriptos y la cantidad de inscriptos (suponer único).
c) Mostar por cada facultad la cantidad de alumnos con promedio mayor o igual a 7, que cursan de segundo año en adelante. Usar una función recursiva.
*/

void leerString(char* str){
	fflush(stdin);
	fgets(str, strLen, stdin);

	char* pos = strchr(str, '\n');
	if (pos != NULL) *pos = '\0';
}

inscripcion_t cargaInscripciones(){
	char nombre[strLen];
	
	printf("  Introduzca el nombre del alumno (fin para terminar): ");
	leerString(nombre);

	if(stricmp(nombre, "fin") == 0) return NULL;

	inscripcion_t nodo = (inscripcion_t) malloc(sizeof(struct inscripcion));

	strcpy(nodo->nombre, nombre);
	printf("  Introduzca el promedio: ");
	scanf("%f", &nodo->promedio);
	printf("  Introduzca el curso que cursa: ");
	scanf("%i", &nodo->curso);

	printf("\n");
	nodo->next = cargaInscripciones();
	return nodo;
}

void cargaFacultades(facultad_t facultades[], int cantFacultades){
	for(int i = 0; i < cantFacultades; i++){
		printf("\nIntroduzca el nombre de la facultad: ");
		leerString(facultades[i].nombre);

		facultades[i].inscripciones = cargaInscripciones();
	}
}

void ordenar(inscripcion_t nodo){
    inscripcion_t aux, k = NULL, p, cota = NULL;

    while (k != nodo){
        k = nodo;
		p = nodo;

        while (p->next != cota){
            if (p->promedio > p->next->promedio){
                aux = p->next;
                p->next = p;
                p = aux;
                k = p;
            };
            p = p->next;
        }

        cota = k->next;
    }
}
	
void mostrarListado(inscripcion_t nodo){
	if(nodo == NULL) return;

	printf("Alumno: %s %.2f %d\n", nodo->nombre, nodo->promedio, nodo->curso);

	mostrarListado(nodo->next);
}

void buscarFacultad(facultad_t facultades[], int cantFacultades){
	char nombreFacultad[strLen];
	printf("Introduzca el nombre de la facultad a buscar: ");
	leerString(nombreFacultad);

	for(int i = 0; i < cantFacultades; i++){
		printf("%i\n", i);
		if(stricmp(facultades[i].nombre, nombreFacultad) == 0){
			inscripcion_t cabeza = (inscripcion_t) malloc(sizeof(struct inscripcion));
			cabeza->next = facultades[i].inscripciones;

			ordenar(cabeza);
			facultades[i].inscripciones = cabeza->next;

			mostrarListado(facultades[i].inscripciones);
			return;
		}
	}
}

int cantidadInscriptos(inscripcion_t nodo, int i){
	if(nodo == NULL) return i;

	return cantidadInscriptos(nodo->next, i + 1);
}

void menosInscriptos(facultad_t facultades[], int cantFacultades){
	int cantidades[cantFacultades];

	for(int i = 0; i < cantFacultades; i++){
		cantidades[i] = cantidadInscriptos(facultades[i].inscripciones, 0);
	}

	int indexMin = 0;
	for(int i = 1; i < cantFacultades; i++){
		if(cantidades[i] < cantidades[indexMin]) indexMin = i;
	}

	printf("La facultad con menos alumnos es: %s, con %d alumnos\n", facultades[indexMin].nombre, cantidades[indexMin]);
}

int promedio7(inscripcion_t nodo, int i){
	if(nodo == NULL) return i;

	return cantidadInscriptos(nodo->next, i + (nodo->promedio >= 7 && nodo->curso >= 2));
}

void alumnosPromedio(facultad_t facultades[], int cantFacultades){
	int cant;
	for(int i = 0; i < cantFacultades; i++){
		cant = promedio7(facultades[i].inscripciones, 0);

		printf("La facultad %s tiene %d alumnos con promedio mayor o igual a 7, que cursan segundo curso en adelante\n", facultades[i].nombre, cant);
	}
}

void freeLista(inscripcion_t nodo){
	if(nodo->next != NULL) freeLista(nodo->next);
	free(nodo);
}

void freeFacultades(facultad_t facultades[], int cantFacultades){
	for(int i = 0; i < cantFacultades; i++){
		freeLista(facultades[i].inscripciones);
	}
}

int main(){
	int cantFacultades;
	printf("Introduzca la cantidad de facultades: ");
	scanf("%d", &cantFacultades);

	facultad_t facultades[cantFacultades];
	cargaFacultades(facultades, cantFacultades);

	printf("\n");
	buscarFacultad(facultades, cantFacultades);
	printf("\n");
	menosInscriptos(facultades, cantFacultades);
	printf("\n");
	alumnosPromedio(facultades, cantFacultades);

	freeFacultades(facultades, cantFacultades);

	return 0;
}

void ordenar2(inscripcion_t nodo, inscripcion_t &cabeza){
    inscripcion_t aux, k, p, cota = NULL;

    while (k != nodo){
        k = p = nodo;

        while (p->next != cota){
            if (p->promedio > p->next->promedio){
				if(p == cabeza) cabeza = p->next;
                aux = p->next;
                p->next = p;
                p = aux;

                k = p;
            };
            p = p->next;
        }

        cota = k->next;
    }
}

/*
3
UNSJ 1
Juanito
7
2
Fin
UNSJ 2
Juanito 2
7
2
Juanito 5
2
5
Juanito 6
4
5
Fin
UNSJ 3
Juanito 3
7
2
Fin
UNSJ 2

*/