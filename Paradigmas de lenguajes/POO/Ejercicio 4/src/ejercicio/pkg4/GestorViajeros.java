package ejercicio.pkg4;

import java.util.List;
import java.util.ArrayList;

public class GestorViajeros {
	private List<ViajeroFrecuente> viajeros = new ArrayList<ViajeroFrecuente>();

	public GestorViajeros() { }
	public GestorViajeros(List<ViajeroFrecuente> viajeros) {
		this.viajeros = viajeros;
	}

	public void agregar(ViajeroFrecuente viajero) {
		this.viajeros.add(viajero);
	}

	public List<ViajeroFrecuente> ordenadosPorMillas() {
		return this.viajeros.stream()
			.sorted((v1, v2) -> v1.getMillas() - v2.getMillas())
			.toList();
	}

	public List<String> nombresConMasDe200Millas() {
		return this.viajeros.stream()
			.filter(v -> v.getMillas() > 200)
			.map(ViajeroFrecuente::getNombre).toList();
	}

	public ViajeroFrecuente getViajeroConMasMillas() {
		if(this.viajeros.size() == 0) return null;
		else return this.viajeros.stream()
			.max((v1, v2) -> v1.getMillas() - v2.getMillas())
			.get();
	}
}
