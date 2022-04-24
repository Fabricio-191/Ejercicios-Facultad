#include "tipos.h"
static void cuenta(restaurante *r, int tam, int i, float a){
	if(i<tam){
		printf("\n\t-Restaurante %s: %.2f",r[i].r.nom, r[i].impp*0.05);
		cuenta(r, tam, i+1, a+r[i].impp);
	}else printf("\n\n->Total vendido por la plataforma: $ %.2f \n\n", a);
}
void cierre(float h[6], restaurante *r, int tam){
	system("cls");
	printf("\n El metodo de pago mas usado por los clietes es: ");
	if(h[2]>h[3]) printf("Tarjeta");
	else printf("Efectivo");
	printf("\n El metodo de entrega mas usado por los clietes es: ");
	if(h[0]>h[1]) printf("Delivery");
	else printf("Pick Up");
	printf("\nEl mayor importe recaudado es: %.2f", h[4]);
	printf("\nEl menor importe recaudado es: %.2f", h[5]);
	printf("\n****Recaudaciones****");
	cuenta(r, tam, 0, 0);
	system("pause");
}
