function [L]=lagrange()
disp('Ingrese cantidad de elementos');
n=input (' ');

for i=1:n
  printf('x%d =', i);
  x(i)=input(' ');
end  

for k =1:n
 Lk = poly([1], 'x', 'c');
 deno = 1;
 for i=1:n
  if i ~= k
  Lk = Lk*poly([x(i)], 'x');
  deno = deno*(x(k) - x(i));
 end
end
 Lk = Lk/deno;
 // ingreso de los valores de la función evaluada en los x(i)
printf('f(x(%d)) = ',k);
y(k)= input(' '); 
fLk(k)=y(k)*prod(Lk); 
L=sum(fLk);
end
x1=[-5:0.05:5];
y=x1^2;

clf();//borra pantalla grafica
xtitle('título de la gráfica', ' eje x', ' eje y');
plot(x1,y,'r');
x1=2;
y=-2:0.01:5;

plot(x1,y,'b');
//plot(-1,1,'b');
//plot(x,y);
endfunction
