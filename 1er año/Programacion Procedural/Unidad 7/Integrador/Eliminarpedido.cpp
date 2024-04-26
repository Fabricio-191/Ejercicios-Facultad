#include "tipos.h"
void eliminarp(nodo *&cabeza, empleado *emple, restaurante *resta){
		if(cabeza == NULL){
		printf("No hay pedidos pendientes \n");
		return;
	}	
	int cod;
	printf("Ingrese el codigo del empleado: ");
	scanf("%d", &cod);
	nodo *xp, *anterior;
	if(cabeza->l.idemp == cod){
		xp=cabeza;
		cabeza=cabeza->sig;
		printf("Pedido de %s fue entregado por %s \n", xp->l.alimento, emple[cod-1].a.nom );
		emple[cod-1].cantp--;
		resta[xp->l.idrest-1].cantp--;
		free(xp);
	}else{
		xp=cabeza;
		anterior=cabeza;
		while(xp !=NULL && xp->l.idemp != cod){
			anterior=xp;
			xp=xp->sig;
		}
		if(xp!=NULL){
			anterior->sig=xp->sig;
			printf("Pedido de %s fue entregado por %s \n", xp->l.alimento, emple[cod-1].a.nom );
			emple[cod-1].cantp--;
			resta[xp->l.idrest-1].cantp--;
			free(xp);
		}else {
			printf("No se encontro algun pedido para %s \n", emple[cod-1].a.nom); 
		}
}
}
