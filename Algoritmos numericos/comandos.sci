
I = [1 0 0; 0 1 0; 0 0 1]; // Matriz identidad
I1 = [1; 0; 0];            // Primera columna de la matriz identidad
I2 = [0; 1; 0];            // Segunda columna de la matriz identidad
I3 = [0; 0; 1];            // Tercera columna de la matriz identidad

A'                // A traspuesta
inv(A)            // Matriz inversa de A
det(A)            // Determinante de A
spec(A)           // Autovalores de A
norm(A, normType) // Norma de A, normType = 1, 2, %inf
cond(A, normType) // Numero de condicion de A, normType = 1, 2, %inf


A \ b          // Resuelve el sistema Ax = b
A \ I  	       // Encuentra la inversa de A
A \ I1         // Primera columna de la inversa de A
A \ I2         // Segunda columna de la inversa de A
A \ I3         // Tercera columna de la inversa de A


[L, U] = lu(A) // Descomposicion LU de A
A == L * U     // Revisar que la descomposicion LU es correcta
U \ (L \ b)    // Resuelve el sistema L * (U * x) = b

U \ (L \ I)    // Encontrar la inversa de A con la descomposicion LU
U \ (L \ I1)   // Primera columna de la inversa de A
U \ (L \ I2)   // Segunda columna de la inversa de A
U \ (L \ I3)   // Tercera columna de la inversa de A


T = chol(A)    // Descomposicion de Cholesky de A
A == T' * T    // Revisar que la descomposicion de Cholesky es correcta
T \ (T' \ b)   // Resuelve el sistema L * (L' * x) = b

T \ (T' \ I)   // Encontrar la inversa de A con la descomposicion de Cholesky
T \ (T' \ I1)  // Primera columna de la inversa de A
T \ (T' \ I2)  // Segunda columna de la inversa de A
T \ (T' \ I3)  // Tercera columna de la inversa de A


