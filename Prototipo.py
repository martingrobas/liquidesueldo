# PRIMERA PARTE - IMPORTACIONES
#------ Se hacen los importes necesarios ------#
# PRIMERA PARTE - IMPORTACIONES
#------ Se hacen los importes necesarios ------#
import time
import random
import colored
from funcs import *
import pandas as pd
from datetime import datetime, date
from colored import stylize
from num2words import num2words



# SEGUNDA PARTE - LECTURA DE DATOS INICIALES
#------ Carga de datos ------#
df_categorias = pd.read_csv('./csv_files/categorias.csv', sep=',') 
df_trabajadores = pd.read_csv('./csv_files/trabajadores.csv', sep=',')
df_planilla_salarial = pd.read_csv('./csv_files/planilla_salarial.csv', sep=',')
df_neto = pd.read_csv('./csv_files/neto.csv', sep=',')
matriz_neto = df_neto.values.tolist()
matriz_trabajadores = df_trabajadores.values.tolist()
matriz_planilla_salarial = df_planilla_salarial.values.tolist()
matriz_categorias = df_categorias.values.tolist()
lista_datos = ['Legajo', 'Nombre', 'Sexo', 'DNI', 'CUIL', 'Fecha Ingreso', 'Antiguedad', 'Nacimiento', 'Edad', 'Horas extras 50%', 'Horas extras 100%', 'Presentismo', 'Vacaciones', 'Estado Civil', 'Hijos', 'Puesto', 'Básico']


# Opción 1
def agregar_trabajador(matriz_trabajadores, matriz_categorias, df_trabajadores, azul, morado):
    time.sleep(1.5)
    trabajador = []

    # Dato principal
    legajo=int(input("Ingrese el legajo del trabajador: "))
    existe_trabajador = verificar_existencia(legajo)
    while existe_trabajador:
        legajo=int(input("El legajo ya pertenece a otro trabajador, por favor ingrese uno nuevo: "))
        existe_trabajador = verificar_existencia(legajo)
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
    existe_trabajador = verificar_existencia(dni)
    while existe_trabajador:
        dni=int(input("Esa persona ya se encuentra registrada, por favor ingrese nuevamente el DNI: "))
        existe_trabajador = verificar_existencia(dni)
    trabajador.append(dni)

    cuil = obtener_cuil(sexo, dni)
    trabajador.append(cuil)

    fecha_ingreso = input("Indique la fecha de ingreso a la empresa (D-M-AAAA): ")
    ingreso_correcto = verificar_fecha(fecha_ingreso, date.today())
    while not ingreso_correcto:
        print('No ingresó una fecha válida')
        fecha_ingreso = input("Introduzca la fecha de ingreso a la empresa (D-M-AAAA): ")
        ingreso_correcto = verificar_fecha(fecha_ingreso, date.today())
    trabajador.append(fecha_ingreso)
    
    fecha_ingreso = fecha_ingreso.split('-')
    antiguedad = calcular_diferencia(date(int(fecha_ingreso[2]), int(fecha_ingreso[1]), int(fecha_ingreso[0])), date.today())
    trabajador.append(antiguedad)
    
    birthday = input("Ingrese la fecha de nacimiento (D-M-AAAA): ")
    cumple = verificar_fecha(birthday, date.today())
    while not cumple:
        print('No ingresó una fecha válida')
        birthday = input("Ingrese la fecha de nacimiento (D-M-AAAA): ")
        cumple = verificar_fecha(birthday, date.today())
    trabajador.append(birthday)
        
    birthday = birthday.split('-')
    edad = calcular_diferencia(date(int(birthday[2]), int(birthday[1]), int(birthday[0])), date.today())
    trabajador.append(edad) 

    horas_extras_50 = input("Indique las horas extras totales del trabajador al 50%: ")
    trabajador.append(horas_extras_50)

        
    horas_extras_100 = input("Indique las horas extras totales del trabajador al 100%: ")
    trabajador.append(horas_extras_100)

    presentismo = input("Ingrese 's' para indicar que cumplió con el presentismo, o 'n' para indicar que no: ").upper()
    presentismo = verificar_letras_ingresadas(presentismo, 'S', 'N')
    trabajador.append(presentismo)

    vacaciones = int(input("Ingrese la cantidad de días de vacaciones del trabajador: "))
    while (vacaciones < 0) or (vacaciones > 14):
        print('No ingresó un número válido, este debe ser un entero positivo y no mayor a catorce')
        vacaciones= int(input("Ingrese la cantidad de días de vacaciones del trabajador: "))
    trabajador.append(vacaciones)

    estado_civil = input("Ingrese 'c' para indicar que esta casado, o 's' para soltero: ").upper()
    estado_civil_ = verificar_letras_ingresadas(estado_civil, 'C', 'S')
    trabajador.append(estado_civil_)

    hijos = input("Ingrese 's' para indicar que si tiene hijos, o 'n' para indicar que no: ").upper()
    hijos_ = verificar_letras_ingresadas(hijos, 'S', 'N')
    trabajador.append(hijos_)

    puesto, basico = solicitar_puesto(matriz_categorias, azul, morado)
    trabajador.append(puesto)
    trabajador.append(basico)

    matriz_trabajadores.append(trabajador)
    df_trabajadores = pd.DataFrame(matriz_trabajadores)
    df_trabajadores.to_csv(r"./csv_files/trabajadores.csv", sep=',', index=False)

    time.sleep(1)
    print("Trabajador agregado con éxito, a continuación será llevado al menu principal")
    print()
    time.sleep(3.5)


# Opción 2 
def dar_de_baja(df_trabajadores):
    time.sleep(1.5)
    dar_de_baja = int(input("ingrese el legajo del trabajador que desea dar de baja: "))
    
    try:
        df_trabajadores.drop(df_trabajadores.loc[df_trabajadores['Legajo'] == dar_de_baja].index, inplace=True)
        print("El trabajador ya no se encuentra dentro de los registros")
    except:
        time.sleep(1)
        print("No se pudo dar de baja al trabajador")
        print("Por favor intente de nuevo y verifique que el legajo sea correcto")
    finally:
        time.sleep(1)
        print()
        print("A continuación será llevado de regreso al menú principal")
        print()
        time.sleep(3.5)

# Opción 3
def consultar_trabajador(matriz_trabajadores, df_trabajadores):
    time.sleep(1.5)
    legajo = int(input("Ingrese el legajo del trabajador que desea consultar: "))
    print()

    df_trabajadores = pd.read_csv('./csv_files/trabajadores.csv', sep=',')
    matriz_trabajadores = df_trabajadores.values.tolist()
    
    for i in range(len(matriz_trabajadores)):
        if (legajo) == int(matriz_trabajadores[i][0]):
            time.sleep(1)
            print("El trabajador se encuentra dentro de los registros")
            print("Datos del trabajador")
            print(df_trabajadores.iloc[i, 0:])
            print(), time.sleep(1)
            print("A continuación será llevado de regreso al menú principal")
            print()
            time.sleep(3.5)
            break
    else:
        time.sleep(1)
        print("El trabajador no se encuentra dentro de los registros"), time.sleep(1.5)
        print("¿Desea volver a intentarlo?")
        print("Ingrese -1 para volver a intentar o 0 para continuar:")
        respuesta = int(input("Respuesta: "))
        
        while (respuesta != -1) and (respuesta != 0):
            print("Por favor ingrese -1 para volver a intentar o 0 para continuar:")
            respuesta = int(input('Respuesta: ')), time.sleep(0.5)
        
        if respuesta == -1:
            consultar_trabajador(matriz_trabajadores, df_trabajadores)
        else:
            print("Entendido, será llevado de regreso al menú principal.")
            print()
            time.sleep(3.5)


# Opción 4 
def editar_trabajador(matriz_trabajadores, df_trabajadores):
     
    time.sleep(1.5)
    legajo = int(input("Ingrese el legajo del trabajador del cual desea editar su información: "))
    print()

    trabajador = []

    for i in range(len(matriz_trabajadores)):
        if (legajo) == int(matriz_trabajadores[i][0]):
            for j in range(17):
                trabajador.append(matriz_trabajadores[i][j])

            print(len(trabajador))
            print(trabajador)
            time.sleep(1)
            print("El trabajador se encuentra dentro de los registros, a continuación se le solcitarán datos para editar su información."), time.sleep(0.3)
            print()

            horas_extras_50 = int(input("Ingrese las nuevas horas extras al 50 del trabajador: "))
            trabajador[9] = horas_extras_50

            horas_extras_100 = int(input("Ingrese las nuevas horas extras al 100 del trabajador: "))
            trabajador[10] = horas_extras_100

            presentismo=(input("Ingrese el nuevo presentismo 's' para indicar que posee o 'n' para indicar o contrario: ")).upper()
            presentismo = verificar_letras_ingresadas(presentismo, 'S', 'N')
            trabajador[11] = presentismo
            
            vacaciones = int(input("Ingrese la cantidad de días de vacaciones del trabajador: "))
            while (vacaciones < 0) or (vacaciones > 14):
                print('No ingresó un número válido, este debe ser un entero positivo y no mayor a catorce')
                vacaciones= int(input("Ingrese la cantidad de días de vacaciones del trabajador: ")) 
            trabajador[12] = vacaciones

            hijos = input("Ingrese 's' para indicar que si tiene hijos, o 'n' para indicar que no: ").upper()
            hijos_ = verificar_letras_ingresadas(hijos, 'S', 'N')
            trabajador[13] = hijos_

            matrix = matriz_trabajadores[:]
            matrix.remove(matriz_trabajadores[i])
            matriz_trabajadores = matrix
            matriz_trabajadores.append(trabajador)
            df_trabajadores = pd.DataFrame(matriz_trabajadores)
            df_trabajadores.to_csv(r"./csv_files/trabajadores.csv", sep=',', index=False)
            time.sleep(1)
            print("Trabajador modificado con éxito, a continuación será llevado al menú principal")
            print()
            time.sleep(3.5)

            break
    else:
        time.sleep(1)
        print("El trabajador no se encuentra dentro de los registros"), time.sleep(1.5)
        print("¿Desea volver a intentarlo?")
        print("Ingrese -1 para volver a intentar o 0 para continuar:")
        respuesta = int(input("Respuesta: "))
        
        while (respuesta != -1) and (respuesta != 0):
            print("Por favor ingrese -1 para volver a intentar o 0 para continuar:")
            respuesta = int(input('Respuesta: ')), time.sleep(0.5)
        
        if respuesta == -1:
            consultar_trabajador(matriz_trabajadores, df_trabajadores)
        else:
            print("Entendido, será llevado de regreso al menú principal.")
            print()
            time.sleep(3.5)



# Opción 5
def obtener_liquidacion(planilla_salarial, matriz_trabajadores, df_neto, matriz_neto, azul, morado):
    
    time.sleep(1.5)
    legajo = int(input("Ingrese el legajo del trabajador del cual desea obtener su liquidación: "))
    print()

    for i in range(len(matriz_trabajadores)):
        if (legajo) == int(matriz_trabajadores[i][0]):
            time.sleep(1)
            print("El trabajador se encuentra dentro de los registros, se procederá a calcular su liquidación."), time.sleep(0.3)

            antiguedad_total = int(matriz_trabajadores[i][6]) * float(planilla_salarial[7][1])
            # A fines prácticos, si se cumple con el presentismo se considerará un 10% del salario BASICO según categoría.

            if ((matriz_trabajadores[i][11]) == "S"):
                presentismo = float(matriz_trabajadores[i][16]) * 0.1
            else:
                presentismo = 0
            bruto_inicial = float(matriz_trabajadores[i][16]) + antiguedad_total + presentismo
            #El primer item es el que accede al dato del sueldo basico segun el rango del empleado.
            
            #Deducciones
            aporte_obra_social = bruto_inicial * 0.03
            jubilacion = bruto_inicial * 0.11
            aporte_obra_sindical = bruto_inicial * 0.02
    

            hs_ext_50 = ((bruto_inicial /240)*1.5) * int(matriz_trabajadores[i][9]) #(acceder al dato del CSV)
            hs_ext_100 = ((bruto_inicial / 240)*2) * int(matriz_trabajadores[i][10]) #(acceder al dato siguiente)
    
            bruto_total = bruto_inicial + hs_ext_50 + hs_ext_100 #(todo lo que gana sin descuentos)
            neto = bruto_total - jubilacion - aporte_obra_sindical - aporte_obra_social #(el sueldo real final)
            
            amarillo = colored.fg("yellow") + colored.attr("bold")
            verde = colored.fg("green") + colored.attr("bold")

            print(stylize("---------------- LIQUIDACIÓN DE SUELDO ------------", morado))
            print(stylize("Legajo: ", morado), stylize(f"{matriz_trabajadores[i][0]}", azul))
            print(stylize("Nombre y Apellido: ", morado), stylize(f"{matriz_trabajadores[i][1]}", azul))
            print(stylize("Sumas remunerativas:", morado))
            print(stylize(f"Básico               - - - - - - - - - - - -   ", azul), stylize(f"{round(matriz_trabajadores[i][16], 2)}", verde)), time.sleep(0.3)
            print(stylize(f"Antiguedad           - - - - - - - - - - - -   ", azul), stylize(f"{round(antiguedad_total, 2)}", verde)), time.sleep(0.3)
            print(stylize(f"Presentismo          - - - - - - - - - - - -   ", azul), stylize(f"{round(presentismo, 2)}", verde)), time.sleep(0.3)
            print(stylize(f"Horas extras al 50%  - - - - - - - - - - - -   ", azul), stylize(f"{round(hs_ext_50, 2)}", verde)), time.sleep(0.3)
            print(stylize(f"Horas extras al 100% - - - - - - - - - - - -   ", azul), stylize(f"{round(hs_ext_100, 2)}", verde)), time.sleep(0.3)
            print(stylize("Deducciones:", morado)), time.sleep(0.3)
            print(stylize(f"Jubilación           - - - - - - - - - - - -   ", azul), stylize(f"{round(jubilacion,2)}", amarillo)), time.sleep(0.3)
            print(stylize(f"Aporte Obra social   - - - - - - - - - - - -   ", azul), stylize(f"{round(aporte_obra_social, 2)}", amarillo)), time.sleep(0.3)
            print(stylize(f"Aporte Obra sindical - - - - - - - - - - - -   ", azul), stylize(f"{round(aporte_obra_sindical, 2)}", amarillo)), time.sleep(0.3)
            print()
            print(stylize(f"TOTAL NETO : {round(neto,2)}", azul)), time.sleep(0.3)
            print()
            print(stylize(f"Son en pesos: {(num2words(round(neto,2),to='currency', lang='es_CO'))}", morado))
            print()
            

            print(stylize("----------------------------------------------- ", morado)), time.sleep(1)

            lista_neto = [legajo, matriz_trabajadores[i][1], round(neto,2), datetime.today().month]
            matriz_neto.append(lista_neto)
            df_neto = pd.DataFrame(matriz_neto)
            df_neto.to_csv(r"./csv_files/neto.csv", sep=',', index=False)
            print("A continuación será llevado de regreso al menú principal")
            print()
            time.sleep(3.5)
            break
    else:
        time.sleep(1)
        print("El trabajador no se encuentra dentro de los registros"), time.sleep(1.5)
        print("¿Desea volver a intentarlo?")
        print("Ingrese -1 para volver a intentar o 0 para continuar:")
        respuesta = int(input("Respuesta: "))
        
        while (respuesta != -1) and (respuesta != 0):
            print("Por favor ingrese -1 para volver a intentar o 0 para continuar:")
            respuesta = int(input('Respuesta: ')), time.sleep(0.5)
        
        if respuesta == -1:
            obtener_liquidacion(matriz_planilla_salarial,matriz_trabajadores, df_neto, matriz_neto, azul, morado)
        else:
            print("Entendido, será llevado de regreso al menú principal.")
            print()
            time.sleep(3.5)


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
print(stylize("Bienvenido al programa de Liquidación de Sueldos", azul)), time.sleep(0.7)
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
        agregar_trabajador(matriz_trabajadores, matriz_categorias, azul, morado,df_trabajadores)  
    elif (opcion == 2):
        dar_de_baja(df_trabajadores)
    elif (opcion == 3):
        consultar_trabajador(matriz_trabajadores, df_trabajadores)
    elif (opcion == 4):
        editar_trabajador(matriz_trabajadores, df_trabajadores)
    elif (opcion == 5):
        obtener_liquidacion(matriz_planilla_salarial,matriz_trabajadores, df_neto, matriz_neto, azul, morado)
    elif (opcion == 6):
        imprimir_data(df_trabajadores)
    else:
        corriendo = finalizar_programa(morado, azul)

time.sleep(1.5)
print("Hasta pronto!")
print()