#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>

const int N = 100000;

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

void multiply_matrix_vector_partial(Matrix matrix, Vector vector, Vector result, int start, int end) {
	for (int i = start; i < end; i++) {
		result[i] = 0;
		for (int j = 0; j < N; j++) {
			result[i] += matrix[i][j] * vector[j];
		}
	}
}

int main(int argc, char** argv) {
	MPI_Init(&argc, &argv);

	int rank, size;
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);

	int rows_per_process = N / size;
	int start = rank * rows_per_process;
	int end = (rank == size - 1) ? N : start + rows_per_process;

	Matrix matrix = NULL;
	Vector vector = malloc(N * sizeof(Type));
	Vector result = malloc(N * sizeof(Type));
	Vector local_result = malloc(rows_per_process * sizeof(Type));

	if (rank == 0) {
		matrix = malloc(N * sizeof(Vector));
		for (int i = 0; i < N; i++) {
			matrix[i] = malloc(N * sizeof(Type));
		}
		initialize_matrix(matrix);
		initialize_vector(vector);
	}

	MPI_Bcast(vector, N, MPI_UNSIGNED_LONG, 0, MPI_COMM_WORLD);

	if (rank != 0) {
		matrix = malloc(rows_per_process * sizeof(Vector));
		for (int i = 0; i < rows_per_process; i++) {
			matrix[i] = malloc(N * sizeof(Type));
		}
	}

	for (int i = 0; i < rows_per_process; i++) {
		MPI_Scatter(matrix[start + i], N, MPI_UNSIGNED_LONG, matrix[i], N, MPI_UNSIGNED_LONG, 0, MPI_COMM_WORLD);
	}

	multiply_matrix_vector_partial(matrix, vector, local_result, 0, rows_per_process);

	MPI_Gather(local_result, rows_per_process, MPI_UNSIGNED_LONG, result, rows_per_process, MPI_UNSIGNED_LONG, 0, MPI_COMM_WORLD);

	if (rank == 0) {
		for (int i = 0; i < N; i++) {
			printf("%lu ", result[i]);
		}
		printf("\n");
	}

	if (rank == 0) {
		for (int i = 0; i < N; i++) {
			free(matrix[i]);
		}
		free(matrix);
	}
	free(vector);
	free(result);
	free(local_result);

	MPI_Finalize();
	return 0;
}