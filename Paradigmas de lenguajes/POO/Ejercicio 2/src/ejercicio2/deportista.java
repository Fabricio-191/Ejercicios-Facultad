// class deportista

public class Deportista {
    private String dni;
    private String nombre;
    private Integer numeroJugador;

	public Deportista(String dni, String nombre, Integer numeroJugador) {
		this.dni = dni;
		this.nombre = nombre;
		this.numeroJugador = numeroJugador;
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