#include <stdio.h>
#include <windows.h>
#include <string.h>
typedef struct{
	char nom[30];
	int id;
	char dir[30];
	long int tel;
	int entrega;
	int mpago;
}rest;
typedef struct{
	rest r;
	int cantp;
	float impp;
}restaurante;
int main(){
	FILE *archi;
	archi=fopen("Restaurantes.dat", "w+");
	restaurante h;
	gets(h.r.dir); fflush(stdin);
	h.r.entrega=2;
	h.r.id=1;
	h.r.mpago=1;
	gets(h.r.nom);
	h.r.tel=264555655;
	fwrite(&h.r, sizeof(rest), 1, archi);
	fflush(NULL);
	fread(&h.r, sizeof(rest), 1, archi);
	printf("%s", h.r.nom);
	fclose(archi);
}
