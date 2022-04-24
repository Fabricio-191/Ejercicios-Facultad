#include "tipos.h"
static void cargaarreglo(restaurante *&r, empleado *&e, int a, int &tam){
	FILE *archi;
	fpos_t x;
	if(a){
		if((archi=fopen("Restaurantes.dat", "a+"))!=NULL){
			fseek(archi, 0, 2);
			fgetpos(archi, &x);
			tam=(int) x/sizeof(rest);
			r= (restaurante *)calloc(tam, sizeof(restaurante));
			rewind(archi);
			int i=0;
			while(fread(&r[i].r, sizeof(rest), 1, archi)) 
			i++;
			fclose(archi);
		}else printf("Error al abrir el archivo");
	}
	else{
		if((archi=fopen("Empleados.dat", "a+"))!=NULL){
			fseek(archi, 0, 2);
			fgetpos(archi, &x);
			tam=(int)x/sizeof(emp);
			e=(empleado *)calloc(tam, sizeof(empleado));
			rewind(archi);
			int i=0;
			while(fread(&e[i].a, sizeof(emp), 1, archi))
			i++;
			fclose(archi);
			}else printf("Error al abrir el archivo");	
	}
}
static void altaemp(){
	int a;
	do{
			emp l;
			printf("\nIngrese nombre y apellido del empleado: ");
			fflush(stdin);
			gets(l.nom);
			printf("\nIngrese DNI: ");
			scanf("%ld", &l.dni);
			printf("\nIngrese Numero telefonico: ");
			scanf("%ld", &l.telf);
			FILE *archi;
			if((archi=fopen("Empleados.dat", "ab"))!=NULL){
				fpos_t x;
				fseek(archi, 0, 2);
				fgetpos(archi, &x);
				l.cod=(int) x/sizeof(emp)+1;
				fwrite(&l, sizeof(emp), 1, archi);
				fclose(archi);
				printf("\nEmpleado agregado correctamente ");
				printf("\nCodigo del empleado %d ", l.cod);
			}else printf("Error al añadir el empleado");
			printf("\n Desea dar de alta a otro empleado? \n0). No \n1). Si \nIngrese opcion:  ");
			scanf("%d", &a);
		}while (a);
		system("cls");
}
static void altarest(){ 
	int a;
	do{
			rest l;
			printf("\nIngrese nombre del restaurante: ");
			fflush(stdin);
			gets(l.nom);
			printf("\nIngrese direccion: ");
			fflush(stdin);
			gets(l.dir);
			printf("\nIngrese tipo de entrega (Si posee ambos ingrese 3): ");
			scanf("%d", &l.entrega);
			printf("\nIngrese metodo de pago disponible (Si posee ambos ingrese 3): ");
			scanf("%ld", &l.mpago);
			printf("\nIngrese Numero telefonico: ");
			scanf("%ld", &l.tel);
			FILE *archi;
			if((archi=fopen("Restaurantes.dat", "ab"))!=NULL){
				fpos_t x;
				fseek(archi, 0, SEEK_END);
				fgetpos(archi, &x);
				l.id=(int) (x/sizeof(rest))+1;
				fwrite(&l, sizeof(rest), 1, archi);
				fclose(archi);
				printf("Codigo del restaurante: %d", l.id);
				printf("\nRestaurante agregado correctamente %c", 1);
			}else printf("Error al añadir el empleado");
			printf("Desea dar de alta a otro restaurante? \n0). No \n1). Si \nIngrese opcion:  ");
			scanf("%d", &a);
		}while (a);	
		system("cls");	
}
static void reasigna(emp *r, int tam, int i, int e){
	if(i<tam){
		if(r[i].cod){
			r[i].cod=e;
			reasigna(r, tam, i+1, e+1);
		}else reasigna(r, tam, i+1, e);
	}
}
static void bajarest(){
	int cod;
	printf("Ingrese el codigo del resturante a dar de baja: ");
	scanf("%d", &cod);
	FILE *archi;
	int tam, i, e=1;
	fpos_t x;
	if((archi=fopen("Restaurantes.dat", "r+"))!=NULL){
		fseek(archi, 0, 2);
		fgetpos(archi, &x);
		tam=(int) x/sizeof(rest);
		rest *r=(rest *)malloc(sizeof(rest)*tam);
		rewind(archi);
		fread(r, sizeof(rest), tam, archi);
		fclose(archi);	
		r[cod-1].id=0;
		if((archi=fopen("auxiliar.dat", "wb"))!=NULL){	
		for(i=0; i<tam; i++){
			if(r[i].id){
			r[i].id=e;
			fwrite(&r[i], sizeof(rest), 1, archi);
			e++;}
			}}		
		fclose(archi);
		remove("Restaurantes.dat");
		rename("auxiliar.dat", "Restaurantes.dat");	
		printf("Restaurante %s eliminado \n", r[cod-1].nom);
		free(r);
	}else printf("Error al abrir el archivo");
}
static void bajaemp(){
	int cod;
	printf("Ingrese el codigo del empleado a dar de baja: ");
	scanf("%d", &cod);
	FILE *archi;
	int tam, i, e=1;
	fpos_t x;
	if((archi=fopen("Empleados.dat", "r+"))!=NULL){
		fseek(archi, 0, 2);
		fgetpos(archi, &x);
		int tam=(int) x/sizeof(emp);
		emp *r=(emp *)malloc(sizeof(emp)*tam);
		rewind(archi);
		fread(r, sizeof(emp), tam, archi);
		fclose(archi);	
		r[cod-1].cod=0;
		if((archi=fopen("auxiliar.dat", "wb"))!=NULL){	
		for(i=0; i<tam; i++){
			if(r[i].cod){
			r[i].cod=e;
			fwrite(&r[i], sizeof(emp), 1, archi);
			e++;}
			}		
		}
		fclose(archi);
		remove("Empleados.dat");
		rename("auxiliar.dat", "Empleados.dat");	
		printf("empleado %s eliminado \n", r[cod-1].nom);
		free(r);
		system("pause");
		system("cls");
	}else printf("Error al abrir el archivo");
}
void inicio(restaurante *&r, empleado *&e, int &tamr, int &tame){
	int a;
	do{
		printf("\n1). Dar de alta un Restaurante \n2). Dar de alta un Empleado \n3). Dar de baja un Restaurante \n4). Dar de baja un Empleado\n0). Salir \nIngrese opcion: ");
		scanf("%d", &a);
		switch(a){
			case 1:
				altarest();
				break;
			case 2:
				altaemp();
				break;
			case 3:
				bajarest();
				break;
			case 4:
				bajaemp();
				break;	
				}
	}while(a);	
	cargaarreglo(r,e,1, tamr);
	cargaarreglo(r,e,0, tame);
}	

