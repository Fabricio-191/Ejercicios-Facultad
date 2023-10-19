function [L] = lagrange(x, y)
	printf('x, y');
	n = length(x);

	for k = 1:n
		Lk = poly([1], 'x', 'c');
		deno = 1;
		for i = 1:n
			if i ~= k
				Lk = Lk * poly([x(i)], 'x');
				deno = deno * (x(k) - x(i));
			end
		end
		Lk = Lk / deno;

		fLk(k) = y(k) * prod(Lk); 
		L = sum(fLk);
	end

	x1 = [-5:0.05:5];
	y = x1^2;

	clf(); // borra pantalla gráfica
	xtitle('título de la gráfica', 'eje x', 'eje y');
	plot(x1, y, 'r');
	x1 = 2;
	y = -2:0.01:5;

	plot(x1, y, 'b');
	// plot(-1,1,'b');
	// plot(x,y);
endfunction
