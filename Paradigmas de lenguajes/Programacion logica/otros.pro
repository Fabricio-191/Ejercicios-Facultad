factorial(0, 1).
factorial(A, B) :- A > 0, C is A - 1, factorial(C, R1), B is A * R1.




longitud([], X) :- X is 0.
longitud([_ | COLA], X) :- longitud(COLA, A), X is A + 1.




sum([], X) :- X is 0.
% sum([ELEM | COLA], X) :- sum(COLA, A), X is A + ELEM.

sum([ELEM | COLA], X) :- ELEM < 0, sum(COLA, A), X is A.
sum([ELEM | COLA], X) :- ELEM > 0, sum(COLA, A), X is A + ELEM.




cons(ELEM, LIST, Z) :- Z = [ELEM | LIST].
cons2(ELEM, LIST, Z) :- append([ELEM], LIST, Z).
cons3(ELEM, LIST, [ELEM | LIST]).


