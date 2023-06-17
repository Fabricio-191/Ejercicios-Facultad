package ejercicio3;

public class Deportista {

    private static Integer count = 1;
    private final String dni;
    private final String nombre;
    private final Integer numeroJugador;

    public Deportista(String dni, String nombre) {
        this.dni = dni;
        this.nombre = nombre;
        this.numeroJugador = Deportista.count++;
    }

    public String getDni() {
        return this.dni;
    }

    public String getNombre() {
        return this.nombre;
    }

    public Integer getNumeroJugador() {
        return this.numeroJugador;
    }
}
