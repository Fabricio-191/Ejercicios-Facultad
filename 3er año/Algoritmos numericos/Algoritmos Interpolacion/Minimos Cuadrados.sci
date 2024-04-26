// X = [0, 1, 2, 3, 4, 5]; Y = [5, 25, 130, 340, 375, 375];
// X = [  1, 2,   3,    4,    5,    6,  7,    8,    9,   10];
// Y = [5.1, 7, 8.9, 11.1, 13.2, 14.8, 17, 18.9, 21.1, 23.1];
X = [-1 0 0.5 1]; Y = [1 3 0 4];


// Grado 1 (lineal)
A1 = [
    sum(X.^0) sum(X.^1);
    sum(X.^1) sum(X.^2)
];
b1 = [sum(Y .* X .^ 0); sum(Y .* X .^ 1)];
Z1 = A1 \ b1
polinomio_1 = Z1(1) + Z1(2) * X
vector_errores_1 = polinomio_1 - Y
error_1 = sqrt(sum(vector_errores_1 .^ 2))
var_1 = sum(vector_errores_1 .^ 2) / (length(X) - 2)
condicion_1 = cond(A1)


// Grado 2 (cuadratica)
A2 = [
    sum(X.^0) sum(X.^1) sum(X.^2);
    sum(X.^1) sum(X.^2) sum(X.^3);
    sum(X.^2) sum(X.^3) sum(X.^4)
];
b2 = [sum(Y .* X .^ 0); sum(Y .* X .^ 1); sum(Y .* X .^ 2)];
Z2 = A2 \ b2
polinomio_2 = Z2(1) + Z2(2) * X + Z2(3) * X.^2
vector_errores_2 = polinomio_2 - Y
error_2 = sqrt(sum(vector_errores_2 .^ 2))
var_2 = sum(vector_errores_2 .^ 2) / (length(X) - 3)
condicion_2 = cond(A2)


X = [-1 0 0.5 1];
Y = [1 3 0 4];

// Grado 3
A3 = [
    sum(X.^0) sum(X.^1) sum(X.^2) sum(X.^3);
    sum(X.^1) sum(X.^2) sum(X.^3) sum(X.^4);
    sum(X.^2) sum(X.^3) sum(X.^4) sum(X.^5);
    sum(X.^3) sum(X.^4) sum(X.^5) sum(X.^6) 
];
b3 = [sum(Y .* X .^ 0); sum(Y .* X .^ 1); sum(Y .* X .^ 2); sum(Y .* X .^ 3)];

Z3 = A3 \ b3
polinomio_3 = Z3(1) + Z3(2) * X + Z3(3) * X.^2 + Z3(4) * X.^3
vector_errores_3 = polinomio_3 - Y
error_3 = sqrt(sum(vector_errores_3 .^ 2))
var_3 = sum(vector_errores_3 .^ 2) / (length(X) - 4)
condicion_3 = cond(A3)


plot2d(X, Y, -1)
plot2d(X, Y)
// Usar cholesky ?