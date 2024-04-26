/*********************************************
 * OPL 20.1.0.0 Model
 * Author: Daniel
 * Creation Date: 10 may. 2023 at 18:24:45
 *********************************************/
// tomates, pimientos, espinacas
dvar float+ AcresTomate;
dvar float+ AcresPimientos;
dvar float+ AcresEspinacas;


maximize 6 * AcresTomate + 12 * AcresPimientos + 10 * AcresEspinacas;

subject to
{
 //Restricción de días hombre disponibles 
 C1: 5 * AcresTomate + 8 * AcresPimientos + 13 * AcresEspinacas <= 4000; // solo hay 4000 dias hombres disponibles
 //Importe disponible para preparación
 C2: 12 * AcresTomate + 18 * AcresPimientos + 14 * AcresEspinacas <= 6000;  // se tiene un presupuesto de 6000 pesos para la preparacion
  //Restricción de acres de terreno disponibles
 C3: 1 * AcresTomate + 1 * AcresPimientos + 1 * AcresEspinacas <= 600; // el  tamaño de la finca es de 600 acres
}