% Defina el predicado MIEMBRO:
% miembro (1, [3,2,1]). ---> true
% miembro (X, [3,2,1]). ---> X=3, X=2, X=1

% miembro(X, LISTA) :- member(X, LISTA).

miembro(X, [X | _]).
miembro(X, [_ | COLA]) :- miembro(X, COLA).

