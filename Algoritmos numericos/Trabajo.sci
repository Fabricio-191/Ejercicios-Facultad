/*
function IntegracionSimpson1_3 (X, Y)
    n = length(X);
	suma = 0;
	h = X(2) - X(1);
	
	for i=1 : 2 : n-2
		suma = suma + Y(i) + 4 * Y(i+1) + Y(i + 2);
	end

	suma = suma * h / 3;
	
	printf('El valor de la integral es: %f\n', suma);
end
*/

function mostrarTabla(X, Y)
	n = length(X);
	printf('   i   |   X   |   Y   \n');
	printf('-----------------------\n');
	for i=1 : n
		printf('   %d   |   %f   |   %f   \n', i, X(i), Y(i));
	end
end

function IntegracionSimpson3_8 ()
	disp('    Integracion Simpson 3/8');
	dips('Ingrese el numero de puntos: ')
	n = input('');
	disp('Ingrese el valor de x0: ');
	x0 = input('');
	disp('Ingrese el valor de h: ');
	h = input('');

	if mod(n, 3) ~= 1
		disp('Error: n debe ser multiplo de 3');
		return;
	end

	X = x0 : h : x0 + (n-1)*h;
	Y = [];

	for i=1 : n
		displ('Ingrese el valor de f(x) en x = ', X(i));
		Y(i) = input('');
	end

	IntegracionSimpson3_8_2(X, Y)
end

function IntegracionSimpson3_8_2 (X, Y)
	disp('    Integracion Simpson 3/8');
	n = length(X);
	x0 = X(1);
	h = X(2) - X(1);

	if mod(n, 3) ~= 1 then
		disp('Error: n debe ser multiplo de 3');
		return;
	elseif length(X) ~= length(Y) then
		printf('Error: X e Y deben tener la misma longitud\n');
		return;
	else 
		for i=1 : n - 1
			if X(i) - X(i + 1) ~= h then
				printf('Error: Los valores en X deben estar igualmente espaciados\n');
				return;
			end
		end
	end
	
	suma = 0;

	for i=1 : 3 : n-3
		suma = suma + Y(i) + 3*Y(i+1) + 3*Y(i+2) + Y(i+3);
	end

	suma = suma * 3 * h / 8;
	
	printf('El valor de la integral es: %f\n', suma);
end


function IntegracionSimpson3_8_2 (X, Y)
	disp('    Integracion Simpson 3/8');
	n = length(X);
	x0 = X(1);
	h = X(2) - X(1);
	
	suma = 0;

	for i=1 : 3 : n-3
		suma = suma + Y(i) + 3*Y(i+1) + 3*Y(i+2) + Y(i+3);
	end

	suma = suma * 3 * h / 8;
	
	printf('El valor de la integral es: %f\n', suma);
end