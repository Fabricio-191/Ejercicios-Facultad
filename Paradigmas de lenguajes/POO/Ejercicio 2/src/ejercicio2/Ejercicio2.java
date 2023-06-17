
/*
Los datos de los inscriptos se han almacenado en archivos csv separados por coma, los de Futsal se han registrado en el archivo inscriptosFutbol.csv y los datos de los inscriptos para pin pon en el archivo inscriptosPinPon.csv. En ambos casos los datos registrados son nombre y DNI del deportista.

Los equipos de futsal tienen un nombre que los identifica, mientras que las parejas se identifican por los nombres de los deportistas que la conforman.

Tanto los equipos que participan en futsal como las parejas de pin pon se generan conforme el orden que se presenta en el archivo con los respectivos datos.

Le han solicitado al grupo de desarrollo donde usted trabaja una aplicación que genere automáticamente los equipos correspondientes. Además, la aplicación debe asignar un número a cada deportista que conforma el equipo (1…5) o pareja (1 y 2) según corresponda.

Finalmente mostrar los datos (nombre y datos de cada deportista que lo integra) de los equipos y parejas conformados.


 */
package ejercicio2;

import java.util.Scanner;
import java.io.IOException;

public class Ejercicio2 {

    public static void main(String[] args) throws IOException {
        int cantidadJugadoresFutbol = 5;

        List<Deportista> datosFutbol = leerArchivo("./datos/inscriptosFutbol.csv");
        List<Deportista> datosPinPon = leerArchivo("./datos/inscriptosPinPon.csv");

        List<IDeporte> equiposFutbol = creaEquipos(datosFutbol, cantidadJugadoresFutbol);
        List<IDeporte> parejasPinPon = creaParejas(datosPinPon);

    }
}
