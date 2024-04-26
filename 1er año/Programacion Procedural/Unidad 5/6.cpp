#include <stdio.h>
#include <malloc.h>
#include <string.h>
#define strLen 50
#define N 3

/*
Ejercicio 6
El Proyecto Internacional de Código de Barras de la Vida (iBOL, del inglés International Barcode of Life Project) tiene
como objetivo la obtención de las “huellas genéticas” de las especies en peligro de extinción. Para ello se registra toda
la fauna y flora con el fin de constituir una base de datos global que pueda ser consultada por la comunidad científica
de todo el mundo. En particular se registrará información de los países de Argentina, Brasil y Estados Unidos,
conociendo de los mismos: país, continente y especies. De cada especie en peligro de extinción se registra: nombre,
nombre científico, reino (animal/fauna o vegetal/flora) y cantidad de ejemplares.
Realizar un programa en C que a través de funciones óptimas permita:
a) Generar un arreglo de lista a través de especie_ts con los datos de las especies en extinción para los países indicados.
El ingreso de información se encuentra ordenada por país. Para cada país el ingreso de información finaliza con el
nombre de la especie igual a FIN.
b) Para un nombre de país ingresado por teclado, realizar una función que devuelva al programa principal la cantidad
de especies de la flora y cantidad de especies de la fauna en peligro de extinción. Realizar una función recursiva
que devuelva un dato por parámetro y el otro que lo calcule la función.
c) Incrementar en 200 ejemplares la cantidad de la especie con nombre Petiribí (árbol) en Brasil.
d) Indicar en el programa principal cantidad de ejemplares de Petiribí (árbol presente en Argentina y Brasil)
considerar solamente los ejemplares de los países indicados.
Nota: Para los distintos países se registra una sola vez las distintas especies.
*/

struct especie{
	char nombre[strLen];
	char nom_cientifico[strLen];
	char reino[strLen];
	int cantidad;
	struct especie *sig;
};
typedef struct especie *especie_t;

typedef struct {
	char nombre[strLen];
	char continente[strLen];
	especie_t especies;
} pais_t;

void leerString(char* str){
	fflush(stdin);
	fgets(str, strLen, stdin);

	char* pos = strchr(str, '\n');
	if (pos != NULL) *pos = '\0';
}

void carga(especie_t &nodo){
	char n[strLen];
	printf("  Nombre de la especie: ");
	leerString(n);

	if(stricmp(n, "fin") == 0) return;
	
	nodo = (especie_t) malloc(sizeof(struct especie));

	strcpy(nodo->nombre, n);

	printf("  Nombre cientifico: ");
	leerString(nodo->nom_cientifico);
	printf("  Reino: ");
	leerString(nodo->reino);
	printf("  Cantidad de ejemplares: ");
	scanf("%d", &nodo->cantidad);
	
	nodo->sig = NULL;
	printf("\n");
	carga(nodo->sig);
}

void cargarPaises(pais_t paises[N]){
	for(int i = 0; i < N; i++){
		printf("Introduzca el nombre del pais");
		leerString(paises[i].nombre);
		printf("Introduzca el nombre del continente donde esta el pais");
		leerString(paises[i].continente);
		carga(paises[i].especies);
		printf("\n");
	}
}

int contadores(especie_t nodo, int &contFlora, int contFauna){
	if(nodo == NULL) return contFauna;

	if(stricmp(nodo->reino, "fauna") == 0){
		contFauna++;
	}else if(stricmp(nodo->reino, "flora") == 0){
		contFlora++;
	}

	return contadores(nodo->sig, contFlora, contFauna);
}

void mas200peti(especie_t nodo){
	if(nodo == NULL) return;

	if(stricmp(nodo->nombre, "petiribi") == 0){
		nodo->cantidad += 200;
		return;
	}

	mas200peti(nodo->sig);
}

int contadorPeti(especie_t nodo){
	if(nodo == NULL) return 0;

	if(stricmp(nodo->nombre, "petiribi") == 0){
		return nodo->cantidad;
	}

	return contadorPeti(nodo->sig);
}

especie_t obtenerEspecies(pais_t paises[N], char pais[strLen]){
	int i;
	for(i = 0; i < N; i++) {
		if(stricmp(paises[i].nombre, pais)) break;
	}

	return paises[i].especies;
}

int main(){
	pais_t paises[N];
	cargarPaises(paises);

	char pais[strLen];
	int contFlora = 0, contFauna;
	printf("\nIngrese pais a indicar: ");
	leerString(pais);

	contFauna = contadores(obtenerEspecies(paises, pais), contFlora, 0);

	printf("\nFlora en peligro de extincion: %d\n", contFlora);
	printf("Fauna en peligro de extincion: %d\n", contFauna);

	mas200peti(obtenerEspecies(paises, "brasil"));
	int cantTotal = contadorPeti(obtenerEspecies(paises, "argentina")) + contadorPeti(obtenerEspecies(paises, "brasil"));

	printf("La cantidad total de petiribi en brasil y argentina es %i\n", cantTotal);
}
