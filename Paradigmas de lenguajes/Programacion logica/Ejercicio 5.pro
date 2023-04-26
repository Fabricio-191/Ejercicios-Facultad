% Defina el predicado POTENCIA:
% potencia (3,0,X). ---> X=1
% potencia (5,2,25). ---> true

% potencia(A, B, C) :- C is A ** B.

potencia(_, 0, 1) :- !.
potencia(A, B, C) :- B > 0, D is B - 1, potencia(A, D, E), C is A * E.

