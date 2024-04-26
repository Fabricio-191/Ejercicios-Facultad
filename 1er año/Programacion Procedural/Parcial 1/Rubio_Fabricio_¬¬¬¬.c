/*
Se tiene la información de 3 hoteles de Iguazú y el movimiento turístico en la temporada invernal (junio, julio y agosto).

Cada tabla debe representar un hotel, la fila al mes y la columna la nacionalidad.
*/
#include <stdio.h>
#include <string.h>
#define X 3
#define Y 3
#define Z 3

/*
Para los incisos que se les pide que escriba o lea nombre de mes o nacionalidad, deben trabajar con arreglos, donde tengan guardados los nombres.
*/
const char nacionalidades[3][10] = { "Argentina", "Brasil", "Otra" };
const char meses[3][10] = { "junio", "julio", "agosto" };
int indexMes(char mes[10]){
	for(int i = 0; i < 3; i++){
		if(stricmp(mes, meses[i]) == 0) return i;
	}

	return -1;
}

// Nota: Realizar al menos una función recursiva
void cerear(int hoteles[X][Y][Z], int x, int y, int z){
	if(z == Z){ z = 0; y++; }
	if(y == Y){ y = 0; x++; }
	if(x == X) return;

	hoteles[x][y][z] = 0;
	cerear(hoteles, x, y, z + 1);
}

/*
Para procesar estos datos se ingresa por cada turista el número de hotel (1..3), Mes (el nombre) y la nacionalidad del turista (1: Argentina, 2: Brasil, 3: Otra); finalizando con número de hotel igual a cero.
*/
void carga(int hoteles[X][Y][Z]){
	int hotel, nacionalidad;
	char mes[10];

	printf("Introduzca el numero del hotel (0 para terminar)\n");
	scanf("%i", &hotel);

	while(hotel != 0){
		printf("Introduzca el mes\n");
		scanf("%s", mes);
		printf("Introduzca la nacionalidad\n");
		scanf("%i", &nacionalidad);

		hoteles[hotel - 1][indexMes(mes)][nacionalidad - 1]++;

		printf("Introduzca el numero del hotel (0 para terminar)\n");
		scanf("%i", &hotel);
	}
}

/*
Decir para cada Hotel, el total de turistas que recibió mensualmente (escribir el número de mes).
Procesar todo el cubo, trabajando con cada tabla.
*/
void turistasMensuales(int hoteles[X][Y][Z]){
	for(int x = 0; x < X; x++){
		for(int y = 0; y < Y; y++){
			int acum = 0;
			for(int z = 0; z < Z; z++){
				acum += hoteles[x][y][z];
			}

			printf("El hotel %i recibio %i turistas el mes %i\n", x + 1, acum, y + 6);
		}
	}
}

/*
Ingresar un número de Hotel y decir a que nacionalidad corresponde la mayor cantidad de turistas.
Procesar una tabla, trabajando con las columnas
*/
void hotelNacionalidad(int hoteles[X][Y][Z]){
	int hotel;
	printf("Ingrese el numero del hotel para saber a que nacionalidad corresponde la mayor cantidad de turistas\n");
	scanf("%i", &hotel);
	hotel--;

	int max = 0, totales[Z];
	for(int z = 0; z < Z; z++){
		int total = 0;
		for(int y = 0; y < Y; y++){
			total += hoteles[hotel][y][z];
		}

		totales[z] = total;
		if(total > max) max = total;
	}

	for(int z = 0; z < Z; z++){
		if(totales[z] == max){
			printf("Una de las mayores cantidades, corresponde a la nacionalidad: %s\n", nacionalidades[z]);
		}
	}
}

/*
Decir la cantidad de turistas para un nombre de mes ingresado por teclado.
Procesar todo el cubo, trabajando con una fila en particular de cada tabla.
*/
void turistasMes(int hoteles[X][Y][Z]){
	char mes[10];
	printf("Ingrese el nombre de mes (junio, julio, agosto), para saber la cantidad de turistas\n");
	scanf("%s", mes);
	
	int mesNum = indexMes(mes);
	if(mesNum == -1){
		printf("Ese mes no es valido");
		return;
	}

	int total = 0;
	for(int x = 0; x < X; x++) {
		for(int z = 0; z < Z; z++) {
			total += hoteles[x][mesNum][z];
		}
	}

	printf("El total de turistas de ese mes es %i\n", total);
	printf("¬¬¬¬¬¬¬¬¬¬¬¬¬");
}

int main(){
	int hoteles[X][Y][Z];

	cerear(hoteles, 0, 0, 0);
	carga(hoteles);
	printf("\n");
	// mostrar(hoteles);

	turistasMensuales(hoteles);
	printf("\n");
	hotelNacionalidad(hoteles);
	printf("\n");
	turistasMes(hoteles);
}

/* (para copiar y pegar en consola)
1
Agosto
3
3
Agosto
2
2
Junio
1
2
Junio
1
2
Junio
2
1
Julio
2
1
Junio
2
1
Julio
1
2
Agosto
1
1
Junio
3
2
Agosto
1
3
Julio
2
1
Julio
2
1
Junio
1
3
Agosto
3
2
Junio
3
3
Agosto
3
3
Junio
3
1
Julio
3
1
Agosto
1
2
Agosto
3
3
Julio
3
2
Julio
2
2
Junio
1
3
Julio
2
2
Julio
2
2
Julio
2
2
Agosto
1
3
Julio
1
3
Agosto
1
1
Julio
1
0

*/
