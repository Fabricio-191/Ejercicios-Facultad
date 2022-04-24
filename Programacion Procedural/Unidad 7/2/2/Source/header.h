#pragma once
struct restaurante {
	char nombre[50], direccion[50], telefono[30];
	int ID, pedidos, tipoEntrega, medioPago;
	float montoAcumulado;
};

struct cliente {
	char nombre[50], direccion[50], telefono[30];
	int ID, cupon;
};

struct empleado {
	char nombre[50], direccion[50], telefono[30], DNI[15];
};

struct pedido {
	int IDcliente, IDrestaurante, IDempleado, medioPago, tipoEntrega;
	float importe, tiempoEntrega;
	char alimentosSolicitados[200];
};

void leerString(char* string, int limit, FILE* archivo);
int estaRegistrado(char* nombre);
int leerRestaurantes(restaurante* &res);
void agregarRestaurante(restaurante* &res, int &cant);
void eliminarRestaurante(restaurante* &res, int &cant);
void agregarCliente(char* nombre);