(deftemplate libro (slot editorial)(slot idioma)(multislot titulo)
(slot paginas)(slot autor))

(deffacts libros
(libro (editorial Omega) (idioma castellano) (titulo Inteligencia Artificial) (paginas 350) (autor Smith))
(libro (editorial Alfa) (idioma ingles) (titulo Compilers) (paginas 300) (autor Ullman))
(libro (editorial Beta) (idioma castellano) (titulo Sistemas Expertos) (paginas 250) (autor Martinez))
(libro (editorial Omega) (idioma ingles) (titulo Lenguaje Python) (paginas 290) (autor Cane))
(libro (editorial Beta) (idioma ingles) (titulo Learning Clips) (paginas 200) (autor Calvo))
(libro (editorial Omega) (idioma ingles) (titulo Learning Java) (paginas 320) (autor Smith))
)