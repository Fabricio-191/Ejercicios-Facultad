/*********************************************
 * OPL 22.1.1.0 Model
 * Author: Fabricio
 * Creation Date: 13 abr. 2024 at 21:54:02
 *********************************************/
dvar int x;
dvar int y; 
int a = Math.log(1)

// minimize 1 - (2^x + 3^y);
minimize 1 - (math.pow(2, x) + math.pow(3, y));


subject to {
  x <= 10;
  x >= -10;
  
  y <= 10;
  y >= -10;
}