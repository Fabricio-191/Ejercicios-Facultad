/*
En la provincia de San Juan se instaló una plataforma de pedidos de comida denominada PediYA!. Es una tienda
que permite realizar pedidos de comida a diferentes restaurantes. Para poder hacer uso de esta nueva plataforma es
necesario que tanto los Restaurantes como los Clientes se encuentren registrados; también cuenta con los datos de
los pedidos que se realizan.

Implementación

Para administrar las funcionalidades del sistema debe incluir módulos que permitan:
 Crear los archivos indicados.
 Registrar el alta de nuevos clientes en archivo.
 Registrar el alta de nuevos restaurantes.
 Registrar la baja tanto de restaurantes como de empleados, solo se puede hacer al inicio o fin de sesión y se
debe reasignar el ID para mantener el acceso directo.
 Registrar el ingreso y eliminación de pedidos.
 Realizar un listado de restaurantes que contiene la plataforma.
 Informar por restaurante la cantidad de pedidos.
 Informar cuantos restaurantes reciben solo tarjeta de crédito, cuantos solo efectivo y cuantos ambos tipos de
pago.
 Informar datos de restaurantes por tipo de entrega ingresado por teclado.
 Informar diariamente cuanto es lo que recauda la plataforma, sabiendo que es el 5% de la venta de cada
restaurante. Discriminar por restaurante.
 Informar diariamente el Importe total vendido desde de la plataforma.
 Informar diariamente cual es el método de pago más usado por los clientes.
 Informar diariamente cual es el método de entrega más usado por los clientes.
 Informar diariamente el menor y máximo monto recaudado en pedidos.
 Realizar un listado de cantidad de clientes que posee la plataforma.
 Dado el DNI de un empleado, indicar la su número de teléfono y la información de los pedidos que debe
entregar.
 Hacer respaldo de la información en uso, en archivos en formato de texto.
Nota: en base a estas especificaciones armar el diseño modular.
*/

#include "header.h"
#include <stdio.h>
#include <malloc.h>
#include <string.h>

void leerString(char* string, int limit, FILE* archivo){
	fgets(string, limit, archivo);
	string[strlen(string) - 1] = '\0';
}

void menu() {
	printf("0. Terminar");
	printf("1. Agregar pedido");
	printf("2. Eliminar pedido");
	printf("3. Agregar restaurante");
	printf("4. Eliminar restaurante");
	printf("5. Agregar empleado");
	printf("6. Eliminar empleado");
}

int main() {
	restaurante* restaurantes;
	empleado* empleados;
	pedido* pedidos;

	int cantPedidos,
		cantEmpleados,
		cantRestaurantes = leerRestaurantes(restaurantes);

	int opcion;
	do{
		menu();
		scanf("%d", &opcion);

		switch (opcion) {
			case 1:{ //agregar pedido

			}
			case 2:{ //quitar pedido

			}
			case 3:{ //agregar restaurante

			}
			case 4:{ //quitar restaurante

			}
			case 5:{ //agregar empleados

			}
			case 6:{ //quitar empleados

			}
			default:{
				printf("Opcion desconocida\n");
			}
		}
	}while(opcion != 0);

	printf("\n\nFin del programa\n");
	return 0;
}