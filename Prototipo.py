
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
import re
import time
import random
import colored
import numpy as np
import pandas as pd  # Hacer en la terminal pip install numpy y NumPy y luego pip install pandas
from datetime import datetime
from colored import stylize #Hacer en la terminal pip install termcolor


# SEGUNDA PARTE - LECTURA DE DATOS INICIALES
#------ Carga de datos ------#
df_categorias = pd.read_csv("categorias.csv")
df_trabajadores = pd.read_csv("trabajadores.csv")
matriz_trabajadores = np.loadtxt("trabajadores.csv", dtype=np.object, delimiter=",")


# TERCERA PARTE - FUNCIONES

def verificar_fecha(cad):
    '''validacion='^(0\d|1[0-9]|2[0-9]|3[0-1])/(0\d|1[0-2])/(19[0-9]{2}|20[0-9]{2})$'
    return bool(re.search(validacion,cad))'''
    fecha = cad.split("-") 
    year = fecha[2]
    month = fecha[1]
    day = fecha[0]

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

    elif (month == 2) and (es_bisiesto == False) and (day > 28):
        es_valida = False

    elif (month == 2) and (es_bisiesto) and (day > 29):
        es_valida = False

    elif (month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12) or (day > 31):
        es_valida = False

    elif (month == 4) or (month == 6) or (month == 9) or (month == 11) or (day > 30):
        es_valida = False

    else:
        print("Fecha válida")
    
    return es_valida


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
    while (respuesta != opcion1) or (respuesta != opcion):
        print('No ingresó una letra válida')
        respuesta = input("Por favor ingrese el formato solicitado: ").toupper()
    return respuesta
    

def solicitar_puesto(df_categorias):
    time.sleep(1.5)
    df_categorias[df_categorias["FUNCION"]].astype(str)
    """Elija el puesto:
    1 Supervisor   60000
    2 Encargado 550000
    3 Jardinero 40000
    
    sup
    enc
    jard
    }"""

# Opción 1
def agregar_trabajador(matriz_trabajadores):
    time.sleep(1.5)
    trabajador = []

    # Nombres
    nombre = input("Ingrese el nombre y apellido:\n")
    trabajador.append(nombre)
    
    # Letras
    sexo = input("Ingrese 'f' para femenino o 'm' para masculino\n").toupper()
    sexo_ = verificar_letras_ingresadas(sexo, 'F', 'M')
    trabajador.append(sexo_)
    

    # Números
    legajo=int(input("Ingrese el legado del trabajador:\n"))
    trabajador.append(legajo)

    dni=int(input("Ingrese el DNI:\n"))
    trabajador.append(dni)

    cuil = obtener_cuil(sexo, dni)
    trabajador.append(cuil)

    fecha_ingreso = input("Indique la fecha de ingreso a la empresa (DD-MM-AAAA):\n")
    ingreso_correcto = verificar_fecha(fecha_ingreso)
    while not ingreso_correcto:
        print('No ingresó una fecha válida')
        birthday = input("Introduzca la fecha de ingreso a la empresa (DD-MM-AAAA):\n")
        ingreso_correcto = verificar_fecha(ingreso_correcto)
    trabajador.append(fecha_ingreso)

    fecha_actual = datetime.today().strftime('%Y-%m-%d')
    antiguedad = fecha_actual - fecha_ingreso
    trabajador.append(antiguedad)
    
    birthday = input("Ingrese la fecha de nacimiento (DD-MM-AAAA):\n")
    cumple = verificar_fecha(birthday)
    while not cumple:
        print('No ingresó una fecha válida')
        birthday = input("Ingrese la fecha de nacimiento (DD-MM-AAAA):\n")
        cumple = verificar_fecha(birthday)
    trabajador.append(birthday)
        
    edad = fecha_actual - birthday
    trabajador.append(edad) 

    horas_extras = input("Indique las horas extras totales del trabajador: ")
    trabajador.append(horas_extras)

    presentismo = input("Ingrese 's' para indicar que posee presentismo, o 'n' para indicar que no posee: ").toupper()
    presentismo_ = verificar_letras_ingresadas(presentismo, 'S', 'N')
    trabajador.append(presentismo_)

    escala_salarial = solicitar_escala_salarial(df_categorias)
    trabajador.append(escala_salarial)

    vacaciones = input("Ingrese la cantidad de dias de vacaciones del trabajador: ")
    while (vacaciones < 0) or (vacaciones > 100):
        print('No ingresó un numero valido, este debe ser un entero positivo y no mayor a cien')
        vacaciones= input("Ingrese la cantidad de dias de vacaciones del trabajador: ")
    trabajador.append(vacaciones)

    estado_civil = input("Ingrese 'c' para indicar que esta casado, o 's' para soltero: ").toupper()
    estado_civil_ = verificar_letras_ingresadas(estado_civil, 'C', 'S')
    trabajador.append(estado_civil_)

    hijos = input("Ingrese 's' para indicar si tiene hijos, o 'n' para indicar que no: ").toupper()
    hijos_ = verificar_letras_ingresadas(hijos, 'S', 'N')
    trabajador.append(hijos_)

    jubilacion = input("Ingrese 's' para indicar si tiene jubilacion, o 'n' para indicar que no: ").toupper()
    jubilacion_ = verificar_letras_ingresadas(hijos, 'S', 'N')
    trabajador.append(jubilacion_)
    
    puesto = solicitar_puesto(df_categorias)
    trabajador.append(puesto)

    matriz_trabajadores.append(trabajador)
    df_trabajadores = pandas.DataFrame(matriz_trabajadores)

    time.sleep(1)
    print("Trabajador agregado con exito, a continuacion sera llevado al menu principal")
    print()
    time.sleep(3.5)


# Opción 2 
def dar_de_baja(matriz_trabajadores,df_trabajadores):
    time.sleep(1.5)
    darDeBaja=int(input("ingrese el legajo del trabajador que desea dar de baja"))

    try:
        matriz_trabajadores=df_trabajadores.drop(df_trabajadores.loc[df_trabajadores['Legajo']==darDeBaja].index, inplace=True)
    except:
        time.sleep(1)
        print("No se pudo dar de baja al trabajador")
        print("Por favor intente de nuevo y verifique que el legajo sea correcto")
    finally:
        time.sleep(1)
        print("A continuación será llevado de regreso al menú principal")
        print()
        time.sleep(3.5)

# Opción 3
def consultar_trabajador(matriz_trabajadores, df_trabajadores):
    time.sleep(1.5)
    legajo = int(input("Ingrese el legajo del trabajador que desea consultar: "))
    print()

    for i in range(1, len(matriz_trabajadores)):
        if legajo == int(matriz_trabajadores[i][2]):
            time.sleep(1)
            print("El trabajador se encuentra dentro de los registros")
            print("Datos del trabajador")
            print(df_trabajadores.loc[0,:])
            print(df_trabajadores.loc[i,:])
            print()
            print("A continuación será llevado de regreso al menú principal")
            print()
            time.sleep(3.5)
            break
    else:
        time.sleep(1)
        print("El trabajador no se encuentra dentro de los registros"), time.sleep(1.5)
        print("Desea volver a intentarlo?")
        print("Ingrese -1 para volver a intentar o 0 para cotinuar:")
        respuesta = int(input("Respuesta: "))
        
        while (respuesta != -1) and (respuesta != 0):
            print("Por favor ingrese -1 para volver a intentar o 0 para cotinuar:")
            respuesta = int(input('Respuesta: ')), time.sleep(0.5)
        
        if respuesta == -1:
            consultar_trabajador(matriz_trabajadores, df_trabajadores)
        else:
            print("Entendido, será llevado de regreso al menú principal")
            print()
            time.sleep(3.5)


# Opción 4 
def obtener_liquidacion():
    time.sleep(1.5)

    print("opción 4")


# Opción 5
def imprimir_data(data_frame):
    time.sleep(1.5)
    print(data_frame)
    print()
    print("A continuación será llevado de regreso al menú principal")
    print()
    time.sleep(3.5)


# Opción 6
def finalizar_programa(morado, azul):
    time.sleep(1.5)
    print()
    print(stylize("Gracias por usar nuestro sistema de liquidación de sueldos", morado)), time.sleep(0.3)
    print(stylize("Por favor cuéntenos como ha sido su experiencia: ", morado)), time.sleep(0.3)
    print(stylize(" 1  -    ", morado), stylize("Muy Insatisfactorio", azul)), time.sleep(0.3)
    print(stylize(" 2  -    ", morado), stylize("Insatisfactorio", azul)), time.sleep(0.3)
    print(stylize(" 3  -    ", morado), stylize("Medianamente Satisfactorio", azul)), time.sleep(0.3)
    print(stylize(" 4  -    ", morado), stylize("Satisfactorio", azul)), time.sleep(0.3)
    print(stylize(" 5  -    ", morado), stylize("Muy satisfactorio", azul)), time.sleep(0.3)
    print()

    time.sleep(1)
    ranking=int(input("Por favor seleccione un número del 1 al 5 en base a su nivel de satisfaccion: "))

    while ranking < 1 or ranking > 5:
        time.sleep(0.5)
        print()
        print("Error, ingreso un valor valido")
        ranking=int(input("Por favor seleccione un número del 1 al 5 en base a su nivel de satisfaccion: "))

    print()
    time.sleep(0.5)
    rojo = colored.fg("red") + colored.attr("bold")
    naranja = colored.fg("orange_4b") + colored.attr("bold")
    amarillo = colored.fg("yellow") + colored.attr("bold")
    verde = colored.fg("green") + colored.attr("bold")

    if (ranking == 1):
        print(stylize(" :'( buscaremos mejorar el servicio", rojo))
    elif (ranking == 2):
        print(stylize(" :( que lástima, progresaremos para mejorar el programa", naranja))
    elif (ranking == 3):
        print(stylize(" :| Esperamos que la próxima sea mejor", amarillo))
    elif (ranking == 4):
        print(stylize(" :) Nos alegra", verde))
    elif (ranking == 5):
        print(stylize(" :D Fabuloso!", azul))
    
    print()
    return False                                            
    
  
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
    print(stylize("             Menú Principal           ", morado)), time.sleep(0.3)
    print(stylize(" 1  -    ", morado), stylize("Agregar Trabajador", azul)), time.sleep(0.3)
    print(stylize(" 2  -    ", morado), stylize("Dar de Baja Trabajador", azul)), time.sleep(0.3)
    print(stylize(" 3  -    ", morado), stylize("Consultar Trabajador", azul)), time.sleep(0.3)
    print(stylize(" 4  -    ", morado), stylize("Obtener una Liquidación", azul)), time.sleep(0.3)
    print(stylize(" 5  -    ", morado), stylize("Imprimir Datos", azul)), time.sleep(0.3)
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
        dar_de_baja(matriz_trabajadores, df_trabajadores)
    elif (opcion == 3):
        consultar_trabajador(matriz_trabajadores, df_trabajadores)
    elif (opcion == 4):
        obtener_liquidacion()
    elif (opcion == 5):
        imprimir_data(df_trabajadores)
    else:
        corriendo = finalizar_programa(morado, azul)

time.sleep(1.5)
print("Hasta pronto!")