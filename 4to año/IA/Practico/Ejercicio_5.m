# pkg install "https://downloads.sourceforge.net/project/octave/Octave%20Forge%20Packages/Individual%20Package%20Releases/strings-1.3.1.tar.gz"
# pkg install "https://github.com/lmarkowsky/fuzzy-logic-toolkit/archive/refs/tags/0.5.1.tar.gz"
pkg load strings
pkg load fuzzy-logic-toolkit

fis = newfis('Ejercicio5'); # Crear sistema de inferencia difusa

# inputs
fis = addvar(fis, 'input' , 'Lluvia',        [ 0  100 ]); # Se crea la variable de entrada Lluvia con rango [0, 100]
# Se crean las funciones de membresía para la variable Lluvia
# El "trapmf" es un tipo de función de membresía trapezoidal, que se define por 4 puntos, donde en el primer y último punto la función de membresía vale 0 y en los puntos intermedios vale 1
fis = addmf (fis, 'input' , 1, 'BAJA'      , 'trapmf',  [ -1   0  25  40 ]);
fis = addmf (fis, 'input' , 1, 'IMPORTANTE', 'trapmf',  [ 20  50  50  70 ]);
fis = addmf (fis, 'input' , 1, 'INTENSA'   , 'trapmf',  [ 60  70 100 120 ]);
 
fis = addvar(fis, 'input' , 'Suelo',         [ 0  100 ]); # Se crea la variable de entrada Suelo con rango [0, 100]
fis = addmf (fis, 'input' , 2, 'HUMEDO'    , 'trapmf',  [ 15  35  35  80 ]);
fis = addmf (fis, 'input' , 2, 'EMPAPADO'  , 'trapmf',  [ 45  70 100 120 ]);
 
fis = addvar(fis, 'input' , 'Topografia',    [ 0  100 ]); # Se crea la variable de entrada Topografia con rango [0, 100]
fis = addmf (fis, 'input' , 3, 'SUAVE'     , 'trapmf',  [  2   4  15  25 ]);
fis = addmf (fis, 'input' , 3, 'ESCARPADA' , 'trapmf',  [ 10  20  30  50 ]);

# outputs
fis = addvar(fis, 'output', 'Problema', [ 0  20 ]);  # Se crea la variable de salida Problema con rango [0, 20]
# El valor 0 20 es arbitrario, se puede cambiar por cualquier otro valor como 0 10, pero para que las graficas no se superpongan se eligió 0 20
# Aca cada membresía es una función gaussiana (distribucion de probabilidades normal), que se define por 2 parámetros, el segundo es el centro de la función y el primero es la desviación estándar
fis = addmf (fis, 'output', 1, 'NULO'      , 'gaussmf', [ 1   5 ]); 
fis = addmf (fis, 'output', 1, 'MEDIO'     , 'gaussmf', [ 1  10 ]);
fis = addmf (fis, 'output', 1, 'GRAVE'     , 'gaussmf', [ 1  15 ]);

# rules
# Se crean las reglas difusas, donde se especifica el índice de las funciones de membresía de las variables de entrada y salida, el operador lógico y el peso de la regla
# En cada lista los primeros 3 elementos son los índices de las funciones de membresía de las variables de entrada y el cuarto elemento es el índice de la función de membresía de la variable de salida
# Luego se especifica el peso de la regla y por ultimo el operador lógico para las variables de entrada, 1 = and y 2 = or
fis = addrule(fis, [1 0 0  1  0.8  1]);
fis = addrule(fis, [2 2 0  3  0.7  1]);
fis = addrule(fis, [2 1 0  2  0.9  1]);
fis = addrule(fis, [3 2 0  3  0.5  1]);
fis = addrule(fis, [3 2 2  3  0.7  1]);
fis = addrule(fis, [3 1 1  2  0.7  1]);

puts("Reglas:\n");
showrule(fis, 1:columns(fis.rule), 'symbolic'); # Muestra las reglas en forma simbólica (no en índices) obteniendo los nombres de las reglas y de los miembros desde el sistema de inferencia difusa

# plot
# Muestra las funciones de membresía de las variables de entrada y salida
plotmf(fis, 'input', 1); 
plotmf(fis, 'input', 2);
plotmf(fis, 'input', 3);
plotmf(fis, 'output', 1);

inputs = [32 69 19]; # Valores medidos por los sensores
points = 10001; # Cantidad de puntos para evaluar las funciones de membresía
# El espacio 0 a 20 (valor del problema) se divide en 10001 puntos, y se evalúan las funciones de membresía de las variables de salida en esos puntos
[output, rule_input, rule_output, fuzzy_output] = evalfis(inputs, fis, points);
rule_input # Muestra los valores de las variables de entrada para cada regla
output # Muestra el valor de la variable de salida
# rule_output
# fuzzy_output

# Crea un vector con 10001 puntos entre 0 y 20 que va a ser el eje x de las gráficas
x_axis = linspace(fis.output(1).range(1), fis.output(1).range(2), points); # puntos entre 0 y 20
colors = ['r' 'b' 'm' 'g' 'k' 'c']; # Colores para las 6 reglas en la grafica

figure('NumberTitle', 'off', 'Name', 'Salida difusa de las reglas 1-6 para entrada = (32, 69, 19)');
xlabel('Problema', 'FontWeight', 'bold');
ylim([-0.1, 1.1]); # Agrega un poco de espacio arriba y abajo de las gráficas

for i = 1 : length(fis.rule) # Grafica de los valores de salida de las 6 reglas
    plot (x_axis, rule_output(:,i), [colors(i) ";Rule " num2str(i) ";"], 'LineWidth', 2);
    hold on; # Mantiene la gráfica actual para agregar más datos (para no borrar las salidas de la regla anterior)
endfor
grid;


figure('NumberTitle', 'off', 'Name', 'Agregacion y defuzificacion para entrada = (32, 69, 19)');
xlabel('Problema', 'FontWeight', 'bold');
ylim([-0.1, 1.1]);

# Grafica la salida difusa agregada
# Es el maximo de los valores de salida de las 6 reglas en cada punto
plot (x_axis, fuzzy_output(:, 1), "b;Salida difusa agregada;", 'LineWidth', 2);
hold on; # Mantiene la gráfica actual para agregar más datos

# Grafica la salida crisp (defuzificada)
# Es el centroide de la salida difusa agregada
crisp_output = evalmf(x_axis, output(1), 'constant');
plot (x_axis, crisp_output, ["r;Crisp Output = " num2str(output(1)) "%;"], 'LineWidth', 2);
grid;

pause;