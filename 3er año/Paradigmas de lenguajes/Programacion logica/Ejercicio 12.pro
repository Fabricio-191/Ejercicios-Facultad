% Dadas las cláusulas medico y paciente y una relación entre ellas representada por la cláusula atiende, mediante los siguientes hechos:
medico(m1,rosales).
medico(m2,manni).
paciente(p1,juan).
paciente(p2,ana).
atiende(m1,p1).
atiende(m1,p2).
atiende(m2,p2).

atiende2(M, P) :- medico(A, M), atiende(A, B), paciente(B, P).

opcion(1) :- write("Nombre del medico: "), read(X), atiende2(X, P), writeln(P), fail.
opcion(2) :- write("Nombre del paciente: "), read(P), atiende2(X, P), writeln(X), fail.
opcion(3) :- writeln("ADIOS"), !.
opcion(_) :- base.

base :-
    writeln('1. encontrar pacientes de un medico'),
    writeln('2. encontrar medicos de un paciente'),
    writeln('3. Terminar'),
    read(X), opcion(X).