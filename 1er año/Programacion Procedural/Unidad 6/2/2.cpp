#include <stdio.h>
#include <malloc.h>
#include <string.h>

struct alumno{
	struct alumno* next;
	char* nombre;
	int registro;
	char resultado;
};
	
char* leerString(FILE* archivo){
	char str[200];
 	fgets(str, 200, archivo);

	int len = strlen(str);
	str[len - 1] = '\0';

	char* string = (char*) malloc(sizeof(char) * len);
	strcpy(string, str); 

	return string;
}

void generarArchivo(char* nombreArchivo){
	FILE* archivo = fopen(nombreArchivo, "w");
	
	printf("Introduzca el nombre del alumno: ");
	char* str = leerString(stdin);
	while(stricmp(str, "fin") != 0){
		fprintf(archivo, "%s\n", str);
		
		printf("Introduzca el registro del alumno: ");
		fprintf(archivo, "%s\n", leerString(stdin));
		printf("Introduzca el resultado del alumno: ");
		fprintf(archivo, "%s\n\n", leerString(stdin));

		printf("\nIntroduzca el nombre del alumno: ");
		str = leerString(stdin);
	}

	fclose(archivo);
}

alumno* leerAlumnos(FILE* archivo){
	if(feof(archivo)) return NULL;

	alumno* alu = (alumno*) malloc(sizeof(alumno));

	alu->nombre = leerString(archivo);
	fscanf(archivo, "%d\n%c\n\n", &alu->registro, &alu->resultado);

	alu->next = leerAlumnos(archivo);

	return alu;
}

alumno* leerArchivo(char* filename, char* materia){
	FILE* archivo = fopen(filename, "r");
	if(archivo == NULL){
		printf("No se pudo abrir el archivo \"%s\"", filename);
		return NULL;
	}

	if(feof(archivo)) return NULL;
	alumno* cabeza = leerAlumnos(archivo);
	fclose(archivo);

	alumno* temp = cabeza;

	printf("\n%s:\n", materia);
	while(temp != NULL){
		printf("  %s	%d	%c\n", temp->nombre, temp->registro, temp->resultado);
		temp = temp->next;
	}

	return cabeza;
}

bool encontrarAprobo(alumno* nodo, int registro){
	while(nodo != NULL){
		if(
			nodo->registro == registro &&
			nodo->resultado == 'A'
		) return true;

		nodo = nodo->next;
	}

	return false;
}

void ambasMaterias(alumno* prog, alumno* alge){
	printf("\nAlumnos que aprobaron ambas materias:\n");
	while(prog != NULL){
		if(prog->resultado == 'A' && encontrarAprobo(alge, prog->registro)){
			printf("  %s	%d\n", prog->nombre, prog->registro);
		}

		prog = prog->next;
	}
}

int main(){
	generarArchivo("alumnosPP.dat");
	generarArchivo("alumnosAL.dat");
	alumno* prog = leerArchivo("alumnosPP.dat", "Programacion Procedural");
	alumno* alge = leerArchivo("alumnosAL.dat", "Algebra Lineal");

	ambasMaterias(prog, alge);
	return 0;
}

/*
Calivar, A
20892
A
Alicia Sotelo
20717
A
Fuente, M
20335
A
Fernandez, M
20332
R
Axel Montero
20183
A
Funes, G
20148
R
Castro, L
20128
A
Gonzalez, S
20096
R
Fin
Calivar, A
20892
A
Alicia Sotelo
20717
R
Gamboa, M
20588
A
Juan Torres
20369
A
Fuente, M
20335
A
Aballay, G
20254
R
Axel Montero
20183
A
Funes, G
20148
R
Castro, L
20128
A
Fin

*/