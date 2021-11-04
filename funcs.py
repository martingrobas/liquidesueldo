import time
import random
import colored
from funcs import *
import pandas as pd
from datetime import datetime, date
from colored import stylize

# TERCERA PARTE - FUNCIONES

def verificar_fecha(cad, fecha_actual):
    fecha = cad.split("-") 
    year = int(fecha[2])
    month = int(fecha[1])
    day = int(fecha[0])

    es_bisiesto = False
    if (year % 400 == 0) and (year % 4 == 0) and (year % 100 == 0):
        es_bisiesto = True #bisiesto

    elif (year % 4 == 0) and (year % 100 == 0):
        es_bisiesto = False  #no bisiesto

    elif (year % 4 == 0):
        es_bisiesto = True #bisiesto

    es_valida = True
    
    if (day < 1):
        es_valida = False
    
    elif (month > 12):
        es_valida = False
    
    elif (year > fecha_actual.year):
        es_valida = False

    elif (month == 2) and (es_bisiesto == False) and (day > 28):
        es_valida = False

    elif (month == 2) and (es_bisiesto) and (day > 29):
        es_valida = False

    elif (day > 31) and ((month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12)):
        es_valida = False

    elif (day > 30) and ((month == 4) or (month == 6) or (month == 9) or (month == 11)):
        es_valida = False
    
    return es_valida

def calcular_diferencia(menor_fecha, mayor_fecha ): 
    return (mayor_fecha.year - menor_fecha.year) + (1 if ((menor_fecha.month <= mayor_fecha.month) and (menor_fecha.day <= mayor_fecha.day)) else 0) 

def obtener_cuil(sexo, dni):
    cuil = ''
    if sexo == "F":
        num = random.randint(1, 10)
        cuil = '27' + ' ' + str(dni) + ' ' + str(num) 
    else:
        num = random.randint(1, 10)
        cuil = '20' + ' ' + str(dni) + ' ' + str(num) 
    
    return cuil

def verificar_letras_ingresadas(respuesta, opcion1, opcion2):
    while (respuesta != opcion1) and (respuesta != opcion2):
        print('No ingresó una letra válida')
        respuesta = input("Por favor ingrese el formato solicitado: ").upper()
    return respuesta

def verificar_existencia(legajo):
    # revisa si un trabajador esta en el csv
    legajo = str(legajo)
    existe = False
    with open('./csv_files/trabajadores.csv', "r") as trabajadores_file:
        trabajadores = trabajadores_file.readlines()
        for trabajador in trabajadores:
            if legajo in trabajador:
                existe = True
    return existe
    
def solicitar_puesto(categorias, azul, morado):
    time.sleep(1.5)
    
    print()
    print("A continuación se le mostrará los distintos puestos para que indique una opción"), time.sleep(0.7)
    print(stylize("Puestos: ", morado)), time.sleep(0.3)
    for i in range(len(categorias)):
        print(stylize(f" {i + 1}  -    ", morado), stylize(categorias[i][0], azul)), time.sleep(0.3)
    print()

    time.sleep(1)
    num_puesto = int(input("Por favor seleccione un número del 1 al 21 para indicar el puesto del trabajador: "))
    while num_puesto < 1 or num_puesto > 21:
        time.sleep(0.5)
        print()
        print("Error, ingresó un valor inválido")
        num_puesto = int(input("Por favor seleccione un número del 1 al 21 para indicar el puesto del trabajador: "))

    puesto = categorias[num_puesto - 1][0]
    basico = int(categorias[num_puesto - 1][1])
    return puesto, basico