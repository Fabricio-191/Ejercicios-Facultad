% Defina el predicado REVES:
% reves([3,2,1], [1,2,3]). ---> true (Hacer seguimiento)
% reves([3,2,1], X). ---> X=[1,2,3]

% reves(LISTA, RESULTADO) :- reverse(LISTA, RESULTADO).

reves([], []).
% reves([A], [A]) :- !.
reves([CABEZA | COLA], RESULTADO) :- reves(COLA, A), append(A, [CABEZA], RESULTADO).

