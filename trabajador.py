# Creando la clase Trabajador
class Trabajador: # Clase Trabajador
    
    def __init__(self, nombre, categoria, horas_extras, minutos_tarde):
        
        # Definimos las propiedades y asignamos valores 
        self.nombre = nombre       
        self.categoria = categoria
        self.horas_extras = horas_extras
        self.minutos_tarde = minutos_tarde
        
    # Metodos o Funciones
    def Nombre(self):
        print("TRABAJADOR:             ", self.nombre)
    def Categoria(self):
        print("CATEGORIA:              ", self.categoria)
    def Horas_Extras(self):
        print("HORAS EXTRAS:           ",self.horas_extras)
    def Minutos_Tarde(self):
        print("TARDANZA: (minutos)     ",self.minutos_tarde)