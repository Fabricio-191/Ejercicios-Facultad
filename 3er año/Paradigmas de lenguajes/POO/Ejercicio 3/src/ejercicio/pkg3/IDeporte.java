package ejercicio.pkg3;

import java.util.List;

public interface IDeporte {

    int CANTIDAD_MINIMA = 2;

    boolean conformar(List<Deportista> integrantes);

    void mostrar();

    void numeroDeportista();
}
