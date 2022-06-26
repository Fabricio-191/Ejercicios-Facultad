from tkinter import ttk, messagebox, Tk, StringVar, W, E, Label, Button
import requests
from threading import Timer


class Aplicacion(Tk):
	__precioArs: StringVar
	__precioDls: StringVar
	__dolaresAPesos: float

	def __init__(self):
		super().__init__()
		self.title("Conversor de moneda")
		self.resizable = (0, 0)

		self.__precioArs = StringVar()
		self.__precioDls = StringVar()
		self.__precioDls.trace('w', self.calcular)

		self.precioEntry = ttk.Entry(self, width=15, textvariable=self.__precioDls)
		self.precioEntry.grid(column=2, row=1, sticky=(W, E)) # type: ignore
		self.precioEntry.focus()

		Label(self, textvariable=self.__precioArs).grid(column=2, row=2, sticky=(W, E)) # type: ignore
		
		Button(self, text='Salir', padx=10, pady=5, command=self.destroy).grid(column=3, row=3, sticky=W)
		
		Label(self, text="dolares").grid(column=3, row=1, sticky=W)
		
		Label(self, text="es equivalente a").grid(column=1, row=2, sticky=E)
		
		Label(self, text="pesos").grid(column=3, row=2, sticky=W)
		
		for child in self.winfo_children():
			child.grid_configure(padx=5, pady=5)

		self.actualizarPrecioDolar()

	def actualizarPrecioDolar(self):
		response = requests.get('https://www.dolarsi.com/api/api.php?type=dolar')
		data = response.json()
		
		i = 0
		band = False
		while not band and i < len(data):
			if data[i]['casa']['nombre'] == 'Oficial':
				band = True
				self.__dolaresAPesos = float(data[i]['casa']['venta'].replace(',', '.'))
			
			i += 1

		Timer(60, self.actualizarPrecioDolar).start()

	def calcular(self, *args):
		if self.precioEntry.get() == '':
			self.__precioArs.set('')
		else:
			try:
				valor = float(self.precioEntry.get())
				self.__precioArs.set('{:.2f}'.format(valor * self.__dolaresAPesos))
			except ValueError:
				messagebox.showerror('Error de tipo', 'Debe ingresar un valor numérico')
				self.__precioDls.set('')
				self.precioEntry.focus()

if __name__ == '__main__':
	app = Aplicacion()
	app.mainloop()