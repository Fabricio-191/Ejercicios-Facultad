% ruta(X, Y).: Define las conexiones directas entre puntos X e Y.
ruta(a, b).
ruta(a, c).
ruta(b, f).
ruta(b, d).
ruta(c, d).
ruta(d, e).
ruta(e, r).
ruta(f, g).
ruta(f, k).
ruta(g, h).
ruta(g, i).
ruta(h, i).
ruta(h, k).
ruta(i, j).
ruta(i, l).
ruta(j, m).
ruta(m, n).
ruta(l, n).
ruta(n, o).
ruta(n, p).
ruta(p, r).
ruta(k, o).
ruta(k, q).
ruta(o, r).
ruta(q, r).
ruta(b, a).
ruta(c, a).
ruta(f, b).
ruta(d, b).
ruta(d, c).
ruta(e, d).
ruta(r, e).
ruta(g, f).
ruta(k, f).
ruta(h, g).
ruta(i, g).
ruta(i, h).
ruta(k, h).
ruta(j, i).
ruta(l, i).
ruta(m, j).
ruta(n, m).
ruta(n, l).
ruta(o, n).
ruta(p, n).
ruta(r, p).
ruta(o, k).
ruta(q, k).
ruta(r, o).
ruta(r, q).

camino(A, A, _, []). % Define el caso base de la recursión. Cuando el punto de partida y el punto de llegada son el mismo, el camino es una lista vacía.
camino(A, B, Visited, [C|D]) :- ruta(A, C), not(member(C, Visited)), camino(C, B, [C|Visited], D). % Esta regla define el caso recursivo para encontrar un camino. Busca todos los puntos C conectados a A (que podrían ser B o acercarnos a él), y llama a camino(C, B, [C|Visited], D) para encontrar un camino desde C a B. La lista Visited se utiliza para evitar ciclos en el grafo.
camino(A, B, [A|X]) :- camino(A, B, [A], X). % Esta regla proporciona una interfaz simple para la consulta. Es decir, permite llamar a camino(A, B, Visited, [C|D]) (la regla anterior) sin especificar la lista de nodos visitados inicialmente.


camino(a, r, X). % consulta: busca un camino desde el punto a al punto r, y devuelve el camino en la variable X.

% X = [a, b, f, g, h, i, j, m, n, o, r]
% X = [a, b, f, g, h, i, j, m, n, o, k, q, r]
% X = [a, b, f, g, h, i, j, m, n, p, r]
% X = [a, b, f, g, h, i, l, n, o, r]
% X = [a, b, f, g, h, i, l, n, o, k, q, r]
% X = [a, b, f, g, h, i, l, n, p, r]
% X = [a, b, f, g, h, k, o, r]
% X = [a, b, f, g, h, k, o, n, p, r]
% X = [a, b, f, g, h, k, q, r]
% X = [a, b, f, g, i, j, m, n, o, r]
% X = [a, b, f, g, i, j, m, n, o, k, q, r]
% X = [a, b, f, g, i, j, m, n, p, r]
% X = [a, b, f, g, i, l, n, o, r]
% X = [a, b, f, g, i, l, n, o, k, q, r]
% X = [a, b, f, g, i, l, n, p, r]
% X = [a, b, f, g, i, h, k, o, r]
% X = [a, b, f, g, i, h, k, o, n, p, r]
% X = [a, b, f, g, i, h, k, q, r]
% X = [a, b, f, k, o, r]
% X = [a, b, f, k, o, n, p, r]
% X = [a, b, f, k, q, r]
% X = [a, b, f, k, h, i, j, m, n, o, r]
% X = [a, b, f, k, h, i, j, m, n, p, r]
% X = [a, b, f, k, h, i, l, n, o, r]
% X = [a, b, f, k, h, i, l, n, p, r]
% X = [a, b, f, k, h, g, i, j, m, n, o, r]
% X = [a, b, f, k, h, g, i, j, m, n, p, r]
% X = [a, b, f, k, h, g, i, l, n, o, r]
% X = [a, b, f, k, h, g, i, l, n, p, r]
% X = [a, b, d, e, r]
% X = [a, c, d, e, r]
% X = [a, c, d, b, f, g, h, i, j, m, n, o, r]
% X = [a, c, d, b, f, g, h, i, j, m, n, o, k, q, r]
% X = [a, c, d, b, f, g, h, i, j, m, n, p, r]
% X = [a, c, d, b, f, g, h, i, l, n, o, r]
% X = [a, c, d, b, f, g, h, i, l, n, o, k, q, r]
% X = [a, c, d, b, f, g, h, i, l, n, p, r]
% X = [a, c, d, b, f, g, h, k, o, r]
% X = [a, c, d, b, f, g, h, k, o, n, p, r]
% X = [a, c, d, b, f, g, h, k, q, r]
% X = [a, c, d, b, f, g, i, j, m, n, o, r]
% X = [a, c, d, b, f, g, i, j, m, n, o, k, q, r]
% X = [a, c, d, b, f, g, i, j, m, n, p, r]
% X = [a, c, d, b, f, g, i, l, n, o, r]
% X = [a, c, d, b, f, g, i, l, n, o, k, q, r]
% X = [a, c, d, b, f, g, i, l, n, p, r]
% X = [a, c, d, b, f, g, i, h, k, o, r]
% X = [a, c, d, b, f, g, i, h, k, o, n, p, r]
% X = [a, c, d, b, f, g, i, h, k, q, r]
% X = [a, c, d, b, f, k, o, r]
% X = [a, c, d, b, f, k, o, n, p, r]
% X = [a, c, d, b, f, k, q, r]
% X = [a, c, d, b, f, k, h, i, j, m, n, o, r]
% X = [a, c, d, b, f, k, h, i, j, m, n, p, r]
% X = [a, c, d, b, f, k, h, i, l, n, o, r]
% X = [a, c, d, b, f, k, h, i, l, n, p, r]
% X = [a, c, d, b, f, k, h, g, i, j, m, n, o, r]
% X = [a, c, d, b, f, k, h, g, i, j, m, n, p, r]
% X = [a, c, d, b, f, k, h, g, i, l, n, o, r]
% X = [a, c, d, b, f, k, h, g, i, l, n, p, r]

% en caso de querer ejecutarlo uno mismo https://swish.swi-prolog.org/