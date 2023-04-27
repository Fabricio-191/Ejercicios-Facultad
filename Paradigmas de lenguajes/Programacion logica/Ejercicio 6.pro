% Defina el predicado MODULO:
% modulo(10,5,R). ---> R=0
% modulo(14,3,R). ---> R=2

% modulo(A, B, C) :- C is A mod B.

modulo(A, B, A) :- A < B, !.
modulo(A, B, R) :- A >= B, C is A - B, modulo(C, B, R).

