% Dadas las cláusulas medico y paciente y una relación entre ellas representada por la cláusula atiende, mediante los siguientes hechos:
medico(m1,rosales).
medico(m2,manni).
paciente(p1,juan).
paciente(p2,ana).
atiende(m1,p1).
atiende(m1,p2).
atiende(m2,p2).

% Construya un programa de manera tal que cuando se invoque como base, aparezca en pantalla lo siguiente:
% 	* Dado un médico, listar los pacientes que atiende.
% 	* Dado un paciente, listar los médicos que lo atienden.
% 	* Terminar.
% Se espera que:
% a) Si se responde 1, el programa deberá preguntar por el nombre del médico y mostrar todos los pacientes que atiende, y luego vuelva a mostrar el menu.
% b) Si se responde 2, el programa deberá preguntar por el nombre del paciente y mostrar todos los médicos que lo atienden, y luego vuelva al menú.
% c) Si se responde 3, el programa deberá finalizar dando mensaje que diga "ADIOS".

atiende2(NomM, NomP) :- medico(CodM, NomM), atiende(CodM, CodP), paciente(CodP, NomP).

option(1) :- write("Nombre doctor: "),   read(NomM), atiende2(NomM, NomP), writeln(NomP), fail.
option(2) :- write("Nombre paciente: "), read(NomP), atiende2(NomM, NomP), writeln(NomM), fail.
option(3) :- write_ln("Adios."), !, fail.
option(_).

base :- read(X), option(X), base.