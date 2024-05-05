/*********************************************
 * OPL 20.1.0.0 Model
 * Author: Daniel
 * Creation Date: 14 abr. 2021 at 18:38:26
 *********************************************/

// tomates, pimientos, espinacas
dvar float+ AcresTomate;
dvar float+ AcresPimientos;
dvar float+ AcresEspinacas;
dvar float+ diasHombres;

maximize 6 * AcresTomate + 12 * AcresPimientos + 10 * AcresEspinacas;

subject to
{
 //Restricción de días hombre disponibles 
 C1: 5 * AcresTomate + 8 * AcresPimientos + 13 * AcresEspinacas <= diasHombres; // solo hay 4000 dias hombres disponibles
 //Importe disponible para preparación
 C2: 12 * AcresTomate + 18 * AcresPimientos + 14 * AcresEspinacas <= 6000;  // se tiene un presupuesto de 6000 pesos para la preparacion
 //Restricción de acres de terreno disponibles
 C3: 1 * AcresTomate + 1 * AcresPimientos + 1 * AcresEspinacas <= 600; // el  tamaño de la finca es de 600 acres
 //AcresTomate>=200;
 AcresEspinacas>=196.72;
 AcresEspinacas<=196.72;
}
execute salida {
 if (cplex.getCplexStatus()==1){
 
   writeln ( "solucion: ", cplex.getObjValue());
  
  
   // solucion dual o shadow price
   
    writeln("precio sombra de C1 ", C1.dual);
    writeln("precio sombra de C2 ", C2.dual);
    writeln("precio sombra de C3 ", C3.dual);
  
    // sobrante surplus, lo que no se usa, aqui se puede ver los 
    // insumos con sobrante cero, que son los que pasan por el optimo
    writeln("slack de C1 ", C1.slack);
    writeln("slack de C2 ", C2.slack);
    writeln("slack de C3 ", C3.slack);
    // costo de oportunidad
    writeln("costos oportunidad de X1: ", AcresTomate.reducedCost);
    writeln("costos oportunidad de X2: ", AcresPimientos.reducedCost);
    writeln("costos oportunidad de X3: ", AcresEspinacas.reducedCost);
    writeln (" si produzco un acre de tomates el beneficio deberia ser : ", cplex.getObjValue()+AcresTomate.reducedCost);
     writeln ("Para producir tomates el precio debe superior a :", (( -1)*(AcresTomate.reducedCost -6 )));

}
}  