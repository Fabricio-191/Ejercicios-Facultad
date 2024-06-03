# pkg install "https://downloads.sourceforge.net/project/octave/Octave%20Forge%20Packages/Individual%20Package%20Releases/strings-1.3.1.tar.gz"
# pkg install "https://github.com/lmarkowsky/fuzzy-logic-toolkit/archive/refs/tags/0.5.1.tar.gz"
pkg load strings
pkg load fuzzy-logic-toolkit

fis = newfis('Ejercicio5');

# inputs
fis = addvar(fis, 'input' , 'Lluvia',        [ 0  100 ]);
fis = addmf (fis, 'input' , 1, 'BAJA'      , 'trapmf',  [ -1   0  25  40 ]);
fis = addmf (fis, 'input' , 1, 'IMPORTANTE', 'trapmf',  [ 20  50  50  70 ]);
fis = addmf (fis, 'input' , 1, 'INTENSA'   , 'trapmf',  [ 60  70 100 120 ]);
 
fis = addvar(fis, 'input' , 'Suelo',         [ 0  100 ]);
fis = addmf (fis, 'input' , 2, 'HUMEDO'    , 'trapmf',  [ 15  35  35  80 ]);
fis = addmf (fis, 'input' , 2, 'EMPAPADO'  , 'trapmf',  [ 45  70 100 120 ]);
 
fis = addvar(fis, 'input' , 'Topografia',    [ 0  100 ]);
fis = addmf (fis, 'input' , 3, 'SUAVE'     , 'trapmf',  [  2   4  15  25 ]);
fis = addmf (fis, 'input' , 3, 'ESCARPADA' , 'trapmf',  [ 10  20  30  50 ]);

# outputs
fis = addvar(fis, 'output', 'Problema', [ 0  20 ]); 
fis = addmf (fis, 'output', 1, 'NULO'      , 'gaussmf', [ 1   5 ]);
fis = addmf (fis, 'output', 1, 'MEDIO'     , 'gaussmf', [ 1  10 ]);
fis = addmf (fis, 'output', 1, 'GRAVE'     , 'gaussmf', [ 1  15 ]);

# rules
fis = addrule(fis, [1 0 0  1  0.8  1]);
fis = addrule(fis, [2 2 0  3  0.7  1]);
fis = addrule(fis, [2 1 0  2  0.9  1]);
fis = addrule(fis, [3 2 0  3  0.5  1]);
fis = addrule(fis, [3 2 2  3  0.7  1]);
fis = addrule(fis, [3 1 1  2  0.7  1]);

puts("Reglas:\n");
showrule(fis, 1:columns(fis.rule), 'symbolic');

# plot
plotmf(fis, 'input', 1);
plotmf(fis, 'input', 2);
plotmf(fis, 'input', 3);
plotmf(fis, 'output', 1);

inputs = [32 69 19];
points = 10001;
[output, rule_input, rule_output, fuzzy_output] = evalfis(inputs, fis, points);
rule_input
output
# rule_output
# fuzzy_output

x_axis = linspace(fis.output(1).range(1), fis.output(1).range(2), points); # puntos entre 0 y 20
colors = ['r' 'b' 'm' 'g' 'k' 'c'];

figure('NumberTitle', 'off', 'Name', 'Salida difusa de las reglas 1-6 para entrada = (32, 69, 19)');
xlabel('Problema', 'FontWeight', 'bold');
grid;
ylim([-0.1, 1.1]);

for i = 1 : length(fis.rule)
    plot (x_axis, rule_output(:,i), [colors(i) ";Rule " num2str(i) ";"], 'LineWidth', 2);
    hold on;
endfor


figure('NumberTitle', 'off', 'Name', 'Agregacion y defuzificacion para entrada = (32, 69, 19)');
xlabel('Problema', 'FontWeight', 'bold');
grid;
ylim([-0.1, 1.1]);

plot (x_axis, fuzzy_output(:, 1), "b;Aggregated Fuzzy Output;", 'LineWidth', 2);
hold on;
crisp_output = evalmf(x_axis, output(1), 'constant');
plot (x_axis, crisp_output, ["r;Crisp Output = " num2str(output(1)) "%;"], 'LineWidth', 2);

pause;