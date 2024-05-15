-- Ejercicio Nº 14 Dada una lista ordenada y un átomo escribir una función que inserte el átomo en el lugar correspondiente
insertar :: (Integral a) => a -> [a] -> [a]
insertar x [] = [x]
insertar x x2:xs
  | (x2 > x) = [x, x2] ++ xs
  | otherwise = [x2] ++ (insertar x xs)


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

cant nom xs = length [x | x <- xs, (x !! 0) == nom]
plus xs = [head x | x <- xs, (x !! 1 == "Simple") && (cant (x !! 0) xs) == 1]


-- Parcial (2022) definir funcion enlace que reciba como argumento dos listas de pares de elementos y construya una nueva lista de la siguiente manera:

-- enlace [[1, 2], [5, 6], [20, 8]] [[6, 100], [1, 200], [3, 300], [2, 400], [8, 500]]   ->  [[1, 400], [5, 100], ...]

buscar :: (Eq a) => a -> [[a]] -> a
buscar x [] = []
buscar x (y:ys)
  | (x == (y !! 0)) = y !! 1
  | otherwise = buscar x ys

enlace :: (Eq a) => [[a]] -> [[a]] -> [[a]]
enlace [] lote = []
enlace (x:xs) lote = [x !! 0, buscar (x !! 1) lote] ++ enlace xs lote

enlace2 lista1 lote = [[x !! 0, (head [(y !! 1) | y <- lote, (y !! 0) == (x !! 1)])] | x <- lista1]

enlace3 [] lote = []
enlace3 (x:xs) lote = [x !! 0, (head [(y !! 1) | y <- lote, (y !! 0) == (x !! 1)])] : enlace3 xs lote






-- consultaListaOrdenada [7, 1, 3, 9, 5] [4, 5, 8]

insertar :: (Integral a) => a -> [a] -> [a]
insertar x [] = [x]
insertar x x2:xs
  | (x2 > x) = [x, x2] ++ xs
  | otherwise = [x2] ++ (insertar x xs)

consultaListaOrdenada :: (Ord a) => [a] -> [a] -> [a]
consultaListaOrdenada [] [] = []
consultaListaOrdenada [] a = a
consultaListaOrdenada (x:xs) lista2 = consultaListaOrdenada xs (insertar x lista2)