function difad(x, y)
	printf('cantidad de datos, x0, separación entre muestras');
	n = length(x);
	for i=1:n
		t(i,1) = x(i)
		t(i,2) = y(i)
	end

	
	x0 = t(1,1); 
	h = t(2,1) - t(1,1); //Calcula h
	
	disp('Muestra de la tabla armada:');
	disp(t);
	n = size(t,1);
	
	// Calcula valores de la tabla  
	for j=1:n-1
		for i=1:n-j
			t(i, j+2) = t(i+1, j+1) - t(i, j+1);
		end
	end
	
	// Encabezado de la tabla
	disp('Tabla de Diferencias Adelantadas');
	printf('  i         xi            fi           Δi   \t    ');
	
	for i=2:n-1
		printf('Δ%dfi        ', i);
	end
	
	for i=1:n-1
		printf('\n  %d',i-1);
		printf('    %10.7f', t(i,1));
		printf('    %10.7f', t(i,2));
		
		for j=1:n-i
			printf('  %10.7f', t(i, j+2));
		end
	end
	
	printf('\n  %d', n-1);
	printf('    %10.7f', t(n,1));
	printf('    %10.7f', t(n,2));
	printf('\n\n');
	printf('\n\n Ingrese valor de x para calcular θ : ');
	
	x = input(''); 
	
	if (x>x0)&(x<(x0+h)) then
		s = (x-x0)/h;          // Calcula valor de theta(θ)
		printf('θ  = %f',s);
		printf('\n\n');
		disp('Coeficientes Binomiales:');
		
		// Calcula coeficientes binomiales
		for i=1:n
			sn(i) = 1/factorial(i-1);
			
			for j=1:i-1
				sn(i) = sn(i) * (s-j+1);
			end
			
			printf('\n θ (%d) = %f',i-1,sn(i));
		end
		
		gx = 0;
		printf('\n\n');  
		disp('Imagen de la absisa x ingresada por teclado:');
		
		// Calcula imagen de x (ingresada por teclado)
		for i=1:n
			gx = gx + sn(i) * t(1, i+1);
		end
		
		printf('\n g(%f) = %10.7f', x, gx);
	else 
		printf ('Error en el valor ingresado');
	end 
endfunction
