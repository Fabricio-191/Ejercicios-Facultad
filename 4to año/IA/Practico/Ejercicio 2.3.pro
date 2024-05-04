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

camino(A, A, _, []).
camino(A, B, Visited, [C|D]) :- ruta(A, C), not(member(C, Visited)), camino(C, B, [C|Visited], D).
camino(A, B, [A|X]) :- camino(A, B, [A], X).


camino(a, r, X). % consulta

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
