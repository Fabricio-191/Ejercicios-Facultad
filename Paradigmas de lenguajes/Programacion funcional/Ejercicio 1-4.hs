-- Ejercicio Nº1: Evalúe las siguientes funciones
(min (max 3 4) (max 7 3)) -- 4
(succ 9) + (max 5 4) + 1 -- 16
(max (succ (max 6 8)) (succ (min 6 8))) -- 9
(div 15 4) -- 3

-- Funciones sobre listas. Analizadores de listas: head - tail - last - elem
(head [3, 6, 9]) -- 3
(head ['a', 'b', 'c']) -- 'a'
(head "abcd") -- 'a'
(tail (head (tail ["ab", "cd"]))) -- 'd'
impares = [ "uno", "tres"] 
("cinco" : impares) -- ["cinco", "uno", "tres"]
(["siete"]++ impares) -- ["siete", "uno", "tres"]
impares -- ["uno", "tres"]
(last impares) -- "tres"
uno = [3, 1, 8, 5, 4, 2]
dos = [7, 9, 3, 5, 1]
nueva = [(head uno), (head dos)] -- [3, 7]
(splitAt 3 uno) -- ([3, 1, 8], [5, 4, 2])
(uno !! 2) -- 8
(dos !! 0) -- 7
lista = [(uno !! 2), (dos !! 3)] -- [8, 5]
(sum uno) -- 23
(product dos) -- 945
(null impares) -- False
(reverse impares) -- ["tres", "uno"]
(take 2 uno) -- [3, 1]
(drop 2 dos) -- [3, 5, 1]
(maximum dos) -- 9
(minimum impares) -- "tres"
(elem "cinco" impares) -- False
(elem "seis" impares) -- False

-- valuaciones con operadores lógicos
(not (elem "tres" impares)) -- False
(notElem "tres" impares) -- False
((elem "uno" impares) && (elem "siete" impares)) -- False
((elem "uno" impares) || (elem "siete" impares)) -- True
(length ["Jose", "Antonio", "Mario"]) -- 3
(length [ ["Jose", "Antonio", " Mario"] ]) -- 1

-- Ejercicio Nº2 Tuplas
(fst ("ana", "carlos")) -- "ana" -- Aplica solo duplas, no sobre triplas, cuadruplas, etc.
(snd ("ana", "carlos")) -- "carlos" -- Aplica solo duplas, no sobre triplas, cuadruplas, etc.
(zip [1, 2, 3, 4] ["uno", ['d', 'o', 's'], "tres", "cuatro"]) -- [(1, "uno"), (2, "dos"), (3, "tres"), (4, "cuatro")]
-- (zip [1..] ["uno", ['d', 'o', 's'], "tres", "cuatro"])

-- Ejercicio N°3 Rangos y listas infinitas. Evalúe las siguientes funciones
abecedario = ['a'..'z'] -- "abcdefghijklmnopqrstuvwxyz"
pares = [2, 4 .. 20] -- [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
impares = [21, 19 .. 1 ] -- [21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]
(take 10 [11, 22 .. ]) -- [11, 22, 33, 44, 55, 66, 77, 88, 99, 110]
(take 10 (cycle ['a', 'b', 'c'])) -- "abcabcabca"
(take 10 (repeat 10)) -- [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
(replicate 10 10) -- [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

-- Ejercicio N°4 Listas intencionales. Evaluar las siguientes expresiones:
[x * 2 | x <- [1..10]] -- [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
[x * 2 | x <- [1..10], x * 2 >= 12] -- [12, 14, 16, 18, 20]
frutas = ["naranjas", "peras", "uvas", "mandarinas", "peras"]
[x | x <- frutas, x == "peras"] -- ["peras", "peras"]
lista= [3, 5, 2, 0, 4, 0, 1, 5, 0] 
sum [ 1 | x <- lista, x == 0] -- 3
length [ x | x <- lista, x /= 0] -- 6