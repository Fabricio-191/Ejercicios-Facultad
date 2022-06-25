from tkinter import Toplevel, Button
from .Provincia import Provincia

from tkinter import messagebox, LabelFrame, Frame, Label, Entry, Button, RIGHT, END
from .Provincia import Provincia

class FormDatosProvincia(LabelFrame):
	__campos = {}
	def __init__(self, master, **kwargs):
		super().__init__(master, text="Provincia", padx=10, pady=10, **kwargs)
		self.__frame = Frame(self)
		self.__frame.pack()

		self.__campos = {
			'nombre': self.crearCampo(0, 'Nombre'),
			'capital': self.crearCampo(1, 'Capital'),
			'habitantes': self.crearCampo(2, 'Cantidad de habitantes'),
			'departamentos': self.crearCampo(3, 'Cantidad de departamentos/partidos'),
		}

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

class VentanaNuevaProvincia(Toplevel):
	__callback = None
	def __init__(self, parent, callback):
		super().__init__(parent)

		self.__callback = callback
		self.__form = FormDatosProvincia(self)
		self.__form.pack(padx=10, pady=10)

		self.__botonConfirmar = Button(self, text="Confirmar", command=self.confirmar)
		self.__botonConfirmar.pack(pady=10)

	def confirmar(self):
		data = self.__form.obtenerDatos()
		
		if data is not None:
			provincia = Provincia(data)
			self.__callback(provincia) # type: ignore
			self.destroy()
	