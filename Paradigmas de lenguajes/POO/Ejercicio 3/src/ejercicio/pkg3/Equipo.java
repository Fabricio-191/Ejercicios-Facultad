package ejercicio.pkg3;

import java.util.List;

public class Equipo implements IDeporte {

    private String nombre;
    private List<Deportista> integrantes;

    public Equipo(String nombre) {
        this.nombre = nombre;
    }

    @Override
    public boolean conformar(List<Deportista> integrantes) {
        if (integrantes.size() < CANTIDAD_MINIMA) {
            return false;
        }

        this.integrantes = integrantes;
        return true;
    }

    @Override
    public void mostrar() {
        System.out.println("Equipo: " + this.nombre);
        for (Deportista deportista : this.integrantes) {
            System.out.println(deportista.getNombre());
        }
    }

    @Override
    public void numeroDeportista() {
        System.out.println("Numeros de deportistas del equipo " + this.nombre + ":");
        for (Deportista deportista : this.integrantes) {
            System.out.println(deportista.getNumeroJugador());
        }
    }
}
