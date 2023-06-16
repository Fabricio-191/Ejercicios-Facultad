public interface IDeporte {
	int CANTIDAD_MINIMA = 2;
	boolean conformar(List<Deportista> integrantes);
	void mostrar();
	void numeroDeportista();
}