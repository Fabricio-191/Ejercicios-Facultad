#include <stdio.h>
#include <stdlib.h>
#define N 3
#define M 3

void carga(int tabla[N][M], int n, int m){
	if(m == -1){
		m = M - 1;
		n--;
	}
	if(n == -1) return;

	int num = rand() % 10;
	tabla[n][m] = num;
	
	printf("tabla[%i][%i] = %i\n", n, m, num);

	carga(tabla, n, m - 1);
}

void carga(int tabla[N][M], int n, int m){
	if(m == -1){
		m = M - 1;
		n--;
	}
	if(n == -1) return;

	int num = rand() % 10;
	tabla[n][m] = num;
	
	printf("tabla[%i][%i] = %i\n", n, m, num);

	carga(tabla, n, m - 1);
}

void carga2(int tabla[N][M], int n, int m){
	if(m == M){
		m = 0;
		n++;
	}
	if(n == N) return;

	int num = rand() % 10;
	tabla[n][m] = num;
	
	printf("tabla[%i][%i] = %i\n", n, m, num);

	carga2(tabla, n, m + 1);
}

void mostrar(int tabla[N][M]){
	for (int i = 0; i < N; i++) {
		for (int y = 0; y < M; y++) printf("%i  ", tabla[i][y]);
		printf("\n");
	}
}

int main(){
	int tabla[N][M];
	
	carga(tabla, N - 1, M - 1);
	//carga2(tabla, 0, 0);
	
	mostrar(tabla);

	return 0;
}