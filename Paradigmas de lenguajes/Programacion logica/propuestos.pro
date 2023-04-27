append2([A], LISTA, [A|LISTA]) :- !.
append2([A|COLA], LISTA, [A|X]) :- append2(COLA, LISTA, X).






esDivisible(X, A) :- 0 is X mod A.

esPrimo2(_, 1) :- !.
esPrimo2(X, A) :- A > 1, not(esDivisible(X, A)), B is A - 1, esPrimo2(X, B). 

esPrimo(X) :- A is X - 1, esPrimo2(X, A).






filtrarPositivos([], []) :- !.
filtrarPositivos([A|COLA], RESULTADO) :- A < 0, filtrarPositivos(COLA, RESULTADO), !.
filtrarPositivos([A|COLA], [A|R]) :- A >= 0, filtrarPositivos(COLA, R).






% Ejercicio propuesto (por mi), actualizar el predicado para que quite el elemento aunque este repetido.
elim(X, [X | COLA], COLA) :- not(member(X, COLA)), !.
elim(X, [X | COLA], RESULTADO) :- member(X, COLA), elim(X, COLA, RESULTADO), !.
elim(X, [A | COLA], [A | B]) :- elim(X, COLA, B).