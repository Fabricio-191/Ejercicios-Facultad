factorial(0, 1).
factorial(A, B) :- A > 0, C is A - 1, factorial(C, R1), B is A * R1.






% Definir un predicado que calcule la longitud de una lista.
longitud([], X) :- X is 0.
longitud([_ | COLA], X) :- longitud(COLA, A), X is A + 1.






% Escribir la suma de los elementos positivos de una lista.
sum([], X) :- X is 0.
% sum([ELEM | COLA], X) :- sum(COLA, A), X is A + ELEM.

sum([ELEM | COLA], A) :- ELEM < 0, sum(COLA, A).
sum([ELEM | COLA], X) :- ELEM >= 0, sum(COLA, A), X is A + ELEM.






% Definir un predicado que ante la consulta:
% cons(1, [2,3], Z)  ->  Z=[1,2,3]

cons(ELEM, LIST, Z) :- Z = [ELEM | LIST].
cons2(ELEM, LIST, Z) :- append([ELEM], LIST, Z).
cons3(ELEM, LIST, [ELEM | LIST]).
