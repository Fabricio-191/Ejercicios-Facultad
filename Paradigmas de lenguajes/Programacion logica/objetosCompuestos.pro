% conteo elemetos en arbol binario
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
recorrer(tree(X,Y,Z)) :- write(X), nl, recorrer(Y), recorrer(Z).
mostrar :- miarbol(X), recorrer(X).

contar(nil, A) :- A is 0.
contar(tree(_,Y,Z), A) :- contar(Y, B), contar(Z, C), A is B + C + 1.
contar :- miarbol(X), contar(X, A), write(A).





% EJERCICIO PROPUESTO
animales(mamifero([vaca,mono])).
animales(reptil([serpiente,coco])).
animales(pez([salmon])).

% Construya una función que permita mostrar la clase a que corresponda un animal en caso de ser posible

in(X, [X|_]).
in(X, [_|COLA]) :- in(X, COLA).

es(A, B) :- animales(X), functor(X, B, _), arg(1, X, ANIMALES), in(A, ANIMALES), !.

es(serpiente, X).
es(mono, X).
es(tigre, X).