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

from GestorCamas import GestorCamas
from os import path

if __name__ == "__main__":
	gestor = GestorCamas(path.dirname(__file__) + "/camas.csv", path.dirname(__file__) + "/medicamentos.csv")
	
	gestor.listarDatosYMedicamentos(input('NyA del paciente: '))
	gestor.listarPorDiagnostico(input('Diagnóstico: '))