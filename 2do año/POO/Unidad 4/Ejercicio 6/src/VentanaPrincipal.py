from .ManejadorProvincias import ManejadorProvincias
from .VentanaNuevaProvincia import VentanaNuevaProvincia
from .FormDatosProvincia import FormDatosProvincia
from .Provincia import Provincia

from tkinter import Tk, Button, Listbox, Scrollbar, Frame, messagebox
from tkinter import LEFT, RIGHT, BOTH, BOTTOM, Y, END

class VentanaPrincipal(Tk):
	__manejadorProvincias: ManejadorProvincias

	def __init__(self, manejador):
		super().__init__()
		self.__manejadorProvincias = manejador
		self.title("Lista de Provincias")

		self.__provinciasFrame = Frame(self)
		self.__provinciasFrame.pack(side=LEFT, padx=10, pady=10)

		self.__listbox = Listbox(self.__provinciasFrame, height=15)
		self.__listbox.pack(side=LEFT, fill=BOTH, expand=1)
		self.__listbox.bind("<Double-Button-1>", self.seleccionarProvincia)
		self.__listbox.bind("<<ListboxSelect>>", self.seleccionarProvincia)
	
		scroll = Scrollbar(self.__provinciasFrame, command=self.__listbox.yview)
		scroll.pack(side=RIGHT, fill=Y)
		self.__listbox.config(yscrollcommand=scroll.set)

		self.__form = FormDatosProvincia(self, manejador)
		self.__form.pack(padx=10, pady=10)

		self.__botonAgregarProvincia = Button(self, text="Agregar Provincia", command=self.añadirProvincia)
		self.__botonAgregarProvincia.pack(side=BOTTOM, pady=5)

		for provincia in self.__manejadorProvincias:
			self.cargarProvinciaALista(provincia)

		self.mostrarProvincia(0)

	def añadirProvincia(self):
		def callback(provincia):
			self.__manejadorProvincias.agregar(provincia)
			self.cargarProvinciaALista(provincia)

		ventana = VentanaNuevaProvincia(self, self.__manejadorProvincias, callback)
		ventana.wait_window()

	def cargarProvinciaALista(self, provincia):
		self.__listbox.insert(END, provincia.getNombre())

	def mostrarProvincia(self, pos):
		primerProvincia = self.__manejadorProvincias.obtener(pos)

		if primerProvincia is None:
			self.__form.clear()
		else:
			self.__form.setProvincia(primerProvincia)
			self.__listbox.select_set(pos)

	def seleccionarProvincia(self, _):
		currentSelection = self.__listbox.curselection()

		if len(currentSelection) != 0:
			self.mostrarProvincia(currentSelection[0])
