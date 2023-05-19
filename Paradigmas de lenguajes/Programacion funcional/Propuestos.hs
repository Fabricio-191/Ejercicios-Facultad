-- Ejercicio Nº 14 Dada una lista ordenada y un átomo escribir una función que inserte el átomo en el lugar correspondiente
insertar :: (Integral a) => a -> [a] -> [a]
insertar x [] = [x]
insertar x lista
  | ((head lista) > x) = [x, head lista] ++ (tail lista)
  | otherwise = [head lista] ++ (insertar x (tail lista))


-- Ejercicio Nº 15 Defina una función que, aplicada a una lista de listas, permita obtener una lista de un solo nivel.
concatenar :: [[a]] -> [a]
concatenar [] = []
concatenar (x:xs) = x ++ concatenar xs


-- Ejercicio Nº 16 Construir un programa no recursivo que realice la suma de números complejos, los cuales se ingresan en sublistas con pares de números donde el primer elemento es la componente real y el segundo la componente imaginaria.
-- [[2, 3], [0, 1], [6, 0]]     2 + 3i + i + 6 = 8 + 4i
sumarI :: (Integral a) => [[a]] -> [a]
sumarI list = [sum ([head x | x <- list]), sum ([last x | x <- list])]


-- Ejercicio Nº18: Escriba un programa que recibiendo como argumento una lista de listas donde cada sublista contiene nombre del docente, dedicación y carrera donde trabaja; entregue como resultado una lista con los nombres de los docentes que cobrarán un plus considerando que los cobrarán aquellos docentes que tenga solamente un cargo con dedicación simple.
-- [["Ana", "Exclusivo", "LSI"], ["Mary", "Semi", "LCC"], ["Jose", "Simple", "LSI"], ["Mary", "Simple", "LSI"], ["Raul", "Exclusivo", "LCC"], ["Pepe", "Simple", "LSI"]]
plus :: [[[Char]]] -> [[Char]]
plus lista = [head x | x <- lista, (x !! 1) == "Simple"]
