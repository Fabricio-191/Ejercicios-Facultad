/*********************************************
 * OPL 22.1.1.0 Model
 * Author: Usuario
 * Creation Date: 13 abr. 2024 at 17:30:28
 *********************************************/
dvar float+ Tomates ;
dvar float+ Pimientos ;
dvar float+ Espinacas ;

maximize
  6*Tomates + 12*Pimientos + 10*Espinacas ;
 
 subject to{
   C1: 5*Tomates + 8*Pimientos + 13*Espinacas <= 4000;
   C2: 12*Tomates + 18*Pimientos + 14*Espinacas <= 6000;
   C3: Tomates + Pimientos + Espinacas <=600;
   //C4: Tomates >=200;
 };