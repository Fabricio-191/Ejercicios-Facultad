#ifndef tipo
#define tipo
#include <stdio.h>
#include <windows.h>
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
typedef struct{
	int cod;
	char nom[30];
	long int dni;
	long int telf;
}emp;
typedef struct{
	emp a;
	int cantp;
}empleado;
typedef struct{
	int idcli;
	int idrest;
	int idemp;
	char alimento[50];
	float total;
	int fpago;
	int tiempoe;
	int tipoe;
}pedido;
typedef struct nodo{
	pedido l;
	nodo *sig; 
}nodo;
typedef struct{
	char nom[30];
	int id;
	char dir[30];
	long int telf;
	int cupon;
}cliente;

void inicio(restaurante *&r, empleado *&e, int &tamr, int &tame);
void cargapedido(nodo *&cabeza, empleado *emple, restaurante *resta, int tamr, int tame, float h[6]);
void eliminarp(nodo *&cabeza, empleado *emple, restaurante *resta);
void listado(restaurante *r, int tam, int i, int cod, int t);
void backup(restaurante *r, empleado *e, int tamr, int tame, nodo *xp);
void cierre(float h[6], restaurante *r, int tam);
void empleados(empleado *r, int tam, nodo *xp);
void listado();
#endif
