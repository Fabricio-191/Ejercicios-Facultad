#include <stdio.h>
#include <malloc.h>

struct inqui {
	float importe;
	char nom[40], cel[12];
	int nrod, pago; /*(1 - pagó, 2 - No pagó)*/
};

struct nodo{
	inqui inquilino;
	nodo* next;
};

int cargarInquilinos(FILE* archivo, inqui* &inq){
	fpos_t size;
	fseek(archivo, 0, SEEK_END);
	fgetpos(archivo, &size);

	int cant = size / sizeof(inqui);

	rewind(archivo);
	inq = (inqui*) malloc(size);
	fread(inq, sizeof(inqui), cant, archivo);

	return cant;
}

void actualizarArchivo(){
	FILE* archivo = fopen("deptos.dat", "rwb");

	int num;
	printf("Introduzca el numero de dpto a actualizar\n");
	scanf("%d", &num);

	fseek(archivo, (num - 1) * sizeof(inqui), SEEK_SET);
	inqui inq;
	fread(&inq, sizeof(inqui), 1, archivo);

	float importe;
	printf("Introduzca el nuevo importe\n");
	scanf("%f", &inq.importe);

	fseek(archivo, -sizeof(inqui), SEEK_CUR);

	fwrite(&inq, sizeof(inqui), 1, archivo);
	fclose(archivo);
}

void recaudacionTotal(inqui* inq, int cant){
	float acum = 0;

	for(int i = 0; i < cant; i++){
		if(inq[i].pago == 1){
			acum += inq[i].importe;
		}
	}

	printf("El total recaudado hasta ahora es: %f\n", acum);
}

nodo* crearLista(inqui* inq, int cant){
	nodo* cabeza = (nodo*) malloc(sizeof(nodo));
	cabeza->next = NULL;

	for(int i = 0; i < cant; i++){
		if(inq[i].pago == 2){
			nodo* nuevo = (nodo*) malloc(sizeof(nodo));

			nuevo->inquilino = inq[i];
			nuevo->next = cabeza->next;
			cabeza->next = nuevo;
		}
	}

	return cabeza;
}	

void eliminarDepto(nodo* nod, int num){
	if(nod->next == NULL) return;

	if(nod->next->inquilino.nrod == num){
		nodo* temp = nod->next;

		nod->next = nod->next->next;
		free(temp);
		eliminarDepto(nod, num);
	}else eliminarDepto(nod->next, num);
}

int main(){
	FILE* archivo = fopen("deptos.dat", "rb");

	inqui* inq = NULL;
	int cant = cargarInquilinos(archivo, inq);

	actualizarArchivo();

	recaudacionTotal(inq, cant);
	nodo* cabeza = crearLista(inq, cant);

	int num;
	printf("Introduzca el numero de dpto a eliminar\n");
	scanf("%d", &num);
	eliminarDepto(cabeza, num);

	return 0;
}