/*

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