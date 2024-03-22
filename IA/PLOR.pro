estadoInicial(estado(s, s, s, s)).
estadoFinal(estado(n, n, n, n)).

opuesto(s, n).
opuesto(n, s).

mover(estado(X, L, O, R), estado(Y, L, O, R)) :- opuesto(X, Y). % Mover al pastor solo
mover(estado(X, X, O, R), estado(Y, Y, O, R)) :- opuesto(X, Y). % Mover al pastor y al lobo
mover(estado(X, L, X, R), estado(Y, L, Y, R)) :- opuesto(X, Y). % Mover al pastor y a la oveja
mover(estado(X, L, O, X), estado(Y, L, O, Y)) :- opuesto(X, Y). % Mover al pastor y al repollo

inseguro(estado(P, X, X, _)) :- opuesto(P, X).
inseguro(estado(P, _, X, X)) :- opuesto(P, X).


% solucion(Estado, Visitados, Pasos)
solucion(Estado, _, []) :- estadoFinal(Estado).
solucion(Estado, Visitados, [NuevoEstado|Pasos]) :- 
    mover(Estado, NuevoEstado),
    not(inseguro(NuevoEstado)),
    not(member(NuevoEstado, Visitados)),
    solucion(NuevoEstado, [NuevoEstado|Visitados], Pasos).


main :- 
    estadoInicial(EstadoInicial),
    solucion(EstadoInicial, [EstadoInicial], Pasos),
    writeln([EstadoInicial|Pasos]).

