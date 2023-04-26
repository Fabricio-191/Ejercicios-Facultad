% Defina el predicado ELIM que permita eliminar un elemento de una lista.
% elim(2, [3,2,1], [3,1]). ---> true
% elim(2, [2,3,1], X). ---> X=[3,1]

% elim(LISTA, ELEM, RESULTADO) :- delete(LISTA, ELEM, RESULTADO).

elim(_, [], []).
elim(ELEM, [ELEM | COLA], COLA).
elim(ELEM, [CABEZA | COLA], RESULT) :- elim(ELEM, COLA, A), RESULT = [CABEZA | A].




% Ejercicio propuesto (por mi), actualizar el predicado para que quite el elemento aunque este repetido.

includes(X, [X|_]) :- !.
includes(X, [_|COLA]) :- includes(X, COLA).

elim(X, [X|COLA], COLA) :- not(includes(X, COLA)), !.
elim(X, [X|COLA], RESULTADO) :- includes(X, COLA), elim(X, COLA, RESULTADO), !.
elim(X, [A|COLA], RESULTADO) :- elim(X, COLA, B), RESULTADO = [A | B].
