#include "tipos.h"
void listado(){
	FILE *archi;
	cliente c;
	if((archi=fopen("Clientes.dat", "rb"))!=NULL){
		while(fread(&c, sizeof(cliente), 1, archi))
		printf("\n\t -> %d. %s", c.id-99, c.nom );
		printf("\n Total de clientes: %d", c.id-99);
	}else printf("Error al abrir el archivo");
	fclose(archi);
}
