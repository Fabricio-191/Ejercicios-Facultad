#include <stdio.h>
#define N 6

struct curso {
	int edadPromM, edadPromV, mujeres, varones;
};

typedef struct curso curso;

curso carga(curso cur){
	int edad; char sexo;

	printf("\nIntroduzca la edad del alumno (0 para terminar)\n");
	scanf("%i", &edad);

	while(edad != 0){
		printf("Introduzca el sexo del alumno M o V\n");
		scanf(" %c", &sexo);

		if(sexo == 'M' || sexo == 'm'){
			cur.mujeres++;
			cur.edadPromM += edad;
		}else{
			cur.varones++;
			cur.edadPromV += edad;
		}
		printf("\nIntroduzca la edad del alumno (0 para terminar)\n");
		scanf("%i", &edad);
	}

	if(cur.varones > 0) cur.edadPromV /= cur.varones;
	if(cur.mujeres > 0) cur.edadPromM /= cur.mujeres;
	
	return cur;
}

void cargaCursos(curso cursos[N]){
	for(int i = 0; i < N; i++){
		cursos[i].varones = 0;
		cursos[i].mujeres = 0;
		cursos[i].edadPromM = 0;
		cursos[i].edadPromV = 0;

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
			int edadProm = (cur.edadPromM + cur.edadPromV) / 2;

			printf("En el curso %i la cantidad de mujeres es igual a la de hombres\n",  i + 1);
			printf("y la edad promedio es: %i\n\n", edadProm);
		}
	}
}

void mismaEdadProm(curso cursos[N]){
	int cont = 0;

	for(int i = 0; i < N; i++){
		if(cursos[i].edadPromM == cursos[i].edadPromV) cont++;
	}

	printf("Hay %i curso/s con la misma edad promedio entre mujeres y hombres", cont);
}

int main(){
	curso cursos[N];

	cargaCursos(cursos);
	cantIguales(cursos);
	mismaEdadProm(cursos);

	return 0;
}