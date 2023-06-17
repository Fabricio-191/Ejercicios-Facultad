/*
Campeonato

+ SEPARADOR = ","

+ leerArchivo(String nomArcivo): List<Deportista>
+ creaEquipos(List<Deportista> datos, int cantJugadores): List<IDeporte>
+ creaParejas(List<Deportista> datos): List<IDeporte>
+ numerar(List<Deportista> datos): void
+ mostrar(List<Deportista> deportes): void


• leerArchivo: Recibe como parámetro el nombre del archivo .csv que contiene los datos (nombre y DNI) de los deportistas. A partir de ellos crea las instancias correspondientes, las almacena en una lista y retorna dicha lista. (Se utiliza para los dos archivos)
• creaEquipos: Recibe como parámetro una lista con instancias de la clase Deportista y la cantidad de jugadores que conforman un equipo. De la lista toma la cantidad de jugadores para conformar un equipo, crea una instancia de Equipo y la almacena en una lista. Repite este proceso mientras haya jugadores para conformar un equipo. Retorna la lista con los equipos creados. Nota: Un jugador solo puede estar en un equipo.
• creaParejas: Recibe como parámetro una lista con instancias de la clase Deportista, de esta lista toma de a dos jugadores para conformar una pareja, crea una instancia de Pareja y la almacena en una lista. Repite este proceso mientras haya jugadores para conformar una pareja. Retorna la lista con las parejas creadas. Nota: Un jugador solo puede estar en una pareja.
• numerar: Numera cada integrante de un equipo o de una pareja.
• mostrar: Muestra los datos de cada equipo o de cada pareja.
 */

import java.util.*;
import java.io.*;

public class Campeonato {

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

    }

    /**
     * Crea los equipos con los datos pasados como parámetro
     *
     * @param datos es una lista con todos los deportitas inscriptos
     * @return una lista de Parejas formadas
     */
    public static List<IDeporte> creaParejas(List<Deportista> datos) {

    }

    /**
     * Numera cada integrante del equipo o de la pareja
     *
     * @param datos
     */
    public static void numerar(List<IDeporte> datos) {

    }

    /**
     * Muestra los datos de cada equipo o de cada pareja
     *
     * @param datos
     */
    public static void mostrar(List<IDeporte> datos) {

    }
}
