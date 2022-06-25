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
			'temperatura': self.crearCampo(4, 'Temperatura'),
			'sensacion termica': self.crearCampo(5, 'Sensacion térmica'),
			'humedad': self.crearCampo(6, 'Humedad'),
		}

	def crearCampo(self, i, text):
		label = Label(self.__frame, text=text)
		label.grid(row=i, column=0, pady=5)

		entry = Entry(self.__frame, width=25)
		entry.grid(row=i, column=1, pady=5)

		return entry

	def clear(self):
		for campo in self.__campos:
			self.__campos[campo].delete(0, END)

	def setProvincia(self, provincia: Provincia):
		self.clear()
		self.__campos['nombre'].insert(0, provincia.getNombre())
