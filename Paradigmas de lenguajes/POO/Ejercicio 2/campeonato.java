/*
Campeonato

+ SEPARADOR = ","

+ leerArchivo(String nomArcivo): List<Deportista>
+ creaEquipos(List<Deportista> datos, int cantJugadores): List<IDeporte>
+ creaParejas(List<Deportista> datos): List<IDeporte>
+ numerar(List<Deportista> datos): void
+ mostrar(List<Deportista> deportes): void

*/

import java.util.*;
public class Campeonato {
    public static final String SEPARADOR = ",";
	
    public static List<Deportista>leerArchivo(String nombreArchivo)throws IOException{
        BufferedReader bufferLectura = null;
        List<Deportista> datos = new ArrayList<>();
        try {
            bufferLectura = new BufferedReader(new FileReader(nombreArchivo));
            String linea;                  

            while ((linea=bufferLectura.readLine()) != null) {
             // Sepapar la linea leída con el separador definido previamente
             String[] campos = linea.split(SEPARADOR); 
             Deportista d = new Deportista(campos[0],campos[1]);
             datos.add(d);           
            }
        } 
        catch (IOException e) {
            System.out.println(e.getMessage());
        }
        finally {
         // Cierro el buffer de lectura
         if (bufferLectura != null) {
             bufferLectura.close();
         }
        }
        return datos;
    }
	
    /**
     * Crea los equipos con los datos pasados como parámetro
     * @param datos lista con todos los deportistas inscriptos
     * @param cantidadJugadores cantidad de jugadores que conforman un equipo
     * @return una lista de equipos
     */
    public static List<IDeporte> creaEquipos(List<Deportista> datos, int cantidadJugadores){
		
    }

    /**
     * Crea los equipos con los datos pasados como parámetro
     * @param datos es una lista con todos los deportitas inscriptos
     * @return una lista de Parejas formadas
     */
    public static List<IDeporte> creaParejas(List<Deportista> datos){
        
    }

    /**
     * Numera cada integrante del equipo o de la pareja
     * @param datos 
     */
    public static void numerar(List<IDeporte> datos){
         
    }
	
    /**
     * Muestra los datos de cada equipo o de cada pareja
     * @param datos
     */
    public static void mostrar(List<IDeporte> datos){
          
    }      
}
