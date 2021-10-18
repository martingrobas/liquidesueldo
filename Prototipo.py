
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
"""

# PRIMERA PARTE - IMPORTACIONES
#------ Se hacen los importes necesarios ------#
import csv
import time
import pandas as pd  # Hacer en la terminal pip install numpy y NumPy y luego pip install pandas
import colored
from colored import stylize #Hacer en la terminal pip install termcolor


# SEGUNDA PARTE - LECTURA DE DATOS INICIALES
#------ Carga de datos ------#
df = pd.read_csv("categorias.csv")




# TERCERA PARTE - FUNCIONES

# Opción 1
def agregar_trabajador():
    print("opción 1")

# Opción 2
def eliminar_trabajador():
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
2) Modificar datos #Lucas Perez Erro
3) Borrar datos sobre un empleado #Julian
4) Consultar datos/Imprimir datos #Martin

""" 