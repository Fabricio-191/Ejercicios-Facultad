package ejercicio4;

public class ViajeroFrecuente {

    private Integer num;
    private String dni;
    private String nombre;
    private String apellido;
    private Integer millas;

    public ViajeroFrecuente(Integer num, String dni, String nombre, String apellido, Integer millas) {
        this.num = num;
        this.dni = dni;
        this.nombre = nombre;
        this.apellido = apellido;
        this.millas = millas;
    }

    public Integer cantidadTotalMillas() {
        return this.millas;
    }

    public Integer acumularMillas(Integer a) {
        this.millas += a;
        return this.millas;
    }

    public Integer canjearMillas(Integer a) {
        if (this.millas < a) {
            System.out.println("No hay suficientes millas");
            return -1;
        } else {
            this.millas -= a;
            return this.millas;
        }
    }

    public Integer getNum() {
        return this.num;
    }

    public String getDNI() {
        return this.dni;
    }

    public Integer getMillas() {
        return this.millas;
    }

    @Override
    public String toString() {
        return "ID: " + this.num + "\n"
                + "DNI: " + this.dni + "\n"
                + "NyA: " + this.nombre + " " + this.apellido + "\n"
                + "Millas: " + this.millas + "\n";
    }
}
