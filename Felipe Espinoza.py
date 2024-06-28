#1.	Asignar saldos aleatorios: Generar saldos aleatorios para 10 clientes. '''''OK'''''
#2.	Clasificar saldos: Mostrar los saldos clasificados en tres rangos específicos. '''''OK''''''
#3.	Ver estadísticas: Calcular y mostrar estadísticas avanzadas sobre los saldos.
   #a.	Saldo más alto '''ok'''
   #b.	Saldo más bajo''' OK''''
   #c.	Saldo promedio '''OK'''''
   #d.	Media geométrica.
#4.	Reporte de saldos: Generar un reporte detallado de saldos con deducciones por diferentes conceptos y saldo neto, y exportar a un archivo CSV

import csv  # Importa el módulo csv
import random
import statistics


def generar_saldos_aleatorios(): # se genera aca saldo para los 10 clientes
    saldos = []
    for cliente in range(10):
        saldo = round(random.uniform(1000, 10000), 2)
        saldos.append(saldo)
    return saldos


def clasificar_saldos(saldos): # se genera 3 rangos de saldos y se clasifican
    bajos = []
    medios = []
    altos = []
    
    for saldo in saldos:
        if saldo < 3000:
            bajos.append(saldo)
        elif saldo < 7000:
            medios.append(saldo)
        else:
            altos.append(saldo)
    
    return bajos, medios, altos


def calcular_maximo(lista): # se calcula el maximo de la lista
    maximo = lista[0]
    for elemento in lista[1:]:
        if elemento > maximo:
            maximo = elemento
    return maximo


def calcular_minimo(lista): # se calcula el minimo de la lista range 0
    minimo = lista[0]
    for elemento in lista[1:]:
        if elemento < minimo:
            minimo = elemento
    return minimo


def calcular_promedio(lista): # promedio de una lista ocupo el len ya que al ser una iteracion promedioa todo jutno
    suma = sum(lista)
    promedio = suma / len(lista)
    return promedio


def calcular_media_geometrica(lista): # aca ocupo statitics para calcular la media geometrica de manera mas precisa y detllada, ocupando las herramientas de python
    media_geometrica = statistics.geometric_mean(lista)
    return media_geometrica


def generar_reporte_saldos(saldos, archivo_csv): # reporte de saldos y archivo csv
    deduccion_1 = 100
    deduccion_2 = 50
    saldos_netos = []

    for saldo in saldos:
        saldo_neto = saldo - deduccion_1 - deduccion_2
        saldos_netos.append(saldo_neto)

    with open(archivo_csv, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Cliente', 'Saldo', 'Deducción 1', 'Deducción 2', 'Saldo Neto'])
        for i, saldo in enumerate(saldos):
            writer.writerow([f'Cliente {i+1}', saldo, deduccion_1, deduccion_2, saldos_netos[i]])

    print(f"Reporte generado y guardado en {archivo_csv}. =) ")


def mostrar_menu(): #MENU USUARIO C:
    print("\n*** Menú ***")
    print("1. Generar saldos aleatorios ")
    print("2. Clasificar saldos ")
    print("3. Ver estadísticas ")
    print("4. Generar reporte de saldos ")
    print("5. Salir ")


def manejar_opcion(opcion): #SELECCION DE L USUARIOO desgloss
    global saldos
    if opcion == '1':
        saldos = generar_saldos_aleatorios()
        print("Saldos aleatorios generados: ")
        print(saldos)
    elif opcion == '2':
        bajos, medios, altos = clasificar_saldos(saldos)
        print("Saldos clasificados: ")
        print(f"Bajos: {bajos} ")
        print(f"Medios: {medios} ")
        print(f"Altos: {altos} ")
    elif opcion == '3':
        if not saldos:
            print("No se han generado saldos aleatorios aún ")
        else:
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
        if not saldos:
            print("No se han generado saldos aleatorios aún ")
        else:
            archivo_csv = 'reporte_saldos.csv'
            generar_reporte_saldos(saldos, archivo_csv)
    elif opcion == '5':
        print("¡Hasta luego!, que tenga un buen dia ")
        exit()
    else:
        print("Opción inválida. Por favor selecciona una opción válida del menú porfavor ")

if __name__ == "__main__":
    saldos = []
    
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción del menú (1-5): ")
        manejar_opcion(opcion)
