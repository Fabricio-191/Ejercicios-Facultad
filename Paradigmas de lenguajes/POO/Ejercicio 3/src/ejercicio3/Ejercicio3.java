package ejercicio3;

import java.util.*;
import java.io.*;

public class Ejercicio3 {

    public static final String SEPARADOR = ",";

    public static List<Deportista> leerArchivo(String nombreArchivo) throws IOException {
        BufferedReader bufferLectura = null;
        List<Deportista> datos = new ArrayList<>();

        try {
            bufferLectura = new BufferedReader(new FileReader(nombreArchivo));
            String linea;

            while ((linea = bufferLectura.readLine()) != null) {
                // Sepapar la linea leída con el separador definido previamente
                String[] campos = linea.split(SEPARADOR);
                Deportista d = new Deportista(campos[0], campos[1]);
                datos.add(d);
            }
        } catch (IOException e) {
            System.out.println(e.getMessage());
        } finally {
            // Cierro el buffer de lectura
            if (bufferLectura != null) bufferLectura.close();
        }

        return datos;
    }

    /**
     * Crea los equipos con los datos pasados como parámetro
     *
     * @param datos lista con todos los deportistas inscriptos
     * @param cantidadJugadores cantidad de jugadores que conforman un equipo
     * @return una lista de equipos
     */
    public static List<IDeporte> creaEquipos(List<Deportista> datos, int cantidadJugadores) {
		List<IDeporte> equipos = new ArrayList<>();
		int i = 0;

		while (i < datos.size()) {
			Equipo e = new Equipo("Equipo " + i);
			e.conformar(datos.subList(i, i + cantidadJugadores));
			equipos.add(e);
			i += cantidadJugadores;
		}

		return equipos;
    }

    /**
     * Crea los equipos con los datos pasados como parámetro
     *
     * @param datos es una lista con todos los deportitas inscriptos
     * @return una lista de Parejas formadas
     */
    public static List<IDeporte> creaParejas(List<Deportista> datos) {
		List<IDeporte> parejas = new ArrayList<>();
		int i = 0;

		while (i < datos.size()) {
			Pareja p = new Pareja();
			p.conformar(datos.subList(i, i + 2));
			parejas.add(p);
			i += 2;
		}

		return parejas;
	}

    /**
     * Numera cada integrante del equipo o de la pareja
     *
     * @param datos
     */
    public static void numerar(List<IDeporte> datos) {
		for(IDeporte d : datos) d.numeroDeportista();
    }

    /**
     * Muestra los datos de cada equipo o de cada pareja
     *
     * @param datos
     */
    public static void mostrar(List<IDeporte> datos) {
		for(IDeporte d : datos) d.mostrar();
    }
	
    public static void main(String[] args) throws IOException {
        int cantidadJugadoresFutbol = 5;

        List<Deportista> datosFutbol = leerArchivo("E:\\Programacion\\Ejercicios-Facultad\\Paradigmas de lenguajes\\POO\\Ejercicio 2\\src\\ejercicio3\\datos\\inscriptosFutbol.csv");
        List<Deportista> datosPinPon = leerArchivo("E:\\Programacion\\Ejercicios-Facultad\\Paradigmas de lenguajes\\POO\\Ejercicio 2\\src\\ejercicio3\\datos\\inscriptosPinPon.csv");

        List<IDeporte> equiposFutbol = creaEquipos(datosFutbol, cantidadJugadoresFutbol);
        List<IDeporte> parejasPinPon = creaParejas(datosPinPon);
		
		numerar(equiposFutbol);
		numerar(parejasPinPon);

		mostrar(equiposFutbol);
		mostrar(parejasPinPon);
    }
}
