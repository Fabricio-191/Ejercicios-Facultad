ruta(1, a, b).
ruta(2, a, c).
ruta(8, b, c).
ruta(3, b, d).
ruta(4, c, d).

% camino(a, c, X).
% X = [1, 8]
% X = [2]

% camino(d, a, X). -> false

% camino(a, d, X).
% X = [1, 8, 4]
% X = [1, 3]
% X = [2, 4]

camino(A, A, []).
camino(A, B, X) :- ruta(N, A, C), camino(C, B, D), X = [N|D].