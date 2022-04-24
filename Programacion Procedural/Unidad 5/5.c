#include <stdio.h>
#include <malloc.h>

struct nodo {
    int valor;
    struct nodo *next;
};
typedef struct nodo* nodo_t;

nodo_t carga(){
	int valor;
	printf("Introduzca el valor a guardar (0 para terminar)\n\e[33m");
	scanf("%i", &valor);
	printf("\e[0m");

	while(valor < 0){
		printf("El valor introducido es incorrecto, introduzca denuevo:\n\e[33m");
		scanf("%i", &valor);
		printf("\e[0m");
	}

	if(valor == 0) return NULL;

	nodo_t nodo = (nodo_t) malloc(sizeof(struct nodo));
	nodo->valor = valor;
	nodo->next = carga();

	return nodo;
}

void ordenar(nodo_t nodo){
    nodo_t k, p, cota = NULL;

    int aux;
    while (k != nodo){
        k = p = nodo;

        while (p->next != cota){
            if (p->valor > p->next->valor){
                aux = p->next->valor;
                p->next->valor = p->valor;
                p->valor = aux;
                k = p;
            };
            p = p->next;
        }

        cota = k->next;
    }
}

void ultimoPar(nodo_t nodo){
	if(nodo->next == NULL && (nodo->valor % 2) == 0){
		printf("\nEl ultimo numero de la lista es par");
		return;
	}
	ultimoPar(nodo->next);
}

void mostrar(nodo_t nodo, int i){
	if(nodo == NULL) return;

	printf("Nodo: \e[31m%i\e[0m valor: \e[33m%i\e[0m\n", i, nodo->valor);
	mostrar(nodo->next, i + 1);
}

void freeLista(nodo_t nodo){
	if(nodo->next != NULL) freeLista(nodo->next);
	free(nodo);
}

int main(){
	nodo_t primerNodo = carga();
	printf("\n");

	ordenar(primerNodo);
	mostrar(primerNodo, 1);

	freeLista(primerNodo);
	return 0;
}

/*
puntero aux = (puntero) malloc(sizeof(struct nodo));
60
-5
10
50
20
30
0

*/
