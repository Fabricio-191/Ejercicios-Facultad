% Defina el predicado ADYAC que verifica si dos elementos son adyacentes en una lista.
% adyac(3, 2, [3,2,1]). ---> true
% adyac(2, 3, [3,2,1]). ---> true
% adyac(X, 2, [3,2,1]). ---> X=3, X=1

% adyac(A, B, LIST) :- nextto(A, B, LIST).
% adyac(A, B, LIST) :- nextto(B, A, LIST).

adyac(A, B, [A, B | _]).
adyac(A, B, [B, A | _]).
adyac(A, B, [_ | COLA]) :- adyac(A, B, COLA).
