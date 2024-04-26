miarbol(
	tree(carla,
		tree(miguel,
			tree(carlos, nil, nil),
			tree(maria, nil, nil)
		),
		tree(miriam,
			tree(patri, nil, nil),
			tree(jorge, nil, nil)
		)
	)
).

recorrer(nil).
recorrer(tree(X, Y, Z)) :- write(X), nl, recorrer(Y), recorrer(Z).
mostrar :- miarbol(X), recorrer(X).

% verificar si un árbol es binario
% istree( tree(a, tree(b,nil,nil), nil)).  ->  true
% istree( tree(a, tree(b,nil,nil))).  ->  fail
istree(tree(_, nil, nil)).
istree(tree(_, A,   nil)) :- istree(A).
istree(tree(_, nil, B  )) :- istree(B).
istree(tree(_, A,   B  )) :- istree(A), istree(B).


% Mostrar solo los nodo hojas
mostrarHojas(tree(V, nil, nil)) :- writeln(V).
mostrarHojas(tree(_, A,   nil)) :- mostrarHojas(A).
mostrarHojas(tree(_, nil, B  )) :- mostrarHojas(B).
mostrarHojas(tree(_, A,   B  )) :- mostrarHojas(A), mostrarHojas(B).


% mostrar los nodos que no son hojas
mostrarNoHojas(tree(_, nil, nil)).
mostrarNoHojas(tree(V, A,   nil)) :- writeln(V), mostrarNoHojas(A).
mostrarNoHojas(tree(V, nil, B  )) :- writeln(V), mostrarNoHojas(B).
mostrarNoHojas(tree(V, A,   B  )) :- writeln(V), mostrarNoHojas(A), mostrarNoHojas(B).

% calcular la cantidad de nodos
contar(nil, A) :- A is 0.
contar(tree(_, Y, Z), A) :- contar(Y, B), contar(Z, C), A is B + C + 1.
contar :- miarbol(X), contar(X, A), write(A).






% EJERCICIO PROPUESTO
animales(mamifero([vaca,mono])).
animales(reptil([serpiente,coco])).
animales(pez([salmon])).

% Construya una función que permita mostrar la clase a que corresponda un animal en caso de ser posible
% tipo(X, N) :- animales(F), functor(F, N, _), arg(1, F, LISTA), member(X, LISTA), !.
tipo(X, N) :- animales(F), F=..[N, LISTA], member(X, LISTA), !.

es(X) :- tipo(X, N), writeln(N), !.
es(X) :- not(tipo(X, _)), writeln("ERROR").
