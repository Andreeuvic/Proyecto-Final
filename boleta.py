# Creamos la clase Boleta
class Boleta:
    
        # Metodos Constructor
    #--------------------------------------------------------------
    def __init__(self, categoria, horas_extras, minutos_tardes):
        
        # Definimos las propiedades y asignamos valores 
        self.categoria = categoria
        self.horas_extras = horas_extras
        self.minutos_tardes = minutos_tardes
    #--------------------------------------------------------------
    
    
        # Metodos Sueldo_Basico
    #------------------------------------
    def Sueldo_Basico(self):
        if self.categoria == "A":
            sb = 3000
            return sb
    #------------------------------------
        elif self.categoria == "B":
            sb = 2500
            return sb
    #------------------------------------    
        elif self.categoria == "C":
            sb = 2000
            return sb
    #------------------------------------   
        else:
            sb = 0
            return sb
    #------------------------------------
    
    
    
        # Metodos Descuento_Tardanza
    #--------------------------------------------------------------------------------------------
    def Descuento_Tardanza(self):
        descuento = ((self.Sueldo_Basico() / 240) / 60) * self.minutos_tardes
        return descuento 
    #--------------------------------------------------------------------------------------------
    
        # Metodos Pago_Horas_Extras
    #--------------------------------------------------------------------------------------------
    def Pago_Horas_Extras(self):
        ph_extras = (self.Sueldo_Basico() / 240) * self.horas_extras
        return ph_extras
    
        # Metodos Sueldo_Neto
    #-------------------------------------------------------------------------------------------- 
    def Sueldo_Neto(self):
        sn = (self.Pago_Horas_Extras() - self.Descuento_Tardanza()) + self.Sueldo_Basico()
        return sn 
    #--------------------------------------------------------------------------------------------