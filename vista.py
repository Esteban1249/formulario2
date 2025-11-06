# vista.py

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # Importamos ttk por si queremos usar Combobox en el futuro

class EmpleadoView(tk.Frame):
    """Crea y gestiona la interfaz gráfica del formulario."""
    
    def __init__(self, master, controlador):
        super().__init__(master)
        self.master.title("Formulario de Empleado - MVC")
        self.controlador = controlador
        
        self.entradas = {} # Diccionario para almacenar las variables de entrada
        
        self.crear_widgets()
        self.pack(padx=10, pady=10, fill="both", expand=True)

    def crear_widgets(self):
        campos = [
            "Nombres", "Apellidos", "Numero de Identificacion", "Correo Electrónico", 
            "Fecha de Nacimiento", "Dirección", "Numero de Hijos", "Cargo Empresa"
        ]
        
        
        for i, campo in enumerate(campos):
            campo_key = campo.lower().replace(" ", "_")
            
            
            tk.Label(self, text=f"{campo}:").grid(row=i, column=0, padx=5, pady=5, sticky="w")
            
            var = tk.StringVar()

            if campo == "Numero de Hijos":
                entry = tk.Spinbox(self, from_=0, to=10, textvariable=var, width=38)
                var.set(0) # Valor inicial en 0
            else:
                
                entry = tk.Entry(self, textvariable=var, width=40)
            
            entry.grid(row=i, column=1, padx=5, pady=5, sticky="ew")
            self.entradas[campo_key] = var
        
        
        btn_enviar = tk.Button(self, text="Enviar Datos", command=self._enviar_formulario)
        btn_enviar.grid(row=len(campos), column=0, columnspan=2, pady=15)

    def _enviar_formulario(self):
        """
        Recopila los datos de la interfaz y los pasa al Controlador.
        """
        datos = {k: v.get() for k, v in self.entradas.items()}
        self.controlador.procesar_formulario(datos)
        
    def mostrar_mensaje(self, titulo, mensaje):
        """
        Muestra un mensaje (éxito o error) al usuario.
        """
        messagebox.showinfo(titulo, mensaje)
        
    def limpiar_formulario(self):
        """
        Limpia todos los campos del formulario.
        """
        for key, var in self.entradas.items():
            var.set("")
            if key == "numero_de_hijos":

                 var.set(0)
