from src.VentanaPrincipal import VentanaPrincipal
from src.ManejadorProvincias import ManejadorProvincias
from os import path

if __name__ == '__main__':
	manejador = ManejadorProvincias(
		path.join(path.dirname(__file__), 'datos.json')
	)
	app = VentanaPrincipal(manejador)
	app.mainloop()