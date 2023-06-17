package ejercicio2;

public class Pareja implements IDeporte {

    private Deportista deportista1;
    private Deportista deportista2;

    public boolean conformar(List<Deportista> integrantes) {
        if (integrantes.size() != CANTIDAD_MINIMA) {
            return false;
        }
        this.deportista1 = integrantes.get(0);
        this.deportista2 = integrantes.get(1);
        return true;
    }

    public void mostrar() {
        System.out.println("Pareja: " + this.deportista1.getNombre() + " y " + this.deportista2.getNombre());
    }

    public void numeroDeportista() {
        System.out.println("Numero de deportista: " + this.deportista1.getNumeroJugador() + " y " + this.deportista2.getNumeroJugador());
    }
}
