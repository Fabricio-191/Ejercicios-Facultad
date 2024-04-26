"""
La aplicación creada deberá:

1) Leer  los  datos  de  cada  cama,  leyendo  los  datos  desde  el  archivo  “camas.csv”, generando  unmanejador  de  camas,  utilice  la  colección  arreglo  para  almacenar  los objetos instancia de la clase cama Cama.

2) Leer los datos de los medicamentos utilizados en cada cama, leyendo los datos desde el archivo “medicamentos.csv”, generandoun manejador que utiliceuna colección del tipo lista en la que se almacenen objetosinstancia de la claseMedicamento.

3) Dado un el nombre y apellido de un paciente internado al que se le da el alta, listar los datos  del  paciente  y  los  medicamentos  que  deberá  devolver,  indicando  el  precio  de cada  medicamento  y  el  total  que  deberá  abonar  en  caso  de no devolverlos, con el siguiente formato:

Paciente: xxxxxxxxxxxxx, xxxxxx   Cama: xxxxx    Habitación: xxx
Diagnóstico: xxxxxxxxxxx    Fecha de internación: dd/mm/aaaa
Fecha de Alta: dd/mm/aaaa

Medicamento/monodroga           Presentacion          Cantidad    Precio
xxxxxxxxxxxxxxxxxxxxx           xxxxxxxxxxxxxxxxxx   xxxxxxxxxxxx  xxxxxxx.xxx
xxxxxxxxxxxxxxxxxxxxx           xxxxxxxxxxxxxxxxxx   xxxxxxxxxxxx  xxxxxxx.xxx
xxxxxxxxxxxxxxxxxxxxx           xxxxxxxxxxxxxxxxxx   xxxxxxxxxxxx  xxxxxxx.xxx
xxxxxxxxxxxxxxxxxxxxx           xxxxxxxxxxxxxxxxxx   xxxxxxxxxxxx  xxxxxxx.xxx

Total adeudado: xxxx.xx

4) Listar  los  datos  de  pacientes  internados  (cama  ocupada),  que  tienen  un  diagnóstico leído desde teclado.
"""

from Cama import Cama
from Medicamento import Medicamento
from GestorMedicamentos import GestorMedicamentos

from GestorCamas import GestorCamas
from os import path

def test():
	cama = Cama(4, 1, True, "Juan Leandro", "Cancer", "01/01/2020", "03/03/2020")

	assert cama.obtenerDiagnostico() == "Cancer"
	assert cama.obtenerFechaInternacion() == "01/01/2020"
	assert cama.obtenerHabitacion() == 1
	assert cama.obtenerID() == 4
	assert cama.obtenerNyA() == "Juan Leandro"

	medicamento = Medicamento(1, 10, "a", "Paracetamol", "Tableta", 12, 155)

	assert medicamento.getCantidadAplicada() == 12
	assert medicamento.getIdCama() == 1
	assert medicamento.getMonodroga() == "Paracetamol"
	assert medicamento.getPrecio() == 155
	assert medicamento.getPresentacion() == "Tableta"
	assert medicamento.getNombreComercial() == "a"

	camas = GestorCamas(
		path.dirname(__file__) + "/camas.csv",
		path.dirname(__file__) + "/medicamentos.csv"
	)

	assert camas.obtenerPaciente("Perez, Luis").obtenerNyA() == "Perez, Luis" # type: ignore

	GestorMedicamentos(path.dirname(__file__) + "/medicamentos.csv")

if __name__ == "__main__":
	test()
	gestor = GestorCamas(path.dirname(__file__) + "/camas.csv", path.dirname(__file__) + "/medicamentos.csv")
	
	gestor.listarDatosYMedicamentos(input('NyA del paciente: '))
	gestor.listarPorDiagnostico(input('Diagnóstico: '))