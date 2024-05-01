estadoInicial(jarras(24, 0, 0, 0)).
estadoFinal(jarras(8, 8, 8, 0)).
% capacidades(24, 13, 11, 5)

% Reglas
mover(jarras(J1, J2, J3, J4), jarras(NJ1, NJ2, J3, J4)) :- % de jarra 1 a jarra 2
	J1 > 0, J2 < 13,
	Cant is min(J1, 13 - J2),
	NJ1 is J1 - Cant,
	NJ2 is J2 + Cant.

mover(jarras(J1, J2, J3, J4), jarras(NJ1, J2, NJ3, J4)) :- % de jarra 1 a jarra 3
	J1 > 0, J3 < 11,
	Cant is min(J1, 11 - J3),
	NJ1 is J1 - Cant,
	NJ3 is J3 + Cant.

mover(jarras(J1, J2, J3, J4), jarras(NJ1, J2, J3, NJ4)) :- % de jarra 1 a jarra 4
	J1 > 0, J4 < 5,
	Cant is min(J1, 5 - J4),
	NJ1 is J1 - Cant,
	NJ4 is J4 + Cant.

mover(jarras(J1, J2, J3, J4), jarras(NJ1, NJ2, J3, J4)) :- % de jarra 2 a jarra 1
	J2 > 0, J1 < 24,
	Cant is min(J2, 24 - J1),
	NJ2 is J2 - Cant,
	NJ1 is J1 + Cant.

mover(jarras(J1, J2, J3, J4), jarras(J1, NJ2, NJ3, J4)) :- % de jarra 2 a jarra 3
	J2 > 0, J3 < 11,
	Cant is min(J2, 11 - J3),
	NJ2 is J2 - Cant,
	NJ3 is J3 + Cant.

mover(jarras(J1, J2, J3, J4), jarras(J1, NJ2, J3, NJ4)) :- % de jarra 2 a jarra 4
	J2 > 0, J4 < 5,
	Cant is min(J2, 5 - J4),
	NJ2 is J2 - Cant,
	NJ4 is J4 + Cant.

mover(jarras(J1, J2, J3, J4), jarras(NJ1, J2, NJ3, J4)) :- % de jarra 3 a jarra 1
	J3 > 0, J1 < 24,
	Cant is min(J3, 24 - J1),
	NJ3 is J3 - Cant,
	NJ1 is J1 + Cant.

mover(jarras(J1, J2, J3, J4), jarras(J1, NJ2, NJ3, J4)) :- % de jarra 3 a jarra 2
	J3 > 0, J2 < 13,
	Cant is min(J3, 13 - J2),
	NJ3 is J3 - Cant,
	NJ2 is J2 + Cant.

mover(jarras(J1, J2, J3, J4), jarras(J1, J2, NJ3, NJ4)) :- % de jarra 3 a jarra 4
	J3 > 0, J4 < 5,
	Cant is min(J3, 5 - J4),
	NJ3 is J3 - Cant,
	NJ4 is J4 + Cant.

mover(jarras(J1, J2, J3, J4), jarras(NJ1, J2, J3, NJ4)) :- % de jarra 4 a jarra 1
	J4 > 0, J1 < 24,
	Cant is min(J4, 24 - J1),
	NJ4 is J4 - Cant,
	NJ1 is J1 + Cant.

mover(jarras(J1, J2, J3, J4), jarras(J1, NJ2, J3, NJ4)) :- % de jarra 4 a jarra 2
	J4 > 0, J2 < 13,
	Cant is min(J4, 13 - J2),
	NJ4 is J4 - Cant,
	NJ2 is J2 + Cant.

mover(jarras(J1, J2, J3, J4), jarras(J1, J2, NJ3, NJ4)) :- % de jarra 4 a jarra 3
	J4 > 0, J3 < 11,
	Cant is min(J4, 11 - J3),
	NJ4 is J4 - Cant,
	NJ3 is J3 + Cant.

resolver(Estado, Visitados, Pasos) :- estadoFinal(Estado), reverse(Visitados, Pasos).
resolver(Estado, Visitados, Pasos) :- 
	mover(Estado, EstadoSiguiente),
	not(member(EstadoSiguiente, Visitados)),
	resolver(EstadoSiguiente, [EstadoSiguiente|Visitados], Pasos).

main(Pasos) :- estadoInicial(Inicio), resolver(Inicio, [Inicio], Pasos).


