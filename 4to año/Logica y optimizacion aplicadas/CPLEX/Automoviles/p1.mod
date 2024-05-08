/*********************************************
 * OPL 22.1.0.0 Model
 * Author: Daniel
 * Creation Date: 16 abr. 2024 at 22:36:27
 
 
 Una f�brica de autom�viles produce dos modelos de coches: econ�mico (Modelo E) y de lujo (Modelo L).
 La producci�n de cada uno de estos modelos est� limitada por tres factores principales: 
 horas de trabajo, componentes plasticos, componentes metalicos,componentes electronicos  y capacidad de la l�nea de montaje.
 Las  tablas a continuacion establece los requerimientos de recurso de cada modelo y la disponibilidad de cada uno de ellos
 +---------------------------------+---------------------+---------------------+
| Descripci�n                     | Modelo E (Unidades) | Modelo L (Unidades) |
+---------------------------------+---------------------+---------------------+
| Horas de Trabajo Necesarias     | 10 horas            | 20 horas            |
| Componentes Pl�sticos           | 3 unidades          | 6 unidades          |
| Componentes Met�licos           | 7 unidades          | 14 unidades         |
| Componentes Electr�nicos        | 2 unidades          | 4 unidades          |
+---------------------------------+---------------------+---------------------+
La disponibilidad de recursos
+----------------------------------+---------------------+
| Recurso                          | Disponibilidad      |
+----------------------------------+---------------------+
| Horas de Trabajo                 | 800 horas           |
| Componentes Pl�sticos            | 240 unidades        |
| Componentes Met�licos            | 560 unidades        |
| Componentes Electr�nicos         | 160 unidades        |
| Capacidad de Producci�n Total    | 60 autos            |
+----------------------------------+---------------------+

 El modelo E es vendido  en $3000, mientras que el modelo L tiene un costo de $5000.
 Se desea conocer la cantidad optima de autos modelo E y modelo L que maximize los beneficios
 Ademas basados en esta solucion optima, se pide
   1- �C�mo afectar�a a la soluci�n �ptima un aumento del 10% en las horas de trabajo disponibles?
   2- Si el costo de los componentes plasticos (20$) aumenta en un 20%, �c�mo afectar�a esto a las ganancias totales bajo la soluci�n actual?
   3- �Cu�l es el rango de variabilidad en el precio de venta del Modelo L para que siga siendo rentable mantener la producci�n actual?
   */

dvar int+ modeloE;
dvar int+ modeloL;

maximize modeloE * 3000 + modeloL * 5000;

subject to {
	C1: modeloE * 10 + modeloL * 20 <= 800; // 800 - 880
	C2: modeloE * 3  + modeloL * 6  <= 240;
	C3: modeloE * 7  + modeloL * 14 <= 560;
	C4: modeloE * 2  + modeloL * 4  <= 160;
	C5: modeloE      + modeloL       <= 60;  
};

// modeloE = 40; modeloL = 20;   220000
// sale igual por que el limite superior de las horas es infinito
// las ganancias se reducen 960$ 
// entre 3000 (180000) y 6000 (240000)