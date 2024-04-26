#include "tipos.h"
static void busca(nodo *x, int cod){
	if(x!=NULL){
		if(x->l.idemp==cod){
			printf("\n -> %s por un importe de %.2f a entregarse en %d mins", x->l.alimento, x->l.total, x->l.tiempoe);
			busca(x->sig, cod);
		}busca(x->sig, cod);
	}		
}
void empleados(empleado *r, int tam, nodo *xp){
	printf("Ingrese DNI del empleado: ");
	long int dni;
	int i=0;
	scanf("%ld", &dni);
	while(r[i].a.dni!=dni&&i<tam)
	i++;
	if(i>tam) printf("No se encontro el empleado");
	printf("El empleado %s tel: %ld", r[i].a.nom, r[i].a.telf);
	printf("\nTiene los siguientes pedidos: ");
	busca(xp, r[i].a.cod);
}
