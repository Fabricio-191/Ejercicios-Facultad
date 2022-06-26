from tkinter import Toplevel, Button, messagebox, LabelFrame, Frame, Label, Entry, Button, RIGHT, END
from .Provincia import Provincia
from .ManejadorProvincias import ManejadorProvincias

class VentanaNuevaProvincia(Toplevel):
	__campos = {}
	__callback = None
	__manejadorProvincias: ManejadorProvincias
	def __init__(self, parent, manejadorProvincias, callback):
		super().__init__(parent)
		self.__callback = callback
		self.__manejadorProvincias = manejadorProvincias

		self.__labelFrame = LabelFrame(self, text="Provincia", padx=10, pady=10)
		self.__labelFrame.pack(padx=10, pady=10)
		self.__frame = Frame(self.__labelFrame)
		self.__frame.pack()
		
		self.__campos = {
			'nombre': self.crearCampo(0, 'Nombre'),
			'capital': self.crearCampo(1, 'Capital'),
			'habitantes': self.crearCampo(2, 'Cantidad de habitantes'),
			'departamentos': self.crearCampo(3, 'Cantidad de departamentos/partidos'),
		}

		self.__botonConfirmar = Button(self, text="Confirmar", command=self.confirmar)
		self.__botonConfirmar.pack(pady=10)
	
	def crearCampo(self, i, text):
		label = Label(self.__frame, text=text)
		label.grid(row=i, column=0, pady=5)

		entry = Entry(self.__frame, width=25)
		entry.grid(row=i, column=1, pady=5)

		return entry

	def obtenerDatos(self):
		data = {}

		for campo in self.__campos:
			valor = self.__campos[campo].get()

			if valor == '':
				messagebox.showerror("Error", "Falta completar campo: {}".format(campo))
				return
		
			data[campo] = valor

		try:
			float(data['habitantes'])
		except:
			messagebox.showerror("Error", "Habitantes debe ser un numero")
	
		try:
			float(data['departamentos'])
		except:
			messagebox.showerror("Error", "Departamentos debe ser un numero")
		
		return data

	def confirmar(self):
		data = self.obtenerDatos()

		if data is None:
			return

		if self.__manejadorProvincias.yaExisteProvincia(data['nombre']):
			messagebox.showerror("Error", "Ya existe una provincia con ese nombre")
		elif not self.__manejadorProvincias.existeProvincia(data['nombre']):
			messagebox.showerror("Error", "No existe una provincia con ese nombre")
		else:
			provincia = Provincia(data)
			self.__callback(provincia) # type: ignore
			self.destroy()
		