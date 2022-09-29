/*
Se pretende que las líneas de datos PA0 a PA7 de la PIA Nº 0 se comporten como las salidas de un contador binario de 8 bits cuyo valor se incremente en uno cada 5 segundos.

El valor de inicio del contador estará dado por las salidas de un periférico de 8 bits conectado a las líneas de datos PA0 a
PA7 de la PIA Nº 1 y el valor de finalización del conteo estará dado por las salidas de otro periférico de 8 bits conectado a las líneas de datos PB0 a PB7 de la misma PIA Nº 1.

El contador comienza a evolucionar a partir del valor de inicio al detectarse un flanco positivo sobre la línea CA1 de la PIA
Nº 0, lo que produce un pedido de interrupción sobre el uP que hace ejecutar la rutina de servicio correspondiente.

La tarea de la rutina de servicio finaliza cuando las salidas del contador alcanzan el valor de finalización leído, retornándose el control al programa interrumpido. 
Escriba el programa de inicialización de las PIAs y la rutina de servicio que implemente dicha función.

El intervalo de 5 segundos entre cada incremento debe obtenerse invocando a la subrutina de tiempo parametrada cuyo
nombre es DELAY y su único parámetro de entrada es el tiempo de retardo dado en segundos que debe cargarse en el registro L
*/

