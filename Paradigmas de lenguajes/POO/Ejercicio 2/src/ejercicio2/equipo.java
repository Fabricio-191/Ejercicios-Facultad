package ejercicio2;

public class Equipo implements IDeporte {

    private String nombre;
    private List<Deportista> integrantes;

    public Equipo(String nombre) {
        this.nombre = nombre;
    }

    public boolean conformar(List<Deportista> integrantes) {
        if (integrantes.size() < CANTIDAD_MINIMA) {
            return false;
        }

        this.integrantes = integrantes;
        return true;
    }

    public void mostrar() {
        System.out.println("Equipo: " + this.nombre);
        for (Deportista deportista : this.integrantes) {
            System.out.println(deportista.getNombre());
        }
    }

    public void numeroDeportista() {
        System.out.println("Numeros de deportistas del equipo " + this.nombre + ":");
        for (Deportista deportista : this.integrantes) {
            System.out.println(deportista.getNumeroJugador());
        }
    }
}
