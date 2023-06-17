/*
Ejercicio 1: Viajeros
Objetivos:
- Repasar conceptos del paradigma orientado a objetos
- Conocer el lenguaje y el entorno de desarrollos implementando una aplicación sencilla.
Descripción General: En una aerolínea ofrece una promoción a sus viajeros frecuentes que consiste en acumular millas por los viajes que realizan, pudiendo luego recibir beneficios a través del canje de millas.
Usted trabaja en el área de sistemas de la aerolínea y le han solicitado la implementación de un sistema capaz de gestionar la promoción. Respetando el siguiente diseño de clase:

1. Las clases dadas en el diagrama. La clase gestor se basa en un arreglo.
2. Un programa que presente un menú con las siguientes funcionalidades:
 */


package ejercicio1;

import java.util.Scanner;

public class Ejercicio1 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.print("Ingrese la cantidad de viajeros: ");
        var gestor = new GestorViajeros(in.nextInt());

		System.out.println("Opciones:");
		System.out.println("0. Salir");
		System.out.println("1. Registrar un nuevo viajero");
		System.out.println("2. Mostrar datos de viajero");
		System.out.println("3. Cantidad de millas de un viajero");
		System.out.println("4. Añadir millas a un viajero");
		System.out.println("5. Canjear millas a un viajero");
		System.out.println("6. Mostrar el viajero e mas millas");
      	var opcion = in.nextInt();

        while (opcion != 0) {
            switch (opcion) {
                case 1 ->  {
                    System.out.print("Ingrese el ID del viajero: ");
                    var ID = in.nextInt();
                    System.out.print("Ingrese el DNI del viajero: ");
                    var DNI = in.next();
                    System.out.print("Ingrese el nombre del viajero: ");
                    var nombre = in.next();
                    System.out.print("Ingrese el apellido del viajero: ");
                    var apellido = in.next();
                    System.out.print("Ingrese el millas del viajero: ");
                    var millas = in.nextInt();

                    var viajero = new ViajeroFrecuente(ID, DNI, nombre, apellido, millas);
                    gestor.agregar(viajero);
                }

                case 2 ->  {
                    System.out.print("Ingrese el DNI del viajero: ");
                    var viajero = gestor.getByDNI(in.next());
                    if (viajero != null) {
                        System.out.println(viajero.toString());
                    } else {
                        System.out.println("El viajero no se encontro");
                    }
                }

                case 3 ->  {
                    System.out.print("Ingrese el DNI del viajero: ");
                    var viajero = gestor.getByDNI(in.next());
                    if (viajero != null) {
                        System.out.println("El viajero tiene " + viajero.getMillas() + " millas");
                    } else {
                        System.out.println("El viajero no se encontro");
                    }
                }

                case 4 ->  {
                    System.out.print("Ingrese el DNI del viajero: ");
                    var viajero = gestor.getByDNI(in.next());
                    if(viajero == null){
                        System.out.println("El viajero no se encontro");
                    }else{
                        System.out.print("Ingrese las millas a agregar: ");
                        viajero.acumularMillas(in.nextInt());
                    }
                    
                }

                case 5 ->  {
                    System.out.print("Ingrese el DNI del viajero: ");
                    var viajero = gestor.getByDNI(in.next());
                    if(viajero == null){
                        System.out.println("El viajero no se encontro");
                    }else{
                        System.out.print("Ingrese las millas a canjear: ");
                        viajero.canjearMillas(in.nextInt());
                    }
                    
                }

                case 6 ->  {
                    // Mejor viajero: Mostrar los datos del/ los viajero/s con mayor cantidad de millas.
                    var mejorViajero = gestor.mejorViajero();
                    
                    if(mejorViajero == null){
                        System.out.print("No hay mejor viajero");
                    }else{
                        System.out.println(mejorViajero.toString());
                    }
                    
                }

                default -> {
                    System.out.println("Opcion invalida");
                }
            }
			
			System.out.println("Opciones:");
			System.out.println("0. Salir");
			System.out.println("1. Registrar un nuevo viajero");
			System.out.println("2. Mostrar datos de viajero");
			System.out.println("3. Cantidad de millas de un viajero");
			System.out.println("4. Añadir millas a un viajero");
			System.out.println("5. Canjear millas a un viajero");
			System.out.println("6. Mostrar el viajero e mas millas");
      		opcion = in.nextInt();
        }
    }
}
