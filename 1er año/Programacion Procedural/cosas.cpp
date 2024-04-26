#include <stdio.h>
#include <stdarg.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <time.h>
#include <malloc.h>
#include <unistd.h>
#include <string>
#include <stdexcept> 
#define strLen 20
#define N 3

namespace cadenas{
	// https://en.cppreference.com/w/cpp/string/basic_string
	char* toString(auto x){
		std::string s = std::to_string(x);

		char* string = (char*) malloc(sizeof(char) * s.length());
		strcpy(string, s.c_str()); 

		return string;
 	}

	char* padEnd(char* str, int amount, char* filler){
		int len = strlen(str), fillerLen = strlen(filler);
		if(len >= amount) return str;

		if((amount - len) % fillerLen != 0){
 			throw std::invalid_argument("invalid filler length");
		}

		char* string = (char*) malloc(sizeof(char) * amount);
		strcpy(string, str);

		while(len < amount){
			strcat(string, (const char*) filler);
			len += fillerLen;
		}

		return string;
	}
	char* padStart(char* str, int amount, char* filler){
		int len = strlen(str), fillerLen = strlen(filler);
		if(len >= amount) return str;

		if((amount - len) % fillerLen != 0){
 			throw std::invalid_argument("invalid filler length");
		}

		char* string = (char*) malloc(sizeof(char) * amount);
		strcpy(string, "");

		while(len < amount){
			strcat(string, (const char*) filler);
			len += fillerLen;
		}
		strcat(string, str);

		return string;
	}

	int startsWith(char* string, char* startString){
		int size = strlen(string), sizeS = strlen(startString);
		int i = 0;

		while(i < size && i < sizeS){
			if(string[i] != startString[i++]) return 0;
		}

		return 1;
	}
	int endsWith(char* string, char* endString){
		int size = strlen(string), sizeS = strlen(endString);

		while(sizeS != 0 && size != 0){
			if(string[--size] != endString[--sizeS]) return 0;
		}

		return 1;
	}

	void leerCadena(char* str, int maxLength){
		fflush(stdin);
		fgets(str, maxLength, stdin);

		char* pos = strchr(str, '\n');
		if (pos != NULL) *pos = '\0';
	}
	char* leerCadenaVariable(){
		char* string = NULL;
		int size = 0;

		fflush(stdin);
		char c = getchar();
		while(c != '\n'){
			string = (char*) realloc(string, size + 1);
			string[size++] = c; 
			c = getchar();
		}
		string[size] = '\0';

		return string;
	}
	char* leerCadenaVariableGrande(){
		char* string = NULL;
		int size = 0, t = 0;

		fflush(stdin);
		char c = getchar();
		while(c != '\n'){
			if(size >= t){
				t += 7;
				string = (char*) realloc(string, t + 1);
			}
			string[size++] = c; 
			c = getchar();
		}
		string[size] = '\0';

		return string;
	}
	char* generarString(int maxLength){
		// diccionario de caracteres
		char diccionario[] = {
			'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
			'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
			'w', 'x', 'y', 'z',
			'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
			'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
			'W', 'X', 'Y', 'Z',
			'!', '#', '@', '%', '&', '*', '-', '{', '}', '[', ']',
			'1', '2', '3', '4', '5', '6', '7', '8', '9'
		};

		srand(getpid()); // genero una semilla para poder tener un numero random
		char *string = (char*) malloc(maxLength + 1); // le doy la cantidad de memoria a la variable que guardara la clave
		int len = strlen(diccionario); // obtengo la longitud de caracteres del diccionario

		for(int i = 0; i < maxLength; i++){
			string[i] += diccionario[rand() % len]; // se genera la clave aleatoria
		}
		
		return string; // retorno la clave
	}

	/*
	strlen(cadena); //(la longitud de la cadena sin el caracter final 0)
	strcpy(cadenaDestino, cadena); //cadenaDestino = cadena1
	strcat(cadenaDestino, cadena); //cadenaDestino += cadena

	strcmp(cadena1, cadena2);
	// Devuelve un 0 si las dos cadenas son iguales
	// Un número negativo si <cadena1> es menor que (precede alfabéticamente a) <cadena2> 
	// Un número positivo (mayor que cero) si <cadena1> es mayor que <cadena2>.

	//https://es.stackoverflow.com/questions/31601/guardar-cadena-de-caracteres-en-c
	*/
}

namespace listas{
	typedef struct node {
		struct node *next;
		int value;
	}* nodo_t;

	int obtenerValor(){
		int value;
		printf("Introduzca el valor a guardar\n\e[33m");
		scanf("%i", &value);
		printf("\e[0m");

		return value;
	}

	nodo_t crearCabeza(){
		nodo_t nodo = (nodo_t) malloc(sizeof(struct node));
		nodo->value = -1;
		nodo->next = NULL;

		return nodo;
	}

	void carga(nodo_t nodo){
		int value = obtenerValor();

		while(value != 0){
			nodo->next = (nodo_t) malloc(sizeof(struct node));
			nodo = nodo->next;
			nodo->value = value;
			nodo->next = NULL;

			value = obtenerValor();
		}
	}

	void cargaRecursiva(nodo_t anterior){
		int value = obtenerValor();

		if(value == 0) return;

		nodo_t nodo = (nodo_t) malloc(sizeof(struct node));
		nodo->value = value;
		nodo->next = NULL;

		anterior->next = nodo;

		cargaRecursiva(nodo);
	}

	void cargaOrdenada(nodo_t cabeza){
		nodo_t temp;

		int value = obtenerValor();
		while(value != 0){
			temp = cabeza;

			while(temp->next != NULL && value < temp->next->value){ // cambiar este < para cambiar el orden de carga
				temp = temp->next;
			}
			
			nodo_t nodo = (nodo_t) malloc(sizeof(struct node));
			nodo->value = value;
			
			nodo->next = temp->next;
			temp->next = nodo;
			
			value = obtenerValor();
		}
	}

	//cargaOrdenadaRecursiva(cabeza, NULL, 0)
	void cargaOrdenadaRecursiva(nodo_t cabeza, nodo_t temp, int value){
		if(value != 0){
			if(temp->next != NULL && value > temp->next->value)  // cambiar este < para cambiar el orden de carga
				return cargaOrdenadaRecursiva(cabeza, temp->next, value);

			nodo_t nodo = (nodo_t) malloc(sizeof(struct node));
			nodo->value = value;
			nodo->next = temp->next;
			temp->next = nodo;
		}
		
		value = obtenerValor();
		if(value == 0) return;

		cargaOrdenadaRecursiva(cabeza, cabeza, value);
	}

	void ordenar(nodo_t cabeza){ //metodo burbuja (no mejorado)
		if(cabeza == NULL || cabeza->next == NULL || cabeza->next->next == NULL) return;
		nodo_t temp = cabeza, k = cabeza;

		while(k != NULL){
			k = NULL;
			temp = cabeza;

			while (temp->next->next != NULL){
				if(temp->next->value > temp->next->next->value){  // cambiar este > para cambiar el orden
					nodo_t aux2 = temp->next->next->next;
					nodo_t aux = temp->next;
					temp->next = temp->next->next;
					aux->next = aux2;
					temp->next->next = aux;

					k = temp;
				}
				
				temp = temp->next;
			}
		}
	}

	// ordenarRecursivo(cabeza, cabeza, cabeza);
	void ordenarRecursivo(nodo_t cabeza, nodo_t temp, nodo_t k){ //metodo burbuja (no mejorado)
		if(cabeza->next == NULL || cabeza->next->next == NULL) return;

		if(temp->next->next != NULL){
			if(temp->next->value > temp->next->next->value){  // cambiar este > para cambiar el orden
				nodo_t aux2 = temp->next->next->next;
				nodo_t aux = temp->next;
				temp->next = temp->next->next;
				aux->next = aux2;
				temp->next->next = aux;

				k = temp;
			}
			ordenarRecursivo(cabeza, temp->next, k);
		}else if(k != NULL) ordenarRecursivo(cabeza, cabeza, NULL);
	}

	void mostrar(nodo_t nodo){
		if(nodo->next == NULL) return;
		int i = 1;
		do{
			printf("Nodo: \e[31m%i\e[0m value: \e[33m%i\e[0m\n", i++, nodo->next->value);
			nodo = nodo->next;
		}while(nodo->next != NULL);
	}

	// mostrarRecursivo(cabeza, 1);
	void mostrarRecursivo(nodo_t nodo, int i){
		if(nodo->next == NULL) return;
		printf("Nodo: \e[31m%i\e[0m value: \e[33m%i\e[0m\n", i, nodo->next->value);
		mostrarRecursivo(nodo->next, i + 1);
	}

	void ultimoPar(nodo_t nodo){
		if(nodo->next == NULL && (nodo->value % 2) == 0){
			printf("\nEl ultimo numero de la lista es par");
			return;
		}
		ultimoPar(nodo->next);
	}

	void freeLista(nodo_t nodo){
		nodo_t aux;
		while(nodo != NULL){
			aux = nodo->next;
			free(nodo);
			nodo = aux;
		}
	}

	void freeListaRecursivo(nodo_t nodo){
		if(nodo->next != NULL) freeLista(nodo->next);
		free(nodo);
	}

	void cargarLista(nodo_t cabeza, int argsAmount, ...){
		va_list valist;
		va_start(valist, argsAmount);

		nodo_t ultimoNodo = cabeza;

		for(int i = 0; i < argsAmount; i++){
			int value = va_arg(valist, int);

			ultimoNodo->next = (nodo_t) malloc(sizeof(struct node));
			ultimoNodo = ultimoNodo->next;
			ultimoNodo->value = value;
			ultimoNodo->next = NULL;
		}

		va_end(valist);
	}

	void cargarListaAleatoria(nodo_t cabeza, int cant, int max){
		srand(time(NULL));
		nodo_t ultimoNodo = cabeza;

		while(cant-- > 0){
			ultimoNodo->next = (nodo_t) malloc(sizeof(struct node));
			ultimoNodo = ultimoNodo->next;
			ultimoNodo->value = rand() % max;
			ultimoNodo->next = NULL;

			ultimoNodo = ultimoNodo->next;
		}
	}
}

namespace numeros{
	int min(int argsAmount, int first, ...){
		va_list valist;
		va_start(valist, argsAmount);

		int min = first, i;
		for (i = 0; i < argsAmount; i++) {
			int num = va_arg(valist, int);
			if(num < min) min = num;
		}
			
		va_end(valist);

		return min;
	}
	int max(int argsAmount, int first, ...){
		va_list valist;
		va_start(valist, argsAmount);

		int max = first, i;
		for (i = 0; i < argsAmount; i++) {
			int num = va_arg(valist, int);
			if(num > max) max = num;
		}
			
		va_end(valist);

		return max;
	}
	int prom(int argsAmount, ...){
		va_list valist;
		va_start(valist, argsAmount);

		int total = 0, i;
		for (i = 0; i < argsAmount; i++) {
			total += va_arg(valist, int);
		}

		va_end(valist);

		if(total == 0) return 0;
		return total / argsAmount;
	}
	
	/*
	srand(time(NULL));
	srand(getpid());
	srand48(time(NULL)); 
	srand48(getpid());

	// RAND_MAX es un numero que cambia segun el compilador, lo normal es 2.147.483.647 (0x7FFFFFFF) o 32.767 (0x7FFF)
	rand() 							//Da un numero entero entre 0 y RAND_MAX
	(rand() % N) 					//Da un numero entero entre 0 y N - 1 (siempre que N sea menor que RAND_MAX)
	(rand() % N) + X 				//Da un numero entero entre X y (N - 1 + X) (siempre que N sea menor que RAND_MAX)
	(rand() / (float) RAND_MAX) 	//Da un numero flotante entre 0 y 1
	drand48() 						//Da un numero flotante entre 0 y 1 (es el equivalente a (rand() / (float) RAND_MAX))
	drand48() * N 					//Da un numero flotante entre 0 y N
	drand48() * N + X 				//Da un numero flotante entre X y (N + X)
	*/
}

namespace ordenamientos{
	void ordenar1(int arreglo[N]){ //metodo burbuja mejorado
		int k = 1, i, aux, cota = N - 1;

		while(k != -1){
			k = -1;

			for(i = 0; i < cota; i++){
				if(arreglo[i] > arreglo[i + 1]){ //ascendente
					aux = arreglo[i];
					arreglo[i] = arreglo[i + 1];
					arreglo[i + 1] = aux;
					k = i;
				}
			}

			cota = k;
		}
	}

	void ordenar2(int arreglo[N]){ //metodo seleccion
		int i, j, min, aux;

		for(i = 0; i < (N - 1); i++){
			min = i;
			for(j = (i + 1); j < N; j++){
				if(arreglo[j] < arreglo[min]) min = j; //ascendente
			}

			aux = arreglo[i];
			arreglo[i] = arreglo[min];
			arreglo[min] = aux;
		}
		return;
	}

	void ordenar3(int arreglo[N]){ //metodo insercion
		int i, j, valor;

		for(i = 1; i < N; i++){
			valor = arreglo[i];
			j = i - 1;
			while((j >= 0) && (valor < arreglo[j])){//ascendente
				arreglo[j+1] = arreglo[j];
				j--;
			}
			arreglo[j+1] = valor;
		}
	}
}

namespace busquedas{
	int buscar(int arreglo[N], int elem){ //Busqueda sin bandera
		int i = 0;

		while((i < N) && (arreglo[i] != elem)) i++;

		return i;
	}

	int buscar1(int arreglo[N], int elem){ //Busqueda binaria (no secuencial)
		int inf = 0, sup = N - 1, medio = (inf + sup) / 2;

		while ((inf <= sup) && (elem != arreglo[medio])){
			if(elem < arreglo[medio]){
				sup = medio - 1;
			}else inf = medio + 1;
			medio = (inf + sup) / 2;
		}

		if (inf > sup) medio = -1;

		return medio;
	}

	int buscar2(int arreglo[N], int elem){ //Busqueda con bandera
		int i = 0;
		bool encontro = false;

		while((i < N) && (!encontro)){
			if(arreglo[i] == elem){
				encontro = true;
			}else i++;
		}

		return i;
	}

	int buscar3(int arreglo[N+1], int elem){ //Busqueda con elemento sentinela
		int i = 0;
		arreglo[N] = elem;

		while (arreglo[i] != elem) i++;
		return i;
	}
}

namespace colores{
	//Regular text
	const char* BLK = "\e[0;30m";
	const char* RED = "\e[0;31m";
	const char* GRN = "\e[0;32m";
	const char* YEL = "\e[0;33m";
	const char* BLU = "\e[0;34m";
	const char* MAG = "\e[0;35m";
	const char* CYN = "\e[0;36m";
	const char* WHT = "\e[0;37m";

	//Regular bold text
	const char* BBLK = "\e[1;30m";
	const char* BRED = "\e[1;31m";
	const char* BGRN = "\e[1;32m";
	const char* BYEL = "\e[1;33m";
	const char* BBLU = "\e[1;34m";
	const char* BMAG = "\e[1;35m";
	const char* BCYN = "\e[1;36m";
	const char* BWHT = "\e[1;37m";

	//Regular underline text
	const char* UBLK = "\e[4;30m";
	const char* URED = "\e[4;31m";
	const char* UGRN = "\e[4;32m";
	const char* UYEL = "\e[4;33m";
	const char* UBLU = "\e[4;34m";
	const char* UMAG = "\e[4;35m";
	const char* UCYN = "\e[4;36m";
	const char* UWHT = "\e[4;37m";

	//Regular background
	const char* BLKB = "\e[40m";
	const char* REDB = "\e[41m";
	const char* GRNB = "\e[42m";
	const char* YELB = "\e[43m";
	const char* BLUB = "\e[44m";
	const char* MAGB = "\e[45m";
	const char* CYNB = "\e[46m";
	const char* WHTB = "\e[47m";

	//High intensty background 
	const char* BLKHB = "\e[0;100m";
	const char* REDHB = "\e[0;101m";
	const char* GRNHB = "\e[0;102m";
	const char* YELHB = "\e[0;103m";
	const char* BLUHB = "\e[0;104m";
	const char* MAGHB = "\e[0;105m";
	const char* CYNHB = "\e[0;106m";
	const char* WHTHB = "\e[0;107m";

	//High intensty text
	const char* HBLK = "\e[0;90m";
	const char* HRED = "\e[0;91m";
	const char* HGRN = "\e[0;92m";
	const char* HYEL = "\e[0;93m";
	const char* HBLU = "\e[0;94m";
	const char* HMAG = "\e[0;95m";
	const char* HCYN = "\e[0;96m";
	const char* HWHT = "\e[0;97m";

	//Bold high intensity text
	const char* BHBLK = "\e[1;90m";
	const char* BHRED = "\e[1;91m";
	const char* BHGRN = "\e[1;92m";
	const char* BHYEL = "\e[1;93m";
	const char* BHBLU = "\e[1;94m";
	const char* BHMAG = "\e[1;95m";
	const char* BHCYN = "\e[1;96m";
	const char* BHWHT = "\e[1;97m";

	//Reset
	const char* RESET = "\e[0m";
}

void pretyPrint(char* str, ...){
	const char validFormats[] = { 'i', 'c', 's', 'b', 'd' };
	// prettyPrint("Cosas %i %b %s %c", 32, 1, "asd", 'a');
	int length = strlen(str);
	int count = 0;

	for(int i = 0; i < length; i++){
		if(
			str[i] == '%' && 
			strchr(validFormats, str[i + 1]) != NULL
		) count++;
	}

	va_list valist;
	va_start(valist, count);

	for(int i = 0; i < length; i++){
		if(str[i] == '%' && strchr(validFormats, str[i + 1]) != NULL){
			char next = str[++i];

			switch(next){
				case 'd':
				case 'i':{
					printf("\e[33m%i\e[0m", va_arg(valist, int));
					continue;
				}
				case 'c':{
					printf("\e[32m'%c'\e[0m", va_arg(valist, int));
					continue;
				}
				case 's':{
					printf("\e[32m\"%s\"\e[0m", va_arg(valist, char*));
					continue;
				}
				case 'b':{
					printf("\e[33m%s\e[0m", va_arg(valist, int) ? "true" : "false");
					continue;
				}
			}
		}
		
		printf("%c", str[i]);
	}

	va_end(valist);
}

namespace misc{
	int obtenerValor(char* msg, char* msg2, int min, int max){
		int valor = 0;

		printf(msg);
		scanf("%d", &valor);
		while(valor < min || valor > max){
			printf(msg2);
			scanf("%d", &valor);
		}

		return valor;
	}
}