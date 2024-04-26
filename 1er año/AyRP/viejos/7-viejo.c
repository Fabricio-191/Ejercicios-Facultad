#include <stdio.h>
#include <stdbool.h>
#define N 6

/*
Este es el ejercicio 7 pero antes de que cambiaran el inciso 3:
3. Informar cuantos cursos tienen la misma edad promedio.
*/

struct curso {
	int edadProm, mujeres, varones;
};

typedef struct curso curso;

curso carga(curso cur){
	int edad; char sexo;

	printf("\nIntroduzca la edad del alumno (0 para terminar)\n");
	scanf("%i", &edad);

	while(edad != 0){
		printf("Introduzca el sexo del alumno M o V\n");
		scanf(" %c", &sexo);

		cur.edadProm += edad;
		if(sexo == 'M' || sexo == 'm'){
			cur.mujeres++;
		}else{
			cur.varones++;
		}
		printf("\nIntroduzca la edad del alumno (0 para terminar)\n");
		scanf("%i", &edad);
	}

	int alumnosTotales = cur.varones + cur.mujeres;
	if(alumnosTotales > 0) cur.edadProm /= alumnosTotales;

	return cur;
}

void cargaCursos(curso cursos[N]){
	for(int i = 0; i < N; i++){
		cursos[i].varones = 0;
		cursos[i].mujeres = 0;
		cursos[i].edadProm = 0;

		printf("\nIntroduzca los datos de los alumnos del curso: %i\n", i + 1);
		cursos[i] = carga(cursos[i]);
	}
	printf("\n");
}

void cantIguales(curso cursos[N]){
	curso cur;

	for(int i = 0; i < N; i++){
		cur = cursos[i];

		if(cur.varones == cur.mujeres){
			printf("En el curso %i la cantidad de mujeres es igual a la de hombres\n",  i + 1);
			printf("y la edad promedio es: %i\n\n", cur.edadProm);
		}
	}
}


int cantidadMismaEdad(curso cursos[N], int edad){
	int cont = 0;

	for(int i = 0; i < N; i++){
		if(cursos[i].edadProm == edad) cont++;
	}

	return cont;
}

bool tiene(int edadesMostradas[N], int LT, int valor){
	int i = 0;
	bool encontro = false;

	while((i < LT) && !encontro){
		if(edadesMostradas[i] == valor){
			encontro = true;
		}else i++;
	}

	return encontro;
}

//3. Informar cuantos cursos tienen la misma edad promedio.
void mismaEdadProm(curso cursos[N]){
	int edadesMostradas[N], LT = 0, cant, edadProm;

	for(int i = 0; i < N; i++){
		edadProm = cursos[i].edadProm;
		cant = cantidadMismaEdad(cursos, edadProm); //cantidad de cursos con esa edad promedio

		//el tiene es para comprobar que esa edad promedio no se haya mostrado antes
		if((cant > 1) && !tiene(edadesMostradas, LT, edadProm)){
			printf("Hay %i cursos con la edad promedio: %i\n", cant, edadProm);
			edadesMostradas[LT] = edadProm;
			LT++;
		}
	}
}

int main(){
	curso cursos[N];

	cargaCursos(cursos);
	cantIguales(cursos);
	mismaEdadProm(cursos);

	return 0;
}