#include "tipos.h"
void listado(restaurante *r, int tam, int i, int cod, int t){
if(i<tam){	
	switch(cod){
		case 3:
			printf("\n -> %d. %s", i+1, r[i].r.nom );
			listado(r, tam, i+1, cod, t);
			break;
		case 4:
			printf("\n -> %d. %s tiene %d pedidos", i+1, r[i].r.nom, r[i].cantp);
			listado(r, tam, i+1, cod, t);
			break;
		case 5:
			printf("\n -> %d. %s recibe: ", i+1, r[i].r.nom);
			switch(r[i].r.mpago){
				case 1: printf("\n Tarjetas");
				break;
				case 2: printf("\n Efectivo");
				break;
				case 3: printf("\n Tarjetas y Efectivo");
				break;}
				listado(r, tam, i+1, cod, t);
				break;
		case 6:
			if(r[i].r.entrega ==t || r[i].r.entrega==3){
				printf("\n Datos de %s: \n -ID: %d \n -Direccion %s \n -Telefono %ld ", r[i].r.nom, r[i].r.id, r[i].r.dir, r[i].r.tel);
			}
			listado(r, tam, i+1, cod, t);
		}
	}
}	
