# controlador.py

from modelo import EmpleadoModel
from vista import EmpleadoView
import tkinter as tk

class EmpleadoController:
    """Controla el flujo de la aplicación MVC."""
    
    def __init__(self, root):
        self.modelo = EmpleadoModel()
        self.vista = EmpleadoView(root, self)

    def procesar_formulario(self, datos):
        """
        Recibe los datos de la Vista, los valida y actualiza el Modelo.
        """
        
        
        errores = self._validar_datos(datos)
        
        if errores:
            mensaje_error = "Por favor, corrige los siguientes errores:\n" + "\n".join(errores)
            self.vista.mostrar_mensaje("Error de Validación", mensaje_error)
        else:
            exito = self.modelo.guardar_datos(datos)
            
            if exito:
                self.vista.mostrar_mensaje("Éxito", "¡Datos del empleado guardados correctamente!")
                self.vista.limpiar_formulario()
            else:
                self.vista.mostrar_mensaje("Error", "No se pudieron guardar los datos. Intenta de nuevo.")

    def _validar_datos(self, datos):
        """
        Implementa una validación básica de los campos.
        """
        errores = []
        
       
        for campo in ["nombres", "apellidos", "identificacion", "correo_electrónico"]:
            if not datos.get(campo):
                errores.append(f"- El campo '{campo.replace('_', ' ').title()}' es obligatorio.")
                
        
        num_hijos_str = datos.get("numero_de_hijos", "0")
        if not num_hijos_str.isdigit():
             errores.append("- El 'Numero de Hijos' debe ser un valor numérico.")
             
        
        return errores


if __name__ == "__main__":
    root = tk.Tk()
    app = EmpleadoController(root)

    root.mainloop()
