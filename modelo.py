# modelo.py

class EmpleadoModel:
    """Representa la estructura de datos del formulario."""
    
    def __init__(self, nombres="", apellidos="", identificacion="", correo="", 
                 fecha_nacimiento="", direccion="", num_hijos=0, cargo=""):
        # Los atributos del modelo coinciden con los ítems del formulario
        self.nombres = nombres
        self.apellidos = apellidos
        self.identificacion = identificacion
        self.correo = correo
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion
        self.num_hijos = num_hijos
        self.cargo = cargo

    def guardar_datos(self, datos_formulario):
        """
        Asigna los datos validados del formulario a los atributos del modelo.
        En un caso real, aquí iría la lógica para interactuar con una base de datos.
        """
        # Se asume que los datos ya están validados por el Controlador
        self.nombres = datos_formulario.get("nombres", "")
        self.apellidos = datos_formulario.get("apellidos", "")
        self.identificacion = datos_formulario.get("identificacion", "")
        self.correo = datos_formulario.get("correo", "")
        self.fecha_nacimiento = datos_formulario.get("fecha_nacimiento", "")
        self.direccion = datos_formulario.get("direccion", "")
        
        # Intenta convertir a entero, si falla, usa 0
        try:
            self.num_hijos = int(datos_formulario.get("num_hijos", 0))
        except ValueError:
            self.num_hijos = 0
            
        self.cargo = datos_formulario.get("cargo", "")
        
        # Para demostración: imprime los datos guardados
        print("\n--- Datos Guardados en el Modelo ---")
        print(f"Nombres: {self.nombres}")
        print(f"Identificación: {self.identificacion}")
        print(f"Número de Hijos: {self.num_hijos}")
        print("------------------------------------")
        
        return True # Retorna éxito