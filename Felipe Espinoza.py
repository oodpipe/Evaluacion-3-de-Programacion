#1.	Asignar saldos aleatorios: Generar saldos aleatorios para 10 clientes. '''''OK'''''
#2.	Clasificar saldos: Mostrar los saldos clasificados en tres rangos específicos. '''''OK''''''
#3.	Ver estadísticas: Calcular y mostrar estadísticas avanzadas sobre los saldos.
   #a.	Saldo más alto '''ok'''
   #b.	Saldo más bajo''' OK''''
   #c.	Saldo promedio '''OK'''''
   #d.	Media geométrica.
#4.	Reporte de saldos: Generar un reporte detallado de saldos con deducciones por diferentes conceptos y saldo neto, y exportar a un archivo CSV

import csv
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


def generar_reporte_saldos(saldos, archivo_csv):
    deduccion_1 = 100  #unad educcion
    deduccion_2 = 50   #una deduccion
    saldos_netos = []

    
    for saldo in saldos: #calculo saldo neto y lo pongo en saldo_neto
        saldo_neto = saldo - deduccion_1 - deduccion_2
        saldos_netos.append(saldo_neto)

    
    with open(archivo_csv, 'w', newline='') as file: #escribo datos en archivo csv
        writer = csv.writer(file)
        writer.writerow(['Cliente', 'Saldo', 'Deducción 1', 'Deducción 2', 'Saldo Neto'])
        for i, saldo in enumerate(saldos):
            writer.writerow([f'Cliente {i+1}', saldo, deduccion_1, deduccion_2, saldos_netos[i]])

    print(f"Reporte generado y guardado en {archivo_csv}. =) ")



 #MENU DE USUARIO

print("\n*** Menú ***")
print("1. Generar saldos aleatorios ")
print("2. Clasificar  saldos ")
print("3. Ver estadísticas ")
print("4. Generar reporte de saldos ")
print("5. Salir ")


def manejar_opcion(opcion): #dejo q el usuario escoga
    if opcion == '1':
        saldos = generar_saldos_aleatorios()
        print("Saldos aleatorios generados:  ")
        print(saldos)
    elif opcion == '2':
        bajos, medios, altos = clasificar_saldos(saldos)
        print("Saldos clasificados: ")
        print(f"Bajos: {bajos} ")
        print(f"Medios: {medios} ")
        print(f"Altos: {altos} ")
    elif opcion == '3':
        maximo = calcular_maximo(saldos)
        minimo = calcular_minimo(saldos)
        promedio = calcular_promedio(saldos)
        media_geom = calcular_media_geometrica(saldos)
        print("Estadísticas de saldos: ")
        print(f"Saldo más alto: {maximo} ")
        print(f"Saldo más bajo: {minimo} ")
        print(f"Saldo promedio: {promedio} ")
        print(f"Media geométrica: {media_geom} ")
    elif opcion == '4':
        archivo_csv = 'reporte_saldos.csv'
        generar_reporte_saldos(saldos, archivo_csv)
    elif opcion == '5':
        print("¡Hasta luego!, que tenga buen dia ")
        exit()
    else:
        print("Opción inválida. Por favor selecciona una opción válida del menú.")

if __name__ == "__main__":
    saldos = []
    
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción del menú (1-5): ")
        manejar_opcion(opcion)
        
print('menu ')

PermissionErrorsadas
f
asfsa
fsafaf
