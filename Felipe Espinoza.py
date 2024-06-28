#1.	Asignar saldos aleatorios: Generar saldos aleatorios para 10 clientes.
#2.	Clasificar saldos: Mostrar los saldos clasificados en tres rangos específicos.
#3.	Ver estadísticas: Calcular y mostrar estadísticas avanzadas sobre los saldos.
   #a.	Saldo más alto
   #b.	Saldo más bajo
   #c.	Saldo promedio
   #d.	Media geométrica.
#4.	Reporte de saldos: Generar un reporte detallado de saldos con deducciones por diferentes conceptos y saldo neto, y exportar a un archivo CSV

import random

#aca se genera saldos al azar 
def generar_saldos_aleatorios():
    saldos = []
    for _ in range(10):
        saldo = round(random.uniform(1000, 10000), 2)  # Número aleatorio entre 1000 y 10000, Ocupo el '2' para que redonde lso saldos aleatorios para q sea mas manejable numeros
        saldos.append(saldo)
    return saldos
