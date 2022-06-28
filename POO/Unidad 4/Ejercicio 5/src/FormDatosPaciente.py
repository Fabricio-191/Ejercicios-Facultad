from tkinter import messagebox, LabelFrame, Frame, Label, Entry, Button, RIGHT, END
from .Paciente import Paciente

class FormDatosPaciente(LabelFrame):
	__campos = {}
	def __init__(self, master, **kwargs):
		super().__init__(master, text="Paciente", padx=10, pady=10, **kwargs)
		self.__frame = Frame(self)
		self.__frame.pack()

		self.__campos = {
			'nombre': self.crearCampo(0, 'Nombre'),
			'apellido': self.crearCampo(1, 'Apellido'),
			'telefono': self.crearCampo(2, 'Telefono'),
			'altura': self.crearCampo(3, 'Altura'),
			'peso': self.crearCampo(4, 'Peso')
		}

	def crearCampo(self, i, text):
		label = Label(self.__frame, text=text)
		entry = Entry(self.__frame, width=25)
		label.grid(row=i, column=0, pady=5)
		entry.grid(row=i, column=1, pady=5)

		return entry
	
	def obtenerDatos(self):
		data = {}

		campos = list(self.__campos.keys())
		i = 0
		band = False

		while i < len(campos) and not band:
			if self.__campos[campos[i]].get() == '':
				band = True
				messagebox.showerror("Error", "Faltan datos en el campo {}".format(campos[i]))
			else:
				data[campos[i]] = self.__campos[campos[i]].get()
			i += 1

		valor = None
		if not band:
			try:
				float(data['altura'])
			except:
				messagebox.showerror("Error", "Altura debe ser un numero")
		
			try:
				float(data['peso'])
			except:
				messagebox.showerror("peso", "Altura debe ser un numero")
			
			valor = data

		return valor

	def clear(self):
		for campo in self.__campos:
			self.__campos[campo].delete(0, END)
			self.__campos[campo].config(state='disabled') # normal disabled readonly

	def setPaciente(self, paciente: Paciente):
		self.clear()
		for campo in self.__campos:
			self.__campos[campo].config(state='normal')
			
		self.__campos['nombre'].insert(0, paciente.getNombre())
		self.__campos['apellido'].insert(0, paciente.getApellido())
		self.__campos['telefono'].insert(0, paciente.getTelefono())
		self.__campos['altura'].insert(0, "{:.2f}".format(paciente.getAltura()))
		self.__campos['peso'].insert(0, "{:.2f}".format(paciente.getPeso()))

		
