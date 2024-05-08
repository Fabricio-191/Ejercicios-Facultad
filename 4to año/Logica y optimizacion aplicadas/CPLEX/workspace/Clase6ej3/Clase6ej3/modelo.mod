/*********************************************
 * OPL 22.1.1.0 Model
 * Author: Usuario
 * Creation Date: 17 abr. 2024 at 18:55:46
 *********************************************/
{string} Bebidas = {"1","2","3"};
{string} Jugos = {"anana","durazno"};

float disp[Jugos] = [1500,2000];
float comp[Bebidas][Jugos] = [[6,3],[3,3],[3,4]];
float beneficio[Bebidas] = [15,14.999999,15];
float total_bebidas = 400;

dvar float+ cantBebidas[Bebidas];

maximize
	sum(b in Bebidas) beneficio[b]*cantBebidas[b];


subject to{
       C1: sum(b in Bebidas) cantBebidas[b]<=total_bebidas;
       C2: forall(j in Jugos)sum(b in Bebidas) cantBebidas[b]*comp[b][j]<=disp[j];
       //C3: sum(b in Bebidas) cantBebidas[b]*comp[b]["anana"]>=1500;
};

/*
1) No variaria la cantidad producida, ya que le minimo necesario es de 1200 de jugo de anana
2) Cambiaria la cantidad producida por: b1 100 b2 300 b3 0
3 y 4) A partir de 15.0001 es interesante producir tanto la bebida 1 y 3

*/