# LIQUIDACIÓN DE SUELDOS

Para correr correctamente todo el programa entrar al carpeta y ejecutar "pip install -r requirements.txt"
Seguidamente, una vez instalado todo, para utilizar el programa haga "python Prototipo.py"

## PRIMERA PARTE - IMPORTACIONES

Se hacen los importes necesarios, por ejemplo: 
- para especificar la fecha de la liquidacion: import datetime
- para facilitar el manejo de las fechas, horas y pausas: import time
- al utilizar un csv file: import pandas
- para asignar colores: import colored


## SEGUNDA PARTE - LECTURA DE DATOS INICIALES

Se lee los archivos de texto o los csv files (esto se guarda en una variable)
Se encuentra en forma de matriz u organizado en listas


## TERCERA PARTE - FUNCIONES

- Función para imprimir todos los trabajadores que se encuentran registrados (ordenada y legible)
- Función para editar datos si se encuentra un trabajador en específico dentro del registro
- Función para consultar si se encuentra un trabajador en específico dentro del registro
- Función para agregar a un trabajador al registro
- Función para eliminar a un trabajador del registro
- Función para obtener la liquidación de un trabajador en específico
- Función para solicitar la detención del programa



## CUARTA PARTE - PROGRAMA PRINCIPAL

Se inicia el programa y se muestran las opciones disponibles.
Dependiendo de la opción seleccionada se llama la función indicada
Finaliza el programa


## FORMATO DE EJEMPLO DE LA LIQUIDACIÓN

---------------- LIQUIDACIÓN DE SUELDO ------------
Legajo:  1234
Nombre y Apellido:  Marcelo Parma
Sumas remunerativas:
Básico               - - - - - - - - - - - -    35968
Antiguedad           - - - - - - - - - - - -    32832.8
Presentismo          - - - - - - - - - - - -    3596.8
Horas extras al 50%  - - - - - - - - - - - -    2262.43
Horas extras al 100% - - - - - - - - - - - -    3016.57
Deducciones:
Jubilación           - - - - - - - - - - - -    8544.43
Aporte Obra social   - - - - - - - - - - - -    2330.3
Aporte Obra sindical - - - - - - - - - - - -    1553.53

TOTAL NETO : 65248.34

Son en pesos: sesenta y cinco mil doscientos cuarenta y ocho pesos y treinta y cuatro centavos

----------------------------------------------- 