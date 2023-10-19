function difat(XX, YY)
	n = length(XX);
	for i=1:n
		t(i,1) = XX(i)
		t(i,2) = YY(i)
	end

	x0 = t(1,1); 
	h = t(2,1) - t(1,1); //Calcula h

	n = size(t,1);
	disp('Muestra la tabla armada:')
	disp(t)  

	// Calcula valores de la tabla    
	for j=1:n-1
		for i=1+j:n
			t(i, j+2) = t(i, j+1) - t(i-1, j+1);
		end
	end

	// Muestra encabezado de la tabla  
	disp('Tabla de Diferencias Atrasadas')
	printf('  i         xi            fi           ∇i   \t    ');
	for i=2:n-1
		printf('∇%dfi        ', i);
	end

	// Muestra valores de la tabla
	printf('\n  %d', 0);
	printf('    %10.7f', t(1,1));
	printf('    %10.7f', t(1,2));    
	for i=1:n-1
		printf('\n  %d',i);
		printf('    %10.7f', t(i+1, 1));
		printf('    %10.7f', t(i+1, 2));
		for j=1:i
			printf('  %10.7f', t(i+1, j+2));
		end
	end
	printf('\n\n');
	printf('\n\n Ingrese valor de x para calcular θ: ');
	x = input(''); 

	if (x<t(n,1))&(x>(t(n,1)-h)) then
		s = (x-t(n,1))/h;      //Calcula valor de θ
		printf('s = %f',s);
		printf('\n\n');
		//Calcula coeficientes binomiales
		disp('Coeficientes Binomiales:')
		for i=1:n
			sn(i) = 1/factorial(i-1);
			for j=1:i-1
				sn(i) = sn(i) * (s+j-1);
			end
			printf('\n s(%d) = %f',i-1,sn(i));
		end
		printf('\n\n');
		//Calcula imagen de x
		gx=0;
		for i=1:n
			gx = gx + sn(i) * t(n, i+1);
		end
		disp('Imagen de x ingresada por teclado:')
		printf('\n\n g(%f) = %10.7f', x, gx);
	else 
		printf ('Error en el valor ingresado');
	end
endfunction
