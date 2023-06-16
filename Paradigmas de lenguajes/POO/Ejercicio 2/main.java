/*
Objetivo: Implementar una aplicación que use interface.
Descripción General

Un club deportivo ha organizado un campeonato de futsal y un campeonato de pin pon. Requiere de una aplicación que le permita administrar los datos de los deportistas inscriptos. Los datos de los inscriptos se han almacenado en archivos csv separados por coma, los de Futsal se han registrado en el archivo inscriptosFutbol.csv y los datos de los inscriptos para pin pon en el archivo inscriptosPinPon.csv. En ambos casos los datos registrados son nombre y DNI del deportista.

Los equipos de futsal tienen un nombre que los identifica, mientras que las parejas se identifican por los nombres de los deportistas que la conforman.

Tanto los equipos que participan en futsal como las parejas de pin pon se generan conforme el orden que se presenta en el archivo con los respectivos datos.

Le han solicitado al grupo de desarrollo donde usted trabaja una aplicación que genere automáticamente los equipos correspondientes. Además, la aplicación debe asignar un número a cada deportista que conforma el equipo (1…5) o pareja (1 y 2) según corresponda. Finalmente mostrar los datos (nombre y datos de cada deportista que lo integra) de los equipos y parejas conformados.

Descripción de los métodos de la clase Deporte.
• leerArchivo: Recibe como parámetro el nombre del archivo .csv que contiene los datos (nombre y DNI) de los deportistas. A partir de ellos crea las instancias correspondientes, las almacena en una lista y retorna dicha lista. (Se utiliza para los dos archivos)
• creaEquipos: Recibe como parámetro una lista con instancias de la clase Deportista y la cantidad de jugadores que conforman un equipo. De la lista toma la cantidad de jugadores para conformar un equipo, crea una instancia de Equipo y la almacena en una lista. Repite este proceso mientras haya jugadores para conformar un equipo. Retorna la lista con los equipos creados. Nota: Un jugador solo puede estar en un equipo.
• creaParejas: Recibe como parámetro una lista con instancias de la clase Deportista, de esta lista toma de a dos jugadores para conformar una pareja, crea una instancia de Pareja y la almacena en una lista. Repite este proceso mientras haya jugadores para conformar una pareja. Retorna la lista con las parejas creadas. Nota: Un jugador solo puede estar en una pareja.
• numerar: Numera cada integrante de un equipo o de una pareja.
• mostrar: Muestra los datos de cada equipo o de cada pareja.

Parte de algunos métodos ha sido implementado, usted deberá completarlo de forma tal que responda a los requerimientos del cliente y a lo propuesto por el equipo (se proporciona el archivo Deportes.java)
*/

import java.util.Scanner;

public class main {
    public static void main(String[] args) throws IOException {
        int cantidadJugadoresFutbol= 5;                  
    
        List<Deportista> datosFutbol= leerArchivo("./datos/inscriptosFutbol.csv");
        List<Deportista> datosPinPon= leerArchivo("./datos/inscriptosPinPon.csv");

		List<IDeporte> equiposFutbol = creaEquipos(datosFutbol, cantidadJugadoresFutbol);
		List<IDeporte> parejasPinPon = creaParejas(datosPinPon);

	}
}