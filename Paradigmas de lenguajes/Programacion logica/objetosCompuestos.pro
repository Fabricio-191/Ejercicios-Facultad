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
istree(tree(_, nil, nil)) :- !.
istree(tree(_, A,   nil)) :- istree(A), !.
istree(tree(_, nil, B  )) :- istree(B), !.
istree(tree(_, A,   B  )) :- istree(A), istree(B).


% Mostrar solo los nodo hojas

% mostrar los nodos que no son hojas

% calcular la cantida de nodos
contar(nil, A) :- A is 0.
contar(tree(_, Y, Z), A) :- contar(Y, B), contar(Z, C), A is B + C + 1.
contar :- miarbol(X), contar(X, A), write(A).




% EJERCICIO PROPUESTO
animales(mamifero([vaca,mono])).
animales(reptil([serpiente,coco])).
animales(pez([salmon])).

% Construya una función que permita mostrar la clase a que corresponda un animal en caso de ser posible

animales(mamifero([vaca,mono])).
animales(reptil([serpiente,coco])).
animales(pez([salmon])).

includes(X, [X|_]) :- !.
includes(X, [_|COLA]) :- includes(X, COLA).

tipo(X, N) :- animales(F), functor(F, N, _), arg(1, F, LISTA), includes(X, LISTA), !.


es(X) :- tipo(X, N), writeln(N), !.
es(X) :- not(tipo(X, _)), writeln("ERROR").