% ejercicios propuestos por mi


append2([A], LISTA, [A|LISTA]) :- !.
append2([A|COLA], LISTA, [A|X]) :- append2(COLA, LISTA, X).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

esDivisible(X, A) :- 0 is X mod A.

esPrimo2(_, 1) :- !.
esPrimo2(X, A) :- A > 1, not(esDivisible(X, A)), B is A - 1, esPrimo2(X, B). 

esPrimo(X) :- A is X - 1, esPrimo2(X, A).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

filtrarPositivos([], []) :- !.
filtrarPositivos([A|COLA], RESULTADO) :- A < 0, filtrarPositivos(COLA, RESULTADO), !.
filtrarPositivos([A|COLA], [A|R]) :- A >= 0, filtrarPositivos(COLA, R).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% quitar elemento de una lista, considerand que puede estar repetido
elim(X, [X | COLA], COLA) :- not(member(X, COLA)), !.
elim(X, [X | COLA], RESULTADO) :- member(X, COLA), elim(X, COLA, RESULTADO), !.
elim(X, [A | COLA], [A | B]) :- elim(X, COLA, B).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

divisionEntera(A, B, 0) :- A < B, !.
divisionEntera(A, B, R) :- A >= B, C is A - B, divisionEntera(C, B, D), R is D + 1.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Ejercicio recuperatorio 2023
categoria(infantil, 5, 12).
categoria(juvenil, 13, 20).
categoria(mayor, 21, 45).

cat(E, Cat) :- categoria(Cat, A, B), B >= E, E >= A.

contar([], 0, 0, 0).
contar([ [_, E] | COLA], A, B, C) :- cat(E, infantil), contar(COLA, A1, B, C), A is A1 + 1.
contar([ [_, E] | COLA], A, B, C) :- cat(E, juvenil),  contar(COLA, A, B1, C), B is B1 + 1.
contar([ [_, E] | COLA], A, B, C) :- cat(E, mayor),    contar(COLA, A, B, C1), C is C1 + 1.

genera(LISTA, [[infantil, A], [juvenil, B], [mayor, C]]) :- contar(LISTA, A, B, C), !

genera([[juana, 13], [ana, 10], [gema, 6]], R).