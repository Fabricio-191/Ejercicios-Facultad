progenitor(joaquin, marcos).
progenitor(joaquin, facundo).
progenitor(florencia, matias).
progenitor(martia, andrea).
hermano(X,Y) :- progenitor(Z,X), progenitor(Z,Y).

% Se pide:
% a) Explique porque es posible que una persona sea hermano de si misma.
% b) Modifique la definición para que esto no suceda.
% c) Dado el Objetivo: hermano(marcos, X)?, Indicar la salida.