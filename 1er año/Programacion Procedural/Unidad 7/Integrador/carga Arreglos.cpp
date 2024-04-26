#include "tipos.h"
#include <malloc.h>
void* cargaarreglo(int a, int &tam){
	FILE *archi;
	fpos_t x;
	if(a){
		if((archi=fopen("Restaurantes.dat", "a+"))!=NULL){
			fseek(archi, 0, 2);
			fgetpos(archi, &x);
			tam=(int) x/sizeof(rest);
			restaurante *p= (restaurante *)calloc(tam, sizeof(restaurante));
			rewind(archi);
			int i=0;
			while(fread(&p[i].r, sizeof(rest), 1, archi)) 
			i++;
			fclose(archi);
			return p;
		}else printf("Error al abrir el archivo");
	}
	else{
		if((archi=fopen("Empleados.dat", "a+"))!=NULL){
			fseek(archi, 0, 2);
			fgetpos(archi, &x);
			tam=(int)x/sizeof(emp);
			empleado *p=(empleado *)calloc(tam, sizeof(empleado));
			rewind(archi);
			int i=0;
			while(fread(&p[i].a, sizeof(emp), 1, archi))
			i++;
			fclose(archi);
			return p;
			}else printf("Error al abrir el archivo");	
	}
}
