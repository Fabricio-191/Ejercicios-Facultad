-- Ejercicio N°5: Definir una función que cuente los elementos pares tiene una lista de números.
countEven :: (Integral a) => [a] -> Int
countEven list = sum [1 | x <- list, even x]


-- Ejercicio Nº 6: Definir una función que reciba una lista de listas y entregue la cantidad de elementos de la lista de mayor longitud.
biggerList :: [[a]] -> Int
biggerList list = maximum [length x | x <- list]


-- Ejercicio Nº 7: Definir una función que transforme una lista de números en otra lista que contenga el cubo de cada elemento.
cubeList :: (Integral a) => [a] -> [a]
cubeList list = [x^3 | x <- list]


-- Ejercicio Nº 8: Definir una función recursiva que permita eliminar los elementos repetidos de una lista de átomos.
removeRepeated :: (Eq a) => [a] -> [a]
removeRepeated [] = []
-- removeRepeated list = if (elem (head list) (tail list)) then (removeRepeated (tail list)) else (head list : (removeRepeated (tail list)))
removeRepeated (x:xs) 
 | (elem x xs) = (removeRepeated xs)
 | otherwise = (x : (removeRepeated xs))


-- Ejercicio Nº 9: Implementar una función recursiva que pase un número decimal a binario
toBinary :: (Integral a) => a -> [Char]
toBinary 0 = "0"
toBinary 1 = "1"
toBinary num
 | ((rem num 2) == 0) = (toBinary (div num 2) ++ "0")
 | otherwise = (toBinary (div num 2) ++ "1")
 

-- Ejercicio Nº 10: Implementar una función recursiva que permita obtener la unión de dos listas dadas; los elementos repetidos solo deben aparecer una vez.
union :: (Eq a) => [a] -> [a] -> [a]
union [] [] = []
union list [] = list
union [] list = list
union (x:xs) list2
 | (elem x list2) = union xs list2
 | otherwise = union xs (x : list2)
 
 
-- Ejercicio Nº 11: Definir una función que permita contar los átomos de una lista de listas. (de manera recursiva)
countAtoms :: [[a]] -> Int
countAtoms [] = 0
countAtoms (x:xs) = (length x) + (countAtoms xs)


-- Ejercicio Nº 12: Calcular el producto de una matriz por un vector.

calc :: [[Int]] -> [Int] -> [[Int]]
calc a b = map (\x -> zipWith (*) x b) a

-- calc2 :: [[Int]] -> [Int] -> Int
-- calc2 a b = sum [sum x | x <- calc a b]