#pragma once
struct empresa {
	empresa* next;
	int cod;
	char *CUIT, *nombre, *direccion;
};

struct empleado {
	empleado* next;
	char* nombre, *DNI;
	int codEmpresa, antiguedad;
	float sueldo;
};

int generarArchivoEmpresas();
void generarArchivoEmpleados(int cantEmpresas);

empresa* leerEmpresa(FILE* archivo);
empleado* leerEmpleado(FILE* archivo);
void emitirListado(empresa* empresa, empleado* empleado);
void liberar(empresa* empresas, empleado* empleados);