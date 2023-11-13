function IntegracionSimpson3_8 ()
	disp('    Integracion Simpson 3/8');
	disp('Ingrese el numero de intervalos: ')
	n = input('');

	if n < 3 || modulo(n, 3) ~= 0
		disp('Error: la cantidad de puntos es invalida\n');
		return;
	end
	
	disp('Ingrese el valor de a: ');
	a = input('');
	disp('Ingrese el valor de b: ');
	b = input('');

	h = (b - a) / n;

	X = a : h : b;
	Y = zeros(n + 1);

	for i = 1 : n + 1
		printf('Ingrese el valor de f(%f) = ', X(i));
		Y(i) = input('');
	end

	suma = 0;

	for i = 1 : 3 : n
		suma = suma + Y(i) + 3*Y(i+1) + 3*Y(i+2) + Y(i+3);
	end

	suma = suma * 3 * h / 8;

	printf('   i    X(i)    Y(i)\n');
	for i = 1 : n + 1
		printf('%4d  %7.5f  %7.5f\n', i, X(i), Y(i));
	end
	
	printf('\nEl valor de la integral es: %f\n', suma);
end

function IntegracionSimpson3_8_2 ()
	disp('    Integracion Simpson 3/8');
	disp('Ingrese el numero de intervalos: ')
	n = input('');

	if n < 3 || modulo(n, 3) ~= 0
		disp('Error: la cantidad de puntos es invalida\n');
		return;
	end
	
	disp('Ingrese el valor de a: ');
	a = input('');
	disp('Ingrese el valor de b: ');
	b = input('');

	h = (b - a) / n;

	X = a : h : b;
	Y = zeros(n + 1);

	disp('Ingrese f(x) = ');
	f = input('', 'string');
	
	for i = 1 : n + 1
		x = X(i);
		Y(i) = evstr(f);
	end

	suma = 0;

	for i = 1 : 3 : n
		suma = suma + Y(i) + 3 * Y(i+1) + 3 * Y(i+2) + Y(i+3);
	end

	suma = suma * 3 * h / 8;

	printf('   i    X(i)    Y(i)\n');
	for i = 1 : n + 1
		printf('%4d  %7.5f  %7.5f\n', i, X(i), Y(i));
	end
	
	printf('\nEl valor de la integral es: %f\n', suma);
end
