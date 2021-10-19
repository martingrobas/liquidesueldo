
"""Cosas que no deben faltar en la liquidación de sueldo:



Antiguedad ()
Sueldo basico (Según tabla de convenio)

Presentismo (+)
Horas extras (+)

Direccion
Nacimiento
Datos filiatorios
DNI

Fecha de ingreso
Escala salarial
Vacaciones
Soltero o Casado
Con o sin hijos


Descuentos:
Jubilación
Obra Social

"""

"""
A consultar:
def completacuil():
    # Con esta función determinamos el CUIL de cada empleado según su DNI (o sexo).

def calculaedad(dd,mm,aa):
    #Esta funcion debe determinar la edad del individuo a partir de la fecha de nacimiento del mismo.

"""



# PRIMERA PARTE - IMPORTACIONES
#------ Se hacen los importes necesarios ------#
import csv
import time
import numpy as np
import random
from datetime import datetime
import pandas as pd  # Hacer en la terminal pip install numpy y NumPy y luego pip install pandas
import colored
from colored import stylize #Hacer en la terminal pip install termcolor


# SEGUNDA PARTE - LECTURA DE DATOS INICIALES
#------ Carga de datos ------#
df = pd.read_csv("categorias.csv")
matriz_trabajadores = np.loadtxt("categorias.csv", dtype=np.object, delimiter=",")


# TERCERA PARTE - FUNCIONES



def obtener_cuil(sexo, dni):
    cuil = ''
    if sexo == "F":
        num = random.randint(1, 10)
        cuil = '27' + ' ' + str(dni) + ' ' + str(num) 
    else:
        num = random.randint(1, 10)
        cuil = '20' + ' ' + str(dni) + ' ' + str(num) 
    
    return cuil

#DNI 36159460
#CUIL 20 36159460 7





# Opción 1
def agregar_trabajador():

    # Nombres
    nombre = input("Ingrese el nombre y apellido:\n")
    
    # Letras
    sexo = input("Ingrese 'f' para femenino o 'm' para masculino\n").toupper()
    while (sexo != 'F') or (sexo != 'M'):
        print('No ingresó una letra válida')
        sexo= input("Por favor ingrese 'f' para femenino o 'm' para masculino\n").toupper()
    
    # Numeros
    legajo=int(input("Ingrese el legado del trabajador:\n"))
    dni=int(input("Ingrese el DNI:\n"))
    cuil = obtener_cuil(sexo, dni)

    fechaingreso = input("Indique la fecha de ingreso a la empresa (DD/MM/AAAA):\n")
    ingreso = datetime.strptime(fechaingreso, '%d/%m/%Y')
    #En base a la fecha de ingreso se debe determinar la antiguedad (en años) con una función.

    birthday = input("Ingrese la fecha de nacimiento (DD/MM/AAAA):\n")
    cumple = verificar_fecha(birthday)
    while not cumple:
        print('No ingresó una fecha válida')
        birthday = input("Ingrese la fecha de nacimiento (DD/MM/AAAA):\n")
        cumple = verificar_fecha(birthday)
        
    
    
    
    """Elija el puesto:
    1 Supervisor   60000
    2 Encargado 550000
    3 Jardinero 40000
    
    sup
    enc
    jard
    }"""

    print("opción 1")

# Opción 2 
def eliminar_trabajador(matriz_trabajadores):
    print("opción 2")

# Opción 3
def consultar_trabajador():
    print("opción 3")

# Opción 4 
def obtener_liquidacion():
    print("opción 4")

# Opción 5
def imprimir_data(data_frame):
    print(data_frame)

# Opción 6
def detener_programa():
    print("Gracias por usar nuestro sistema de liquidacion de sueldos, PONENOS UN 10 FORRO :D")
    print("opción 6")
    
  
# CUARTA PARTE - PROGRAMA PRINCIPAL
#------Se muestra la "interfaz" ------#
azul = colored.fg("sky_blue_1") + colored.attr("bold")
morado = colored.fg("purple_1b") + colored.attr("bold")

for i in range(3):
    print(stylize("Iniciando...", morado))
    time.sleep(0.7)
print()
print(stylize("Bienvenido al programa de Liquidacion de Sueldos", azul)), time.sleep(0.7)
print()

corriendo = True
while corriendo:
    print(stylize("             Menú Principal           ", morado)), time.sleep(0.5)
    print(stylize(" 1  -    ", morado), stylize("Agregar Trabajador", azul)), time.sleep(0.5)
    print(stylize(" 2  -    ", morado), stylize("Eliminar Trabajador", azul)), time.sleep(0.5)
    print(stylize(" 3  -    ", morado), stylize("Consultar Trabajador", azul)), time.sleep(0.5)
    print(stylize(" 4  -    ", morado), stylize("Obtener una Liquidación", azul)), time.sleep(0.5)
    print(stylize(" 5  -    ", morado), stylize("Imprimir Datos", azul)), time.sleep(0.5)
    print(stylize(" 6  -    ", morado), stylize("Detener Programa", azul))    , time.sleep(0.8)

    print()
    opcion = int(input("Por favor seleccione una opción: "))
    print()
    
    while (opcion < 1) or (opcion > 6):
        print()
        print("Opción no válida")
        opcion = int(input("Por favor indique su opción a seleccionar (entre 1 y 6): "))

    if (opcion == 1):
        agregar_trabajador()
        
    elif (opcion == 2):
        eliminar_trabajador()
    elif (opcion == 3):
        consultar_trabajador()
    elif (opcion == 4):
        obtener_liquidacion()
    elif (opcion == 5):
        imprimir_data(df)
    else:
        detener_programa()

"""Se debe desplegar el menu con las 4 opciones, a saber:

1) Crear o generar carga de datos de empleado #GABI agregar trabajador
2) Modificar datos #Lucas 
3) Borrar datos sobre un empleado #Julian
4) Consultar datos/Imprimir datos #Martin

""" 