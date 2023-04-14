% Defina el predicado ELIM que permita eliminar un elemento de una lista.
% elim(2, [3,2,1], [3,1]). ---> true
% elim(2, [2,3,1], X). ---> X=[3,1]

% elim(LISTA, ELEM, RESULTADO) :- delete(LISTA, ELEM, RESULTADO).

elim(_, [], []).
elim(ELEM, [ELEM | COLA], COLA).
elim(ELEM, [CABEZA | COLA], RESULT) :- elim(ELEM, COLA, A), RESULT = [CABEZA | A].

