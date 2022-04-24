#include "tipos.h"
void backup(restaurante *r, empleado *e, int tamr, int tame, nodo *xp){
	FILE *archi;
	if((archi=fopen("Respaldo.txt", "w"))!=NULL){
		fprintf(archi, " ***************Pedidos Pendientes*************** \n");
		while(xp!=NULL){
			fprintf(archi, "Pedido de %s: \n\t -Empleado: %d \n\t -Cliente: %d \n\t -Restaurante: %d \n\t -Importe: %.2f \n ", xp->l.alimento, xp->l.idemp, xp->l.idcli, xp->l.idrest, xp->l.total);
			xp=xp->sig;}
		int i;
		fprintf(archi, "\n ***************Restaurantes*************** \n ");
		for(i=0; i<tamr; i++)
			fprintf(archi,"Restaurante %s:\n\t -ID: %d \n\t -Direccion: %s\n\t -Tel: %ld\n\t -Pedidos Pendientes: %d\n\t -Importe: %.2f \n", r[i].r.nom, r[i].r.id, r[i].r.dir, r[i].r.tel, r[i].cantp, r[i].impp);
		fprintf(archi, "\n ***************Empleados*************** \n ");
		for(i=0; i<tame; i++)
			fprintf(archi,"Empleado %s:\n\t -ID: %d \n\t -DNI: %ld\n\t -Tel: %ld\n\t -Pedidos Pendientes: %d \n", e[i].a.nom, e[i].a.cod, e[i].a.dni, e[i].a.telf, e[i].cantp);
		fclose(archi);
		printf("Respaldo realizado");
	}else printf("\nError al realizar el respaldo");
}
