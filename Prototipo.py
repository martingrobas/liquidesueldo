
"""Cosas que no deben faltar en la liquidación de sueldo:

Antiguedad
Sueldo basico (Tenemos que ver si es fijo o lo ingresamos por teclado.)
Obra social
Descuento ley 19032 (ver)
Descuento ley 23660 (ver)
Jubilación
Medicina prepaga
Presentismo (+)
Horas extras (+)
Direccion
Nacimiento
Datos filiatorios
DNI
CUIL
Fecha de ingreso
Escala salarial
Vacaciones
Soltero o Casado
Con o sin hijos
Aporte sindical, jubilatorio, etc
"""


# PRIMERA PARTE - IMPORTACIONES

#------Se hacen los importes necesarios, por ejemplo: ------#
import datetime
import pandas
import time
#import libreria para poner colores

legajo=int(input("Ingrese el legajo del empleado:\n"))
salariobruto=int(input("Indique el salario bruto:\n"))
nombre=input("Ingrese el nombre del empleado.\n")
años=int(input("Indique los años de antiguedad:\n"))
#medprepaga=input("¿Paga medicina prepaga?.S/N")

antiguedad=años*0.03
obrasocial=salariobruto*0.03
leyjub=salariobruto*0.03
salarioneto=salariobruto-antiguedad-obrasocial-leyjub
print("El salario neto del empleado",nombre,"con legajo",legajo,"es",round(salarioneto,2))



#ec = input("Ingrese su estado civil como 'c' para casado o 's' para soltero: ")
