#include <stdio.h>
#include <malloc.h>

struct vector{
	float* valores;
	int cant;
};

vector cargarVector(){
	vector vec;

	int cant;
	printf("Introduzca la cantidad de componentes del vector\n");
	scanf("%d", &cant);
	vec.cant = cant;
	vec.valores = (float*) malloc(sizeof(float) * cant);

	float v;
	for(int i = 0; i < cant; i++){
		printf("Introduzca el valor de la componente %i del vector\n", i + 1);
		scanf("%f", &vec.valores[i]);
	}
	return vec;
}

float productoEscalar(vector vec1, vector vec2){
	if(vec1.cant != vec2.cant){
		printf("Para calcular el producto escalar los vectores necesitan tener la misma cantidad de componentes");
	}

	float result = 0;
	for(int i = 0; i < vec1.cant; i++){
		result += vec1.valores[i] * vec2.valores[i]; 
	}

	return result;
}

void cargarImpares(vector &impares, vector vec1){
	impares.valores = (float*) malloc(sizeof(float) * vec1.cant);

	int y = 0;
	for(int i = 0; i < vec1.cant; i++){
		if((int) vec1.valores[i] % 2){
			impares.valores[y++] = vec1.valores[i];
		}
	}

	impares.valores = (float*) realloc(impares.valores, sizeof(float) * y);
	impares.cant = y;
}

void mostrarVector(vector vec){
	printf("\n");
	printf("Cant: %d\n", vec.cant);
	for(int i = 0; i < vec.cant; i++){
		printf("%f\n", vec.valores[i]);
	}
}

int main(){
	vector vec1 = cargarVector(), vec2 = cargarVector(), impares;

	printf("\n");

	float producto = productoEscalar(vec1, vec2);
	printf("El producto escalar es: %f\n", producto);

	cargarImpares(impares, vec1);
}

/*
3
1
2
3
3
4
5
6

*/