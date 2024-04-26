/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ejercicio.pkg4;

import java.util.Scanner;
import java.util.List;

public class Ejercicio4 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        var gestor = new GestorViajeros();

        System.out.println("Opciones:");
        System.out.println("0. Salir");
        System.out.println("1. Registrar un nuevo viajero");
        System.out.println("2. Mostrar datos de viajero (ordenados por millas)");
        System.out.println("3. Mostrar nombres de viajeros con mas de 200 millas");
        System.out.println("4. Obtener viajero con mas millas");

        var opcion = in.nextInt();

        while (opcion != 0) {
            switch (opcion) {
                case 1 -> {
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

                case 2 -> {
                    List<ViajeroFrecuente> viajeros = gestor.ordenadosPorMillas();

                    System.out.println("Viajeros ordenados por millas:");
                    for (ViajeroFrecuente viajero : viajeros) {
                        System.out.println(viajero.toString());
                    }
                }

                case 3 -> {
                    List<String> nombres = gestor.nombresConMasDe200Millas();

                    System.out.println("Nombres de viajeros con mas de 200 millas:");
                    for (String nombre : nombres) {
                        System.out.println(nombre);
                    }
                }

                case 4 -> {
                    ViajeroFrecuente viajero = gestor.getViajeroConMasMillas();

                    System.out.println("Viajero con mas millas:");
                    System.out.println(viajero.toString());
                }

                default -> {
                    System.out.println("Opcion invalida");
                }
            }

            System.out.println("Opciones:");
            System.out.println("0. Salir");
            System.out.println("1. Registrar un nuevo viajero");
            System.out.println("2. Mostrar datos de viajero (ordenados por millas)");
            System.out.println("3. Mostrar nombres de viajeros con mas de 200 millas");
            System.out.println("4. Obtener viajero con mas millas");
            opcion = in.nextInt();
        }

        in.close();
    }
}
