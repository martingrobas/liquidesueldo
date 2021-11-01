import time
import random
import colored
from funcs import *
import pandas as pd
from datetime import datetime, date
from colored import stylize

# SEGUNDA PARTE - LECTURA DE DATOS INICIALES
#------ Carga de datos ------#
df_categorias = pd.read_csv("./csv_files/categorias.csv")
df_trabajadores = pd.read_csv("./csv_files/trabajadores.csv")
df_planilla_salarial = pd.read_csv("./csv_files/planilla_salarial.csv")
matriz_trabajadores = df_trabajadores.values.tolist()
matriz_planilla_salarial = df_planilla_salarial.values.tolist()
matriz_categorias = df_categorias.values.tolist()
lista_datos = ['Legajo', 'Nombre', 'Sexo', 'DNI', 'CUIL', 'Fecha Ingreso', 'Antiguedad', 'Nacimiento', 'Edad', 'Horas extra 50%', 'Horas extra 100%', 'Presentismo', 'Vacaciones', 'Estado Civil', 'Hijos', 'Puesto', 'Básico']


# TERCERA PARTE - FUNCIONES

def verificar_fecha(cad, fecha_actual):
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
    print("A continuacion se le mostrará los distintos puestos para que indique una opción"), time.sleep(0.7)
    print(stylize("Puestos: ", morado)), time.sleep(0.3)
    for i in range(len(categorias)):
        print(stylize(f" {i + 1}  -    ", morado), stylize(categorias[i][0], azul)), time.sleep(0.3)
    print()

    time.sleep(1)
    puesto = int(input("Por favor seleccione un número del 1 al 21 para indicar el puesto del trabajador: "))
    while puesto < 1 or puesto > 21:
        time.sleep(0.5)
        print()
        print("Error, ingresó un valor valido")
        puesto = int(input("Por favor seleccione un número del 1 al 21 para indicar el puesto del trabajador: "))

    puesto = categorias[puesto - 1][0]
    basico = int(categorias[puesto - 1][1])
    return puesto, basico
trabajadores_path = "trabajadores.csv"





# A PARTIR DE ACA ES LO DE MARTIN
def SetTrabajador(legajo, **datos):
    # setea los datos de un trabajador
    legajo = str(legajo)
    
    if TrabajadorExists(legajo):
        # modify only mentioned data in datos
        
        valid_datos = ["Nombre", "Sexo", "DNI", "CUIL", "Fecha", "Ingreso", "Fecha",
                       "Actual", "Nacimiento" , "Edad", "Horas extra 50%", "Horas extra 100%",
                       "Presentismo", "Escala Salarial", "Vacaciones" , "Estado Civil" ,"Hijos", "Puesto"]
        
        
        for key in datos.keys():
            if key not in valid_datos:
                print("Error: {} no es un dato valido".format(key))
                return False
            
        with open(trabajadores_path, "r") as trabajadores_file:
            trabajador_line = ""
            trabajadores = trabajadores_file.readlines()
            # obtener trabajador
            for trabajador in trabajadores:
                if legajo in trabajador:
                    trabajador_line = trabajador
                    break
                
            if trabajador_line == "":
                print("Error: el trabajador {} no existe".format(legajo))
                return False
                
            # obtener datos
            trabajador_datos = trabajador_line.split(",")
            # setear datos
            for key in datos.keys():
                trabajador_datos[valid_datos.index(key) + 1] = datos[key]
            
            
            # reescribir trabajador
            trabajadores[trabajadores.index(trabajador_line)] = ",".join(trabajador_datos)

            with open(trabajadores_path, "w") as trabajadores_file:
                trabajadores_file.writelines(trabajadores)

            return True
        
    else:
        print("Error: el trabajador {} no existe".format(legajo))
        return False
      
def GetTrabajador(legajo, datos = []):
    legajo = str(legajo)
    
    if datos == []:
        # get all data
        with open(trabajadores_path, "r") as trabajadores_file:
            trabajadores = trabajadores_file.readlines()
            for trabajador in trabajadores:
                if legajo in trabajador:
                    trabajador_line = trabajador
                    break
            trabajador_datos = trabajador_line.split(",")
            trabajador_datos = [trabajador_datos[i].strip() for i in range(len(trabajador_datos))]
            return trabajador_datos
        
    else:
        gived_datos = []    
        
        valid_datos = {
             # key / indes
             "Nombre": 1, "Sexo" : 2, "DNI" : 3, "CUIL" : 4, "Fecha" : 5, "Ingreso" : 6, "Fecha" : 7,
            "Actual" :8, "Nacimiento" : 9, "Edad" : 10, "Horas extra 50%" : 11, "Horas extra 100%" : 12,
            "Presentismo" : 13, "Escala Salarial" : 14, "Vacaciones" : 15 , "Estado Civil" : 16 ,"Hijos" : 17,
            "Puesto" : 18
            }

        
        with open(trabajadores_path, "r") as trabajadores_file:
            trabajador_line = ""
            trabajadores = trabajadores_file.readlines()
            for trabajador in trabajadores:
                if legajo in trabajador:
                    trabajador_line = trabajador
                    break
                
            if trabajador_line == "":
                print("Error: el trabajador {} no existe".format(legajo))
                return False
                
            trabajador_datos = trabajador_line.split(",")
            trabajador_datos = [trabajador_datos[i].strip() for i in range(len(trabajador_datos))]
            
            
            for dato in datos:
                for key in valid_datos.keys():
                    if dato == key:
                        gived_datos.append(trabajador_datos[valid_datos[key]])
                        
            return gived_datos
    
def DeleteTrabajador(legajo):
    legajo = str(legajo)
    
    if TrabajadorExists(legajo):
        with open(trabajadores_path, "r") as trabajadores_file:
            trabajadores = trabajadores_file.readlines()
        for trabajador in trabajadores:
            if legajo in trabajador:
                trabajadores.remove(trabajador)
                break
            
        with open(trabajadores_path, "w") as trabajadores_file:
            trabajadores_file.writelines(trabajadores)
            
        return True
        
    else:
        print("Error: el trabajador {} no existe".format(legajo))
        return False
        
def CreateTrabajador(**datos):
    # crea un trabajador
    
    # captalize first letter of each word in datos
    for key in datos.keys():
        try:
            # si es un string
            if type(datos[key]) == str:
                datos[key] = datos[key].capitalize()
            else:
                # si es un int o float
                datos[key] = str(datos[key])
        except:
            pass
    
    valid_datos = {
             # key / indes
             "Nombre": 1, "Sexo" : 2, "DNI" : 3, "CUIL" : 4, "Fecha" : 5, "Ingreso" : 6, "Fecha" : 7,
            "Actual" :8, "Nacimiento" : 9, "Edad" : 10, "Horas extra 50%" : 11, "Horas extra 100%" : 12,
            "Presentismo" : 13, "Escala Salarial" : 14, "Vacaciones" : 15 , "Estado Civil" : 16 ,"Hijos" : 17,
            "Puesto" : 18
            }
    
    
    # check if trabajador have all data
    for key in valid_datos.keys():
        if key not in datos.keys():
            # replace with "No definido"
            datos[key] = "No definido"


    # resolve cuil = 20 or 27 if Sexo = M or F + DNI + random digit (1-9)
    if datos["Sexo"] == "M" or datos["Sexo"] == "m":
        datos["CUIL"] = "20" + datos["DNI"] + str(random.randint(1,9))
    elif datos["Sexo"] == "F" or datos["Sexo"] == "f":
        datos["CUIL"] = "27" + datos["DNI"] + str(random.randint(1,9))

    # format date
    datos["Fecha"] = datos["Fecha"].split("/")
    datos["Fecha"] = datos["Fecha"][2] + "-" + datos["Fecha"][1] + "-" + datos["Fecha"][0]

    # format date
    datos["Ingreso"] = datos["Ingreso"].split("/")
    datos["Ingreso"] = datos["Ingreso"][2] + "-" + datos["Ingreso"][1] + "-" + datos["Ingreso"][0]

    # format date actual date   
    date = datetime.datetime.now()
    datos["Actual"] = date.strftime("%m-%d-%y")
    
    # format date
    datos["Nacimiento"] = datos["Nacimiento"].split("/")
    datos["Nacimiento"] = datos["Nacimiento"][2] + "-" + datos["Nacimiento"][1] + "-" + datos["Nacimiento"][0]

    # create trabajador line
    trabajador_line = ""
    for key in datos.keys():
        trabajador_line += datos[key] + ","
    trabajador_line = trabajador_line[:-1]

                
    # add trabajador to file
    with open(trabajadores_path, "a") as trabajadores_file:
        trabajadores_file.write(trabajador_line + "\n")
