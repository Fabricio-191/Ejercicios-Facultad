-- Ejercicio Nº1: Evalúe las siguientes funciones
(min (max 3 4) (max 7 3))
(succ 9) + (max 5 4) + 1
(max (succ (max 6 8)) (succ (min 6 8)))
(div 15 4)

-- Funciones sobre listas. Analizadores de listas: head - tail - last - elem
(head [3, 6, 9])
(head ['a', 'b', 'c'])
(head "abcd")
(tail (head (tail ["ab", "cd"])))
impares = [ "uno", "tres"]
("cinco" : impares)
(["siete"]++ impares)
impares
(last impares)
uno = [3, 1, 8, 5, 4, 2]
dos = [7, 9, 3, 5, 1]
nueva = [(head uno), (head dos)]
(splitAt 3 uno)
(uno !! 2)
(dos !! 0)
lista = [(uno !! 2), (dos !! 3)]
(sum uno)
(product dos)
(null impares)
(reverse impares)
(take 2 uno)
(drop 2 dos)
(maximum dos)
(minimum impares)
(elem "cinco" impares)
(elem "seis" impares)

-- valuaciones con operadores lógicos
(not (elem "tres" impares))
(notElem "tres" impares)
((elem "uno" impares) && (elem "siete" impares))
((elem "uno" impares) || (elem "siete" impares))
(length ["Jose", "Antonio", "Mario"])
(length [ ["Jose", "Antonio", " Mario"] ])

-- Ejercicio Nº2 Tuplas
(fst ("ana", "carlos")) --Aplica solo duplas, no sobre triplas, cuadruplas, etc.
(snd ("ana", "carlos")) --Aplica solo duplas, no sobre triplas, cuadruplas, etc.
(zip [1, 2, 3, 4] ["uno", ['d', 'o', 's'], "tres", "cuatro"]) --(zip [1..] ["uno", ['d', 'o', 's'], "tres", "cuatro"])

-- Ejercicio N°3 Rangos y listas infinitas. Evalúe las siguientes funciones
abecedario = ['a'..'z']
pares = [2, 4 .. 20]
impares = [21, 19 .. 1 ]
(take 10 [11, 22 .. ])
(take 10 (cycle ['a', 'b', 'c']))
(take 10 (repeat 10))
(replicate 10 10)

-- Ejercicio N°4 Listas intencionales. Evaluar las siguientes expresiones:
[x*2 | x <- [1..10]]
[x*2 | x <- [1..10], x*2 >= 12]
frutas = ["naranjas", "peras", "uvas", "mandarinas", "peras"]
[x | x <- frutas, x=="peras"]
lista= [3, 5, 2, 0, 4, 0, 1, 5, 0]
sum [ 1 | x <- lista, x==0]
length [ x | x <- lista, x /= 0]