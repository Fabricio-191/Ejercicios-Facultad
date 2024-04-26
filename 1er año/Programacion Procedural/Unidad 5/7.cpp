/*
Ejercicio 7
La Facultad de Ciencias Exactas organizó el Congreso de Informática, y necesita administrar la información relativa a los 10 tutoriales que se proponen en dicho evento.
Realizar un programa, que a través de un menú de opciones permita:
a) Ingresar los datos correspondientes a cada tutorial: número de tutorial (1-10) y título.
b) Registrar las inscripciones, ingresando el DNI del inscripto y el número de tutorial al que desea asistir.
c) Eliminar alguna inscripción, en cuyo caso se ingresarán los mismos datos que en el ítem anterior.
d) Dado el número de un tutorial, mostrar su título y la cantidad de inscriptos en él.
e) Dado el DNI de una persona, informar el/los tutoriales (número y título) en los que se inscribió.
Nota: Para cada ítem emplear al menos una función recursiva.
*/
#include <stdio.h>
#include <malloc.h>
#include <string.h>
#define strLen 40
#define N 10

struct inscripto {
    struct inscripto *next;
	char DNI[strLen];
	int num_tutorial;
};
typedef struct inscripto* inscripto_t;

struct tutorial_t {
	char titulo[strLen];
	int num;
};

void leerString(char* str){
	fflush(stdin);
	fgets(str, strLen, stdin);

	char* pos = strchr(str, '\n');
	if (pos != NULL) *pos = '\0';
}

void cargarTutoriales(tutorial_t tutoriales[N], int i){
	if(i == N) return;
	
	printf("  Introduzca el numero del tutorial: ");
	scanf("%d", &tutoriales[i].num);
	printf("  Introduzca el titulo del tutorial: ");
	leerString(tutoriales[i].titulo);

	cargarTutoriales(tutoriales, i + 1);
}

inscripto_t cargarInscriptos(){
	int num;
	printf("  Ingrese el numero de tutorial (0 para terminar): ");
	scanf("%d", &num);

	if(num == 0) return NULL;
	inscripto_t insc = (inscripto_t) malloc(sizeof(struct inscripto));

	printf("  Ingrese el DNI del inscripto: ");
	scanf("%s", insc->DNI);

	insc->num_tutorial = num;
	insc->next = cargarInscriptos();

	return insc;
}

void borrarInscripcion(inscripto_t nodo, char DNI[10], int num){
	if(nodo == NULL || nodo->next == NULL) return;
	if(
		nodo->next->num_tutorial == num &&
		strcmp(nodo->next->DNI, DNI) == 0
	){	
		inscripto_t temp = nodo->next->next;
		free(nodo->next);
		nodo->next = temp;
	}

	borrarInscripcion(nodo->next, DNI, num);
}

int contarInscriptos(inscripto_t nodo, int num, int cont){
	if(nodo->next == NULL) return cont;

	return contarInscriptos(
		nodo->next,
		num,
		cont + nodo->num_tutorial == num
	);
}

void tutorialesSegunDNI(inscripto_t nodo, tutorial_t tutoriales[N], char DNI[10]){
	if(nodo == NULL) return;

	if(strcmp(nodo->DNI, DNI) == 0){
		char* titulo = tutoriales[nodo->num_tutorial - 1].titulo;

		printf("  \"%s\" numero: %d\n", titulo, nodo->num_tutorial);
	}

	tutorialesSegunDNI(nodo->next, tutoriales, DNI);
}

int main(){
	tutorial_t tutoriales[N];
	inscripto_t inscriptos;

	int opcion;
	printf("Introduzca la opcion a ejecutar (0 para terminar): ");
	scanf("%d", &opcion);
	while(opcion != 0){
		printf("\n");
		switch (opcion){
			case 1:{ // Carga tutoriales
				cargarTutoriales(tutoriales, 0);
				break;
			}
			case 2:{ // Carga inscripciones
				inscriptos = cargarInscriptos();
				break;
			}
			case 3:{ // Borrar inscripciones
				char DNI[10]; int num;
				printf("Introduzca los datos de la inscripcion a borrar\n  DNI: ");
				scanf("%s", DNI);
				printf("  Numero de tutorial: ");
				scanf("%d", &num);

				inscripto_t cabeza = (inscripto_t) malloc(sizeof(struct inscripto));
				cabeza->next = inscriptos;

				borrarInscripcion(cabeza, DNI, num);
				inscriptos = cabeza->next;
				free(cabeza);
				break;
			}
			case 4:{ // Mostrar tutorial
				int num;
				printf("Introduzca el numero del tutorial a mostrar: ");
				scanf("%d", &num);

				int cant = contarInscriptos(inscriptos, num, 0);

				printf("  titulo: %s\n", tutoriales[num - 1].titulo);
				printf("  inscriptos: %d\n", cant);
				break;
			}
			case 5:{ // Mostrar inscripciones por DNI
				char DNI[10];
				printf("Introduzca el DNI a buscar: ");
				scanf("%s", &DNI);

				printf("Los tutoriales en los que esta inscripto son:\n");
				tutorialesSegunDNI(inscriptos, tutoriales, DNI);
			}
		}

		printf("\nIntroduzca la opcion a ejecutar (0 para terminar): ");
		scanf("%d", &opcion);
	}

	return 0;
}
/*
1
1
Cocina 1
2
Cocina 2
3
Cocina 3
4
Cocina 4
5
Cocina 5
6
Cocina 6
7
Cocina 7
8
Cocina 8
9
Cocina 9
10
Cocina 10
2
1
¬¬¬¬
10
¬¬¬¬
0
4
2
4
1
5
¬¬¬¬
3
¬¬¬¬
10
5
¬¬¬¬
0

*/