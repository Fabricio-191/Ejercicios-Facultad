/*********************************************
 * OPL 22.1.0.0 Model
 * Author: Daniel
 * Creation Date: 17 abr. 2024 at 10:39:46
 ********************************************
 
 Una floristeria popular desea optimizar su produccion de ramos de flores. 
 El due�o ha identificado tres tipos principales de ramos seg�n el evento al cual est�n dirigidos: Bodas, Cumplea�os y Aniversarios.
 La florister�a cuenta con ocho variedades de flores, y cada tipo de ramo requiere una combinaci�n espec�fica de estas variedades.
 Rosas, Tulipanes, Lirios, Orqu�deas, Margaritas, Girasoles, Claveles, Peon�as.
 
 Tabla de recursos requeridos por tipo de ramo
+----------------+--------+-----------+-----------+----------+------------+---------+---------+----------+----------+-
| Tipo de Ramo   | Rosas  | Tulipanes | Lirios    | Orqu�deas| Margaritas | Girasoles| Claveles| Peon�as  | Mano de  |
|                |        |           |           |          |            |          |         |          | obra (h) | 
+----------------+--------+-----------+-----------+----------+------------+----------+---------+----------+----------+
| Bodas (B)      | 4      | 0         | 0         | 2        | 0          | 0        | 0       | 3        | 1.5      | 
| Cumplea�os (C) | 0      | 3         | 0         | 0        | 2          | 2        | 0       | 0        | 1.0      | 
| Aniversarios (A)| 1     | 0         | 3         | 0        | 0          | 0        | 2       | 0        | 1.2      | 
+----------------+--------+-----------+-----------+----------+------------+----------+---------+----------+----------+

Para realizar cada todos estos tipos de ramos se dispone de las siguientes flores
+----------------+------------------+
| Variedad       | Disponibilidad   |
+----------------+------------------+
| Rosas          | 120 unidades     |
| Tulipanes      | 100 unidades     |
| Lirios         | 80 unidades      |
| Orqu�deas      | 60 unidades      |
| Margaritas     | 90 unidades      |
| Girasoles      | 70 unidades      |
| Claveles       | 110 unidades     |
| Peon�as        | 50 unidades      |
+----------------+-----------------+
Adem�s, la florister�a dispone de 180 horas de mano de obra cada d�a para la preparaci�n de los ramos.
-
Los ramos de Bodas se venden a $60 , los de Cumplea�os a $40 y los de Aniversarios a $50.
Se necesita saber 
 1 - �cuantos ramos de cada tipo se necesitan producir para maximizar el beneficio?
 2- En un escenario de mercado donde existe una alta variabilidad en la disponibilidad de rosas como impactaria
 en los beneficios si la disponibilidad de rosas aumnenta o disminuye.
 3- El costo actual de mano de obra es $10 pesos por hora, conviene contratar mas horas de mano de obra ?. Justifique 
 4- ¿Cual seria el efecto en la produccion si la disponibilidad de margaritas disminuye a 70 unidades por dia?
     Investiga como una reduccion en el suministro de un tipo de flor afecta la capacidad de la floristeria para cumplir
     con la demanda de ramos para cumpleanios, que usan margaritas.
  5 Como afecta a de ramos producidos de Cumpleanios si el precio de los ramos para aniversario se incrementa en un 20% 
  


 */
 
 //datos
 {string} Ramos = {"Bodas","Cumpleanio","Aniversario"};
 {string} Flores = {"Rosas", "Tulipanes", "Lirios", "Orquideas", "Margaritas", "Girasoles", "Claveles", "Peonias"};
 
 float comp[Ramos][Flores] = [[4,0,0,2,0,0,0,3],[0,3,0,0,2,2,0,0],[1,0,3,0,0,0,2,0]];
 float mano_de_obra[Ramos] = [1.5,1.0,1.2];
 float disp[Flores] = [120,100,80,60,90,70,110,50];
 float beneficios[Ramos] = [60,40,50];
 float total_hrs = 180;
 
 //funcion
 dvar float+ cantRamos[Ramos];
 
 maximize 
 sum(r in Ramos) beneficios[r]*cantRamos[r];
 
 //restricciones
 
 subject to{
   C1: forall(f in Flores) sum(r in Ramos) cantRamos[r]*comp[r][f] <= disp[f];
   C2:	sum(r in Ramos) mano_de_obra[r]*cantRamos[r]<= total_hrs;
 };
 
 /**1)
 cant ramos:
 16.667 boda
 33.333 cumpleanio
 26.667 aniversario
 
 2)La cantidad de rosas puede aumentar infinitamente, ya que no tiene shadow price. Es decir no hay escases de rosas
 y se necesitaria siempre un minimo de 93.333 rosas
 
 3)La mano de obra no teine shadow price es deicr no se ocupa toda, por lo tanto no es conveniente aumentarla.
 
 4) El minimo de margaritas necesarias es de 66.6667 por lo tanto con 70 se cumpliria la necesidad de los ramos de cupleanios
  y no habira escases de los mismos.
  
  5) El precio de los ramos de aniversario no ninfluyen en la cantidad de ramos de boda producidos.
  Solo aumenta el valor de la funcion objetivo. Esto ya que no tienen maximo permitido.
 **/