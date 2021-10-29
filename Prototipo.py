# PRIMERA PARTE - IMPORTACIONES
#------ Se hacen los importes necesarios ------#
import time
import random
import colored
import pandas as pd  # Hacer en la terminal pip install numpy y NumPy y luego pip install pandas
from datetime import datetime, date
from colored import stylize #Hacer en la terminal pip install termcolor

import datetime 

# SEGUNDA PARTE - LECTURA DE DATOS INICIALES
#------ Carga de datos ------#
df_categorias = pd.read_csv("categorias.csv")
df_trabajadores = pd.read_csv("trabajadores.csv")
df_planilla_salarial = pd.read_csv("planilla_salarial.csv")
matriz_trabajadores = df_trabajadores.values.tolist()
matriz_planilla_salarial = df_planilla_salarial.values.tolist()
matriz_categorias = df_categorias.values.tolist()


# TERCERA PARTE - FUNCIONES

def verificar_fecha(cad):
    fecha = cad.split("-") 
    year = int(fecha[2])
    print(year)
    month = int(fecha[1])
    print(month)
    day = int(fecha[0])
    print(day)

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

    elif (month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12) and (day > 31):
        es_valida = False

    elif (month == 4) or (month == 6) or (month == 9) or (month == 11) and (day > 30):
        es_valida = False
    
    return es_valida



def calcular_diferencia( menor_fecha, mayor_fecha ): 
    return (mayor_fecha.year - menor_fecha.year) + (1 if (mayor_fecha.day >= menor_fecha.day) and (mayor_fecha.month >= menor_fecha.month) else 0) 

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
    
def solicitar_puesto(categorias, azul, morado):
    time.sleep(1.5)
    
    print()
    print("A continuacion de le mostrará los distintos puestos para que indique una opciónÑ"), time.sleep(0.7)
    print(stylize("Puestos: ", morado)), time.sleep(0.3)
    for i in range(len(categorias)):
        print(stylize(f" {i}  -    ", morado), stylize(categorias[i][0], azul)), time.sleep(0.3)
    print()

    time.sleep(1)
    puesto = int(input("Por favor seleccione un número del 1 al 21 para indicar el puesto del trabajador: "))
    while puesto < 1 or puesto > 21:
        time.sleep(0.5)
        print()
        print("Error, ingresó un valor valido")
        puesto = int(input("Por favor seleccione un número del 1 al 21 para indicar el puesto del trabajador: "))

    puesto = categorias[puesto - 1][0]
    return puesto



# Opción 1
def agregar_trabajador(matriz_trabajadores, matriz_categorias, azul, morado):
    time.sleep(1.5)
    trabajador = []

    # Dato principal
    legajo=int(input("Ingrese el legajo del trabajador: "))
    trabajador.append(legajo)

    # Nombres
    nombre = input("Ingrese el nombre y apellido: ")
    trabajador.append(nombre)
    
    # Letras
    sexo = input("Ingrese 'f' para femenino o 'm' para masculino: ").upper()
    sexo = verificar_letras_ingresadas(sexo, 'F', 'M')
    trabajador.append(sexo)
    

    #Numeros

    dni=int(input("Ingrese el DNI: "))
    trabajador.append(dni)

    cuil = obtener_cuil(sexo, dni)
    trabajador.append(cuil)

    fecha_ingreso = input("Indique la fecha de ingreso a la empresa (DD-MM-AAAA): ")
    ingreso_correcto = verificar_fecha(fecha_ingreso)
    while not ingreso_correcto:
        print('No ingresó una fecha válida')
        fecha_ingreso = input("Introduzca la fecha de ingreso a la empresa (DD-MM-AAAA): ")
        ingreso_correcto = verificar_fecha(fecha_ingreso)
    trabajador.append(fecha_ingreso)
    
    fecha_ingreso = fecha_ingreso.split('-')
    antiguedad = calcular_diferencia(date(int(fecha_ingreso[2]), int(fecha_ingreso[1]), int(fecha_ingreso[0])), datetime.date.today())
    trabajador.append(antiguedad)
    print(trabajador)
    
    birthday = input("Ingrese la fecha de nacimiento (DD-MM-AAAA): ")
    cumple = verificar_fecha(birthday)
    while not cumple:
        print('No ingresó una fecha válida')
        birthday = input("Ingrese la fecha de nacimiento (DD-MM-AAAA): ")
        cumple = verificar_fecha(birthday)
    trabajador.append(birthday)
        
    edad = calcular_diferencia(date(int(birthday[2]), int(birthday[1]), int(birthday[0])), datetime.date.today())
    trabajador.append(edad) 
    print(trabajador)

    horas_extras_50 = input("Indique las horas extras totales del trabajador al 50%: ")
    trabajador.append(horas_extras_50)

        
    horas_extras_100 = input("Indique las horas extras totales del trabajador al 100%: ")
    trabajador.append(horas_extras_100)

    presentismo = input("Ingrese 's' para indicar que posee presentismo, o 'n' para indicar que no posee: ").upper()
    presentismo = verificar_letras_ingresadas(presentismo, 'S', 'N')
    trabajador.append(presentismo)

    vacaciones = input("Ingrese la cantidad de dias de vacaciones del trabajador: ")
    while (vacaciones < 0) or (vacaciones > 100):
        print('No ingresó un numero valido, este debe ser un entero positivo y no mayor a cien')
        vacaciones= input("Ingrese la cantidad de dias de vacaciones del trabajador: ")
    trabajador.append(vacaciones)

    estado_civil = input("Ingrese 'c' para indicar que esta casado, o 's' para soltero: ").upper()
    estado_civil_ = verificar_letras_ingresadas(estado_civil, 'C', 'S')
    trabajador.append(estado_civil_)

    hijos = input("Ingrese 's' para indicar si tiene hijos, o 'n' para indicar que no: ").upper()
    hijos_ = verificar_letras_ingresadas(hijos, 'S', 'N')
    trabajador.append(hijos_)

    puesto = solicitar_puesto(matriz_categorias, azul, morado)
    trabajador.append(puesto)

    matriz_trabajadores.append(trabajador)
    df_trabajadores = pd.DataFrame(matriz_trabajadores)

    time.sleep(1)
    print("Trabajador agregado con éxito, a continuación será llevado al menu principal")
    print()
    time.sleep(3.5)


# Opción 2 
def dar_de_baja(matriz_trabajadores,df_trabajadores):
    time.sleep(1.5)
    darDeBaja=int(input("ingrese el legajo del trabajador que desea dar de baja"))

    try:
        matriz_trabajadores = df_trabajadores.drop(df_trabajadores.loc[df_trabajadores['Legajo'] == darDeBaja].index, inplace=True)
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

    for i in range(len(matriz_trabajadores)):
        if (legajo) == int(matriz_trabajadores[i][0]):
            time.sleep(1)
            print("El trabajador se encuentra dentro de los registros")
            print("Datos del trabajador")
            print(df_trabajadores.iloc[i, 0:])
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
            print("Por favor ingrese -1 para volver a intentar o 0 para continuar:")
            respuesta = int(input('Respuesta: ')), time.sleep(0.5)
        
        if respuesta == -1:
            consultar_trabajador(matriz_trabajadores, df_trabajadores)
        else:
            print("Entendido, será llevado de regreso al menú principal")
            print()
            time.sleep(3.5)


# Opción 4 
def editar_trabajador(matriz_trabajadores):
    trabajador = []

    ingresarlegajo=input(int("Ingrese el legajo del trabajador que desea modificar: "))

    
    time.sleep(1.5)

    '''
    matriz_trabajadores.append(trabajador)
    df_trabajadores = pandas.DataFrame(matriz_trabajadores)

    time.sleep(1)
    print("Trabajador modificado con exito, a continuacion sera llevado al menu principal")
    print()
    time.sleep(3.5)'''

    print("opción 4")


# Opción 5
def obtener_liquidacion(matriz_planilla_salarial):
    """
    
    
    Tengo que ver si la jubilacion y aporte obra social, cuota sindical se multiplican por el bruto 
    inicial o por el bruto total HOLA MARTINNNNNNNNNN
    
    aporte_obra_social = bruto * 0.03
    jubilacion= bruto * 0,11
    aporte_obra_sindical= bruto * 0.02
    antiguedad_total= antiguedad * int(matriz_planilla_salarial[8][1])

    bruto_inicial = basico (aca hay que acceder al dato del sueldo segun el rango del empleado) + antiguedad_total + presentismo 
    hs_ext_50 = (bruto_inicial /240) * horas_extras_50
    hs_ext_100 = (bruto_inicial / 240) * horas_extras_100
    
    bruto_total = bruto_inicial + hs_ext_50 + hs_ext_100
    neto = bruto_total - jubilacion - aporte_obra_sindical - aporte_obra_social
    """
    print("opcion 5")


# Opción 6
def imprimir_data(data_frame):
    time.sleep(1.5)
    print(data_frame)
    print()
    print("A continuación será llevado de regreso al menú principal")
    print()
    time.sleep(3.5)


# Opción 7
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
    print(stylize(" 4  -    ", morado), stylize("Editar Trabajador", azul)), time.sleep(0.3)
    print(stylize(" 5  -    ", morado), stylize("Obtener una Liquidación", azul)), time.sleep(0.3)
    print(stylize(" 6  -    ", morado), stylize("Imprimir Datos", azul)), time.sleep(0.3)
    print(stylize(" 7  -    ", morado), stylize("Detener Programa", azul))    , time.sleep(0.8)

    print()
    opcion = int(input("Por favor seleccione una opción: "))
    print()
    
    while (opcion < 1) or (opcion > 7):
        print()
        print("Opción no válida")
        opcion = int(input("Por favor indique su opción a seleccionar (entre 1 y 6): "))

    if (opcion == 1):
        agregar_trabajador(matriz_trabajadores, matriz_categorias, azul, morado)  
    elif (opcion == 2):
        dar_de_baja(matriz_trabajadores, df_trabajadores)
    elif (opcion == 3):
        consultar_trabajador(matriz_trabajadores, df_trabajadores)
    elif (opcion == 4):
        editar_trabajador(matriz_planilla_salarial)
    elif (opcion == 5):
        obtener_liquidacion(matriz_planilla_salarial)
    elif (opcion == 6):
        imprimir_data(df_trabajadores)
    else:
        corriendo = finalizar_programa(morado, azul)

time.sleep(1.5)
print("Hasta pronto!")