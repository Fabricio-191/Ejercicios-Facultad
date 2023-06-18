package ejercicio.pkg1;

public class GestorViajeros {

    private Integer index;
    private ViajeroFrecuente[] viajeros;

    public GestorViajeros(Integer cant) {
        this.index = 0;
        this.viajeros = new ViajeroFrecuente[cant];
    }

    public void agregar(ViajeroFrecuente viajero) {
        this.viajeros[this.index] = viajero;
        this.index++;
    }

    public ViajeroFrecuente getByDNI(String dni) {
        for (int i = 0; i < this.index; i++) {
            if (this.viajeros[i].getDNI().equals(dni)) {
                return this.viajeros[i];
            }
        }

        return null;
    }

    public ViajeroFrecuente mejorViajero() {
        if (this.index == 0) {
            return null;
        }

        var max = this.viajeros[0];
        for (Integer i = 1; i < this.index; i++) {
            if (this.viajeros[i].getMillas() > max.getMillas()) {
                max = this.viajeros[i];
            }
        }

        return max;
    }
}
