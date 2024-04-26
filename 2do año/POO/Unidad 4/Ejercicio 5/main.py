from src.VentanaPrincipal import VentanaPrincipal
from src.ManejadorPacientes import ManejadorPacientes
from os import path

if __name__ == '__main__':
	manejador = ManejadorPacientes(
		path.join(path.dirname(__file__), 'pacientes.json')
	)
	app = VentanaPrincipal(manejador)
	app.mainloop()