#include "header.h"
#include <stdio.h>
#include <malloc.h>
const char* ruta = "../Archivos/RESTAURANTES.dat";
/*
Pedidos
En cuanto a la información de los Pedidos que realizan los clientes, esta debe ser almacenada temporalmente
durante el día, en una estructura auxiliar lista.

Cuando un Cliente hace un pedido (se verifica que el cliente esté registrado, si no lo está se le da de alta en ese
momento) se le pregunta por el nombre del restaurante, que alimentos solicita y Tipo de entrega (validar si el
restaurante la tiene). El operador de PediYa! informa al cliente el importe del pedido, (si el cliente tiene cupón de
descuento le aplica el 10% de correspondiente). Si el importe a pagar es mayor a $ 4000 se le asigna un cupón de
descuento. Una vez que se informó el importe de pedido, se le pregunta al cliente que Forma de pago elige.
Confirmado el pedido se debe informar al cliente el tiempo estimado de entrega.

Para entregar un pedido, se elige al empleado que tiene la menor cantidad de pedidos a entregar. Se estima quince
minutos para la entrega de cada pedido por empleado, por lo tanto, el tiempo de entrega se calcula en función de
estos dos datos.

El empleado, al momento de registrar la cantidad de 5 pedidos comienza la entrega. Cuando concluye la entrega
se actualiza: en el arreglo de empleados la cantidad de pedidos (se inicializa en cero), en el arreglo de restaurantes se
acumula el importe del pedido y en la lista de pedidos se eliminan los entregados.
El sistema incluye una opción de respaldo de la información en uso, en archivos en formato de texto. Se guarda
en archivo de texto la información de la lista (con los pedidos) y de los arreglos (de empleados y de restaurantes).

struct pedido {
	int IDcliente, IDrestaurante, IDempleado, medioPago, tipoEntrega;
	float importe, tiempoEntrega;
	char alimentosSolicitados[200];
};
*/

pedido obtenerDatos(){
	pedido p;

	char nombreCliente[50];
	printf("Introduzca el nombre del cliente\n");
	scanf("%s", nombreCliente);

	if(!estaRegistrado(nombreCliente)) agregarCliente(nombreCliente);

	char nombreRestaurante[50];
	printf("Introduzca el nombre del restaurante\n");
	scanf("%s", nombreRestaurante);

	

	/*
	Cuando un Cliente hace un pedido (se verifica que el cliente esté registrado, si no lo está se le da de alta en ese
momento) se le pregunta por el nombre del restaurante, que alimentos solicita y Tipo de entrega (validar si el
restaurante la tiene). El operador de PediYa! informa al cliente el importe del pedido, (si el cliente tiene cupón de
descuento le aplica el 10% de correspondiente). Si el importe a pagar es mayor a $ 4000 se le asigna un cupón de
descuento. Una vez que se informó el importe de pedido, se le pregunta al cliente que Forma de pago elige.
Confirmado el pedido se debe informar al cliente el tiempo estimado de entrega.
	*/
}