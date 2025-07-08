// haz la multiplicacion de una matrix cuadrada N por N con un vector de N

#include <stdio.h>
#include <stdlib.h>

const int N = 50000;

typedef unsigned long int Type;
typedef Type* Vector;
typedef Type** Matrix;

void initialize_matrix(Matrix matrix) {
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			matrix[i][j] = 1;
		}
	}
}

void initialize_vector(Vector vector) {
	for (int i = 0; i < N; i++) {
		vector[i] = 1;
	}
}

void multiply_matrix_vector(Matrix matrix, Vector vector, Vector result) {
	for (int i = 0; i < N; i++) {
		result[i] = 0;
		for (int j = 0; j < N; j++) {
			result[i] += matrix[i][j] * vector[j];
		}
	}
}

void print_vector(Vector vector) {
	for (int i = 0; i < N; i++) {
		printf("%d ", vector[i]);
	}
	printf("\n");
}

int main(){
	printf("Creating empty matrix ...\n");
	Matrix matrix = malloc(N * sizeof(Vector)); // vector de punteros
	for (int i = 0; i < N; i++) {
		if(i % 10000 == 0) printf("%d\n", i);
		matrix[i] = malloc(N * sizeof(Type)); // cada fila
	}

	printf("Creating vector ...\n");
	Vector vector = malloc(N * sizeof(Type));
	printf("Creating result vector ...\n");
	Vector result = malloc(N * sizeof(Type));

	printf("Initializing matrix ...\n");
	initialize_matrix(matrix);
	printf("Initializing vector ...\n");
	initialize_vector(vector);

	printf("Multiplying matrix by vector ...\n");
	multiply_matrix_vector(matrix, vector, result);

	printf("Multiplication completed.\n");
	print_vector(result);

	return 0;
}