from tkinter import Toplevel, Button
from .FormDatosPaciente import FormDatosPaciente
from .Paciente import Paciente

class VentanaNuevoPaciente(Toplevel):
	__callback = None
	def __init__(self, parent, callback):
		super().__init__(parent)

		self.__callback = callback
		self.__form = FormDatosPaciente(self)
		self.__form.pack(padx=10, pady=10)

		self.__botonConfirmar = Button(self, text="Confirmar", command=self.confirmar)
		self.__botonConfirmar.pack(pady=10)

	def confirmar(self):
		data = self.__form.obtenerDatos()
		
		if data is not None:
			self.__callback(Paciente(data)) # type: ignore
			self.destroy()
	