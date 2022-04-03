# Importamos la clase Boleta de a la carpeta boleta
from trabajador import Trabajador 
from boleta import Boleta

trabajador1 = Trabajador("Andre", "B", 10, 200)
boleta1 = Boleta("B", 10, 200)

# Ejecutamos el código
print("\n*** DATOS DE ENTRADA ***")
trabajador1.Nombre()
trabajador1.Categoria()
trabajador1.Horas_Extras()
trabajador1.Minutos_Tarde()
print("\n*** BOLETA DE PAGO ***")
trabajador1.Nombre()
trabajador1.Categoria()
print("SUELDO BASICO:          ",boleta1.Sueldo_Basico())
print("DESCUENTO TARDANZAS:    ",round(boleta1.Descuento_Tardanza(),2))
print("PAGO HORAS EXTRAS:      ",round(boleta1.Pago_Horas_Extras(),2))
print("SUELDO NETO:            ",round(boleta1.Sueldo_Neto(),2))  