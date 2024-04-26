/*
La salida de un periférico consta de dos números binarios codificados en BCD natural (para
representar las unidades y decenas decimales) conformados por dos grupos de 4 líneas. Se pretende
ingresar esta información al computador para que un programa realice, para cada dígito decimal, la
conversión de BCD natural a 7 segmentos con el propósito de alimentar un par de displays de 7
segmentos para que se pueda visualizar la salida del periférico.
Con este propósito, las salidas A0, A1, A2 y A3 del periférico, que conforman la salida BCD natural
que representa las unidades, son ingresadas por las líneas PA0, PA1, PA2 y PA3 respectivamente de la
PIA N° 0 y las salidas B0, B1, B2 y B3 del periférico, que conforman la salida BCD natural que
representa las decenas, son ingresadas por las líneas PA4, PA5, PA6 y PA7 respectivamente de la
misma PIA N° 0. Además, cuando el periférico vuelca un nuevo valor sobre sus salidas lo indica al
exterior generando un pulso negativo sobre una línea de control que es ingresada a la línea CA1 de la
PIA N° 0 para que al detectarse un flanco negativo se interrumpa al uP para que se ejecute la rutina de
servicio que debe atender al periférico. Sobre las líneas PB0 a PB6 de la PIA N° 1 se conectan las
líneas de entrada de los leds correspondientes a los segmentos del display usado para las unidades y
sobre las líneas PA0 a PA6 de la misma PIA N° 1 se conectan las líneas de entrada de los leds
correspondientes al display de 7 segmentos usado para las decenas.
La conversión de BCD natural a 7 segmentos para cada dígito decimal será realizada invocando a la
subrutina “BCD7SE” cuyo único parámetro de entrada es el N° BCD a convertir, el que debe ser
cargado en los 4 bits menos significativos del registro B y los 7 bits del resultado de la conversión
serán cargados en los bits b0 a b6 del registro C (parámetro de salida) en correspondencia a los
segmentos “a” hasta “g” del display.
Escribir el programa de inicialización de las PIAs y la rutina de servicio que ejecute dicha tarea.
*/

	ORG 1748d
	;salvaguarda de los registros en memoria pila
	PUSH AF
	PUSH BC
	PUSH DE
	PUSH HL
	PUSH IX
	PUSH IY
	IN A,(02d) ;lectura de los números BCD presentes en la salida del periférico
	LD B,A ;carga del parámetro de entrada de la subrutina (Nº BCD correspondiente a las
	;unidades)
	PUSH AF ;salvaguarda en memoria pila de los Nºs BCD leídos (salvaguarda de A)
	CALL BCD7SE ;se invoca a la subrutina que realiza la conversión guardando el resultado en el
	;registro C (parámetro de salida)
	LD A,C ;almacena en A el resultado de la conversión
	OUT (13d),A ;se actualiza el display 7 segmentos de las unidades
	POP AF ;recuperación en el registro A de los Nºs BCD leídos y salvaguardados en pila
	SRL A ;se realizan cuatro desplazamientos lógicos a derecha de los bits del acumulador
	SRL A ;con el objeto de ubicar el Nº BCD correspondiente a las decenas en los cuatro
	SRL A ;bits menos significativos del registro A
	SRL A
	LD B,A ;carga del parámetro de entrada de la subrutina (Nº BCD correspondiente a las
	;decenas)
	CALL BCD7SE ;se invoca a la subrutina que realiza la conversión guardando el resultado en el
	;registro C (parámetro de salida)
	LD A,C ;almacena en A el resultado de la conversión
	OUT (10d),A ;se actualiza el display 7 segmentos de las decenas
	POP IY
	POP IX
	POP HL
	POP DE
	POP BC
	POP AF
	RETI
	END

; El programa de inicialización de las PIAs queda propuesto para el alumno.