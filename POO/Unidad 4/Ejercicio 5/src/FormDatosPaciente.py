from tkinter import messagebox, LabelFrame, Frame, Label, Entry, Button, RIGHT, END

class FormDatosPaciente(LabelFrame):
    __campos = {}
    __master = None
    def __init__(self, master, **kwargs):
        super().__init__(master, text="Paciente", padx=10, pady=10, **kwargs)
        self.__master = master
        self.__frame = Frame(self)
        self.__frame.pack()

        self.__campos['nombre'] = self.crearCampo(0, 'Nombre')
        self.__campos['apellido'] = self.crearCampo(1, 'Apellido')
        self.__campos['telefono'] = self.crearCampo(2, 'Teléfono')
        self.__campos['altura'] = self.crearCampo(3, 'Altura')
        self.__campos['peso'] = self.crearCampo(4, 'Peso')

    def crearCampo(self, i, text):
        label = Label(self.__frame, text=text)
        entry = Entry(self.__frame, width=25)
        label.grid(row=i, column=0, pady=5)
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
        
        return data

    def clear(self):
        for campo in self.__campos:
            self.__campos[campo].delete(0, END)

    def setPaciente(self, paciente):
        self.clear()
        self.__campos['nombre'].insert(0, paciente.getNombre())
        self.__campos['apellido'].insert(0, paciente.getApellido())
        self.__campos['telefono'].insert(0, paciente.getTelefono())
        self.__campos['altura'].insert(0, paciente.getAltura())
        self.__campos['peso'].insert(0, paciente.getPeso())

class FormDatosPaciente2(FormDatosPaciente):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.__botonGuardar = Button(self, text="Guardar", command=self.guardar)
        self.__botonGuardar.pack(side=RIGHT, ipadx=5, padx=5, pady=5)
        
        self.__botonBorrar = Button(self, text="Borrar", command=self.borrar)
        self.__botonBorrar.pack(side=RIGHT, ipadx=5, padx=5, pady=5)
        
        self.__botonIMC = Button(self, text="Ver IMC", command=self.verIMC)
        self.__botonIMC.pack(side=RIGHT, ipadx=5, padx=5, pady=5)

    def guardar(self):
        pass

    def borrar(self):
        pass

    def verIMC(self):
        pass
