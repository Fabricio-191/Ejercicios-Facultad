humano(turing).
humano(socrates).
griego(socrates).
mortal(X) :- humano(X).

% Se pide:
% a) Definir un objetivo (consulta) que nos permita conocer todos los mortales que son griegos.
% b) Especificar todos los pasos que debe realizar el intérprete Prolog para obtener las soluciones del objetivo anterior

mortal(X), griego(X).