function difdiv()
  disp('Ingrese cantidad de elementos:');
  n=input (' ');
 disp('valores de x:') 
 for i=1:n
  printf('x%d =', i);
  x(i)=input(' ');
end  
disp('valores de y:') 
 for i=1:n
  printf('y%d =', i);
  y(i)=input(' ');
 end  
 m=length(x);
 DD = zeros(n,m+1);
 for i=1:length(y)
  DD(i,1)=x(i)
  DD(i,2)=y(i);
 end
 for j=2:m
  for i=1:n-j+1
   Djfi = ( DD(i+1,j) - DD(i,j) )/( x(i+j-1) - x(i) );
   DD(i,j+1) = Djfi;
  end
end
for i=1:n
    for j=2:n+1
     D(i,j-1)=DD(i,j)     
    end
end
format(3)
disp(' Diferencias Divididas: ');
//for para imprimir en la forma de la tabla
for i=1:n
     for j=1:n
         if (i+j) <= (n+1) 
             printf('%3.7f  ', D(i,j))
             if (i+j)==(n+1) 
                 printf("\n")
             end
         end
     end
 end
 
 j=1;i=1
 disp(' Polinomio Resultante:');

for k=2:1:n+1
  printf('%3.7f  ',DD(j,k));
  for kk=1:1:k-2
      printf('*(x-%3.7f)',x(kk));
  end  
  if (k<>n+1)
      printf('+')   
  end  
end

endfunction
