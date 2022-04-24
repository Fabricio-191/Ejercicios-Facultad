#include "tipos.h"
#include <malloc.h>
static nodo* recorre(nodo *xp){
	if(xp->sig !=NULL){
		return recorre(xp->sig);
	}else return xp;}
int buscaempleado(empleado *emple, int tam, int cont, int min, int aux){
	if(cont<tam){
		if(emple[cont].cantp<min){
			return buscaempleado(emple, tam, cont+1, emple[cont].cantp, emple[cont].a.cod);
			
		}else return buscaempleado(emple, tam, cont+1, min, aux);
	}
	else return aux;
}
static void crealist(nodo *&cabeza, cliente &l, empleado *emple, restaurante *resta, int tamr, int tame, float h[6]){
	nodo *nuevo;
	nuevo=(nodo*)malloc(sizeof(nodo));
	nuevo->sig=NULL;
	if(cabeza==NULL){
		cabeza=nuevo;
	}else{
	nodo *xp=recorre(cabeza);
	xp->sig=nuevo;
	}
	printf("\nIngrese el alimento a consumir: ");
	fflush(stdin);
	gets(nuevo->l.alimento);
	nuevo->l.idcli=l.id;
	printf("\nIngrese nombre del restaurante: ");
	fflush(stdin);
	char aux[30];
	int i=0;
	gets(aux);
	while(stricmp(aux, resta[i].r.nom)){
		i++;}
	nuevo->l.idrest=resta[i].r.id;
	printf("\nTipos de entrega disponibles para %s: ", aux);
	switch(resta[i].r.entrega){
		case 1: printf("\n1. Delivery"); break;
		case 2: printf("\n2. Pick Up"); break;
		case 3: printf("\n1. Delivery\n2. Pick Up"); break;
	}
	printf("\nIngrese tipo de entrega: ");
	scanf("%d", &nuevo->l.tipoe);
	if(nuevo->l.tipoe == 1){h[0]++;} 
	else {h[1]++;}
	printf("\nIngrese el importe del pedido: ");
	scanf("%f", &nuevo->l.total);
	if(l.cupon){nuevo->l.total = nuevo->l.total/1.10; l.cupon=0;}
	if(nuevo->l.total>h[4]){h[4]=nuevo->l.total;} 
	if(nuevo->l.total<h[5]){h[5]=nuevo->l.total;} 
	if(nuevo->l.total>4000){l.cupon=1;} 
	printf("El importe a pagar por el cliente es: %.2f", nuevo->l.total);
	printf("\nMetodos de pago disponibles para %s: ", aux);
	switch(resta[i].r.mpago){
		case 1: printf("\n1. Tarjeta"); break;
		case 2: printf("\n2. Efectivo"); break;
		case 3: printf("\n1. Tarjeta\n2. Efectivo"); break;
	}

	printf("\nIngrese metodo de pago: ");
	scanf("%d", &nuevo->l.fpago);
	if(nuevo->l.fpago == 1) h[2]++;
	else h[3]++;
	nuevo->l.idemp=buscaempleado(emple, tame, 0, 5, 0);
	emple[nuevo->l.idemp-1].cantp++;
	resta[nuevo->l.idrest-1].cantp++;
	nuevo->l.tiempoe=emple[nuevo->l.idemp-1].cantp*15;
	resta[i].impp+=nuevo->l.total;
	printf("El pedido %s sera entregado en %d mins", nuevo->l.alimento, nuevo->l.tiempoe);
	printf (" por el empleado %s id %d ", emple[nuevo->l.idemp-1].a.nom, nuevo->l.idemp);
	printf("\nal cliente %s con id %d ", l.nom, l.id);
	}
void cargapedido(nodo *&cabeza, empleado *emple, restaurante *resta, int tamr, int tame, float h[6]){
	int id;
	printf("Ingrese ID del cliente: ");
	scanf("%d", &id);
	id-=100;
	cliente cli;
	FILE *archi;
//	if((archi=fopen("Clientes.dat", "wb"))!=NULL){fclose(archi);}
	if((archi=fopen("Clientes.dat", "r+"))!=NULL){
		fseek(archi, sizeof(cliente)*id, SEEK_SET);
		if(!fread(&cli, sizeof(cliente), 1, archi)){ //si hubo error al buscar
			printf("\nEl cliente no se encuetra en el sistema");
			printf("\nIngrese el nombre del cliente: ");
			fflush(stdin);
			gets(cli.nom);
			printf("\nIngrese direccion del cliente: ");
			fflush(stdin);
			gets(cli.dir);
			printf("\nIngrese numero de telefono: ");
			scanf("%ld", &cli.telf);
			cli.cupon=0; 
			fseek(archi, 0, 2);
			fpos_t x;
			fgetpos(archi, &x);
			cli.id=100+(int) x/sizeof(cliente);
			fwrite(&cli, sizeof(cliente), 1, archi);
			printf("\nCodigo de cliente: %d \n", cli.id);
			crealist(cabeza, cli, emple, resta, tamr, tame, h);
			fseek(archi, sizeof(cliente)*id, 0);
			fwrite(&cli, sizeof(cliente), 1, archi);
			fclose(archi);
		}
		else {
		crealist(cabeza, cli, emple, resta, tamr, tame, h);
		fseek(archi, sizeof(cliente)*-1, SEEK_CUR);
		fwrite(&cli, sizeof(cliente), 1, archi);
		fclose(archi);
		}
	}else printf("\nError al abrir el archivo");
}
