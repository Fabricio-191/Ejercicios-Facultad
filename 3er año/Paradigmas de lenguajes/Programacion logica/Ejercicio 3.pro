% Suponga definidas las siguientes claúsulas:
padre(X,Y). % X es padre de Y.
madre(X,Y). % X es madre de Y.
hombre(X). % X es hombre.
mujer(X). % X es mujer.
progenitor(X,Y). % X es padre o madre de Y.

% Se pide definir en base a ellas las siguientes relaciones:
% es_madre (X). X es madre.
% es_padre (X). X es padre.
% es_hijo (X). X es hijo.
% hija (X,Y). X es hija de Y.
% tio (X,Y). X es tío de Y.
% sobrino (X,Y). X es sobrino de Y.
% prima (X,Y). X es prima de Y.
% abuelo_o_abuela (X,Y). X es abuelo o abuela de Y

es_madre(X) :- madre(X, _).
% es_madre(X) :- mujer(X), progenitor(X, _).

es_padre(X) :- padre(X, _).
% es_padre(X) :- hombre(X), progenitor(X, _).

es_hijo(X) :- hombre(X), progenitor(_, X).
hija(X, Y) :- mujer(X), progenitor(Y, X).

hermano(X, Y) :- progenitor(Padre, X), progenitor(Padre, Y), X \= Y.

tio(Tio, Sobrino) :- hombre(Tio), hermano(Tio, Padre), progenitor(Padre, Sobrino).
sobrino(X,Y) :- tio(Y, X).
prima(X,Y) :- mujer(X), progenitor(Padre, X), tio(Padre, Y).

abuelo_o_abuela(X, Y) :- progenitor(X, Z), progenitor(Z, Y).
