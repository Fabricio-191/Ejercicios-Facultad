/*
Ejercicio 2

Se procesa la información de 97 estudiantes de ingreso a la LCC, de cada uno se registra: Nombre, DNI, Año de ingreso
a la carrera y el promedio del secundario.

1. Almacenar en un arreglo de registro la información de los 97 estudiantes.
2. Indicar cuantos estudiantes ingresaron en el año 2019 y cuantos en el 2020 (hacer una función que devuelva un valor con el retorno y otro por parámetro).
3. Mostrar el Nombre y DNI de los estudiantes que obtuvieron un promedio mayor o igual a 7.
Nota: hacer al menos una función recursiva.
*/
#include <stdio.h>
#define N 97

typedef struct {
	char DNI[11], nombre[40];
	int ingreso;
	float prom;
} estudiante;

void cargar(estudiante estudiantes[N], int i) {
	if(i == N) return;

	printf("Introduzca los datos del estudiante %i\n", i + 1);
	gets(estudiantes[i].nombre);
	scanf("%s%i%f", estudiantes[i].DNI, &estudiantes[i].ingreso, &estudiantes[i].prom);
	fflush(stdin);

	cargar(estudiantes, i + 1);
}

int estudiantesIngreso(estudiante estudiantes[N], int *cont2020){
	int cont2019 = 0;
	for(int i = 0; i < N; i++){
		if(estudiantes[i].ingreso == 2019){
			cont2019++;
		}else if(estudiantes[i].ingreso == 2020){
			*cont2020 = *cont2020 + 1;
		}
	}

	return cont2019;
}

void mostrar(estudiante estudiantes[N]){
	printf("Listado de estudiantes con promedio mayor o igual a 7\n");
	for(int i = 0; i < N; i++){
		if(estudiantes[i].prom >= 7){
			printf("%s (DNI: %s)\n", estudiantes[i].nombre, estudiantes[i].DNI);
		}
	}
}

int main() {
	estudiante estudiantes[N];
	cargar(estudiantes, 0);

	int cont2020 = 0;
	int cont2019 = estudiantesIngreso(estudiantes, &cont2020);
	printf("En 2019 ingresaron %i alumnos y en 2020 ingresaron %i alumnos", cont2019, cont2020);

	mostrar(estudiantes);

	return 0;
}
