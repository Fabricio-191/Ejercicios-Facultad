package javaapplication1;

import java.util.Scanner;

public class JavaApplication1 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.print("Ingrese la cantidad de viajeros: ");
        var gestor = new GestorViajeros(in.nextInt());

        JavaApplication1.menu();
        var opcion = in.nextInt();

        while (opcion != 0) {
            switch (opcion) {
                case 1: {
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
                    break;
                }

                case 2: {
                    System.out.print("Ingrese el DNI del viajero: ");
                    var viajero = gestor.getByDNI(in.next());
                    if (viajero != null) {
                        System.out.println(viajero.toString());
                    } else {
                        System.out.println("El viajero no se encontro");
                    }
                    break;
                }

                case 3: {
                    System.out.print("Ingrese el DNI del viajero: ");
                    var viajero = gestor.getByDNI(in.next());
                    if (viajero != null) {
                        System.out.println("El viajero tiene " + viajero.getMillas() + " millas");
                    } else {
                        System.out.println("El viajero no se encontro");
                    }
                    break;
                }

                case 4: {
                    System.out.print("Ingrese el DNI del viajero: ");
                    var viajero = gestor.getByDNI(in.next());
                    if(viajero == null){
                        System.out.println("El viajero no se encontro");
                    }else{
                        System.out.print("Ingrese las millas a agregar: ");
                        viajero.acumularMillas(in.nextInt());
                    }
                    
                    break;
                }

                case 5: {
                    System.out.print("Ingrese el DNI del viajero: ");
                    var viajero = gestor.getByDNI(in.next());
                    if(viajero == null){
                        System.out.println("El viajero no se encontro");
                    }else{
                        System.out.print("Ingrese las millas a agregar: ");
                        viajero.canjearMillas(in.nextInt());
                    }
                    
                    break;
                }

                case 6: {
                    // Mejor viajero: Mostrar los datos del/ los viajero/s con mayor cantidad de millas.
                    var mejorViajero = gestor.MejorViajero();
                    
                    if(mejorViajero == null){
                        System.out.print("No hay mejor viajero");
                    }else{
                        System.out.println(mejorViajero.toString());
                    }
                    
                    break;
                }

                default: {
                    System.out.println("Opcion invalida");
                }
            }

            opcion = in.nextInt();
        }
    }

    private static void menu() {
        System.out.println("Opciones:");
        System.out.println("0. Salir");
        System.out.println("1. Registrar un nuevo viajero");
        System.out.println("2. Mostrar datos de viajero");
        System.out.println("3. Cantidad de millas de un viajero");
        System.out.println("4. Añadir millas a un viajero");
        System.out.println("5. Canjear millas a un viajero");
        System.out.println("6. Mostrar el viajero e mas millas");
    }
}

/*
5
1
1
123
a
b
3000
*/