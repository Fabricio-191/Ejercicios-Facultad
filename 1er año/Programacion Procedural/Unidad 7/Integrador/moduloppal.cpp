#include "tipos.h"
int main(){
int op, tame, tamr;
restaurante *resta;
empleado *emple;
inicio(resta, emple, tamr, tame);
nodo *cabeza;
cabeza=NULL;
float h[6]={0,0,0,0,0,99999};
do{
	printf("\n");
	system("pause");
	system("cls");
	printf(" 1. Ingresar pedido\n 2. Eliminar pedido ");
	printf("\n 3. Listado de restaurantes \n 4. Cantidad de pedidos de cada restaurante\n 5. Cantidad de restaurantes con metodo de pago ");
	printf("\n 6. Restaurantes por tipo de entrega \n 7. Respaldo de la informacion \n 8. Listado de clientes \n 9. Pedidos del empleado \n 0. Salir");
	printf("\n Ingrese opcion: ");
	scanf("%d", &op);
	switch(op){
		case 1:
			cargapedido(cabeza, emple, resta, tamr, tame, h);
			break;	
		case 2:
			eliminarp(cabeza, emple, resta);
			break;
		case 3:
			listado(resta, tamr, 0, op, 0);
			break;
		case 4:
			listado(resta, tamr, 0, op, 0);
			break;
		case 5:
			listado(resta, tamr, 0, op, 0);
			break;
		case 6:
			printf("\n 1. Delivery \n 2. Pick Up\nIngrese el tipo de entrega: ");
			int h;
			scanf("%d", &h);
			listado(resta, tamr, 0, op, h);
			break;
		case 7:
			backup(resta, emple, tamr, tame, cabeza);
			break;
		case 8:
			listado();
			break;
		case 9:
			empleados(emple, tame, cabeza);
			break;
		case 0: if(!op && cabeza!=NULL){
				printf("Hay pedidos pendientes por entregar");
				op=1;
			}
			break;
	}
}while(op);
cierre(h, resta, tamr);
free(resta);
free(emple);
resta=NULL;
emple=NULL;
}
