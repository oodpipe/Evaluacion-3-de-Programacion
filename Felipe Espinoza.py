#1.	Asignar saldos aleatorios: Generar saldos aleatorios para 10 clientes. '''''OK'''''
#2.	Clasificar saldos: Mostrar los saldos clasificados en tres rangos específicos. '''''OK''''''
#3.	Ver estadísticas: Calcular y mostrar estadísticas avanzadas sobre los saldos.
   #a.	Saldo más alto '''ok'''
   #b.	Saldo más bajo''' OK''''
   #c.	Saldo promedio '''OK'''''
   #d.	Media geométrica.
#4.	Reporte de saldos: Generar un reporte detallado de saldos con deducciones por diferentes conceptos y saldo neto, y exportar a un archivo CSV

import random

#aca se genera saldos al azar 
def generar_saldos_aleatorios():
    saldos = []
    for cliente in range(10):
        saldo = round(random.uniform(1000, 10000), 2)  # Número aleatorio entre 1000 y 10000, Ocupo el '2' para que redonde lso saldos aleatorios para q sea mas manejable numeros
        saldos.append(saldo)
    return saldos

def clasificar_saldos(saldos):
    bajos = []
    medios = []
    altos = []
    
    for saldo in saldos:
        if saldo < 3000:
            bajos.append(saldo) #lista de los de bajoo
        elif saldo < 7000:
            medios.append(saldo) #lista de lso de medios
        else:
            altos.append(saldo) #lista de lso de altoss 7k o mas
    
    return bajos, medios, altos


def calcular_maximo(lista):  #maximo de la listaaa
    maximo = lista[0]
    for elemento in lista[1:]:
        if elemento > maximo:
            maximo = elemento
    return maximo


def calcular_minimo(lista): #calcula el primero o el minimo de lalista de appends
    minimo = lista[0]
    for elemento in lista[1:]:
        if elemento < minimo:
            minimo = elemento
    return minimo


def calcular_promedio(lista): #funcion para sacar el promedio de la lista ocupo el 'len' para saque el promedio de la iteracion
    suma = sum(lista)
    promedio = suma / len(lista)
    return promedio

import statistics

def calcular_media_geometrica(lista): #ocupe statistics proporciona una función llamada geometric_mean que realiza este cálculo de manera eficiente, sin pérdida de precisión
    media_geometrica = statistics.geometric_mean(lista)
    return media_geometrica

