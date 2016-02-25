## ---- Tut02-estadisticaDescriptiva
########################################################
# www.postdata-statistics.com
# POSTDATA. Introducción a la Estadística
# Tutorial 02.  
# Plantilla de comandos Python para Estadística Descriptiva
# Una variable cuantitativa discreta, datos no agrupados.
########################################################


# ATENCION: para que este fichero funcione es NECESARIO: 
# (1) tener en cuenta la estructura de directorios como se explica en el tutorial. 
# (2) introducir el nombre del fichero de datos como argumento de read_csv.

## ---- Importacion de Modulos

import pandas as pd # read_csv, 
import numpy as np # cumsum, ptp, mean, var, std, median, percentile
import matplotlib.pyplot as plt # boxplot, setp, show, bar, hist
import collections as cl # Counter


## ---- Preliminares

linea = "_" * 75

print(linea)
print(linea)
print("www.postdata-statistics.com")
print("Curso de introducción a la Estadística. Tutorial02 (versión Python).")
print("Estadística descriptiva. Una variable cuantitativa discreta,\n datos no agrupados.")
print(linea)
print(linea)

## ---- Lectura de los datos

# Lectura de los datos:
# INTRODUCIR EL NOMBRE DEL FICHERO DE DATOS EN LA SIGUIENTE LINEA:
# EL FICHERO DEBE RESIDIR EN LA CARPETA DATOS DEL DIR. DE TRABAJO
nombreFichero = "Tut02-var3.csv"
datos = pd.read_csv("../../datos/" + nombreFichero, names=["v"])
datos = datos["v"].tolist()

print("El fichero de datos es:")
print(nombreFichero)

n = len(datos)
print("El número de datos leídos es:")
print(n)

print("Los primeros 10 datos son:")
print(datos[:10])
print("Los últimos 10 datos son:")
print(datos[-10:])

print(linea)

## ---- Recorrido
## Recorrido de una lista de números.  

print("El mínimo y máximo de los datos determinan el recorrido:")
print("Mínimo:")
print(min(datos))

print("Máximo:")
print(max(datos))

print("La anchura del recorrido (max - min) es:")

print(max(datos) - min(datos)) 

print(linea)

## ---- Tablas de frecuencia

## ---- Tabla de frecuencias absolutas

datos_counter = cl.Counter(datos)
tablaFreqAbs = datos_counter.most_common()
tablaFreqAbs.sort()	

## ---- Valores unicos y sus frecuencias

valoresUnicos = [ item[0] for item in tablaFreqAbs]
freqAbs = [ item[1] for item in tablaFreqAbs]


## ---- Tabla de frecuencias relativas

freqRel = [ item/n for item in freqAbs]


## ---- Tabla de frecuencias acumuladas

freqAcu = np.cumsum(freqAbs).tolist()

## ---- Tabla de frecuencias acumuladas relativas 

freqAcuRel = [ item/n for item in freqAcu]


## ---- Se muestra una tabla con todas las frecuencias

k = len(valoresUnicos)
print("\nTablas de frecuencias:\n") 
linea = "_" * 75
print(linea)
print("Valor | Frec. absoluta | Frec. relativa | Frec. acumulada | Frec. rel. ac. |")
print(linea)
for i in range(0,k):
    print("{0:5.3g} | {1:14.3g} | {2:14.3f} |{3:16.3g} |{4:15.3g} |\
    ".format(valoresUnicos[i], freqAbs[i], freqRel[i], freqAcu[i], freqAcuRel[i]))
print(linea)    

## ---- Medidas de posición: mediana, cuartiles y percentiles. Rango intercuartílico.

## ---- Mediana

print("Mediana:")
print(np.median(datos))

## ---- Cuartiles y percentiles
print("Percentiles 0, 25, 50, 75, 100:")
print(list(np.percentile(datos, [0, 25, 50, 75, 100])))

## ---- Recorrido intercuartilico
IQR = np.percentile(datos, 75) - np.percentile(datos, 25)
print("Recorrido intercuartílico:")
print(IQR)

print(linea)


## ---- Graficos

#get_ipython().magic('matplotlib inline')

## ---- Boxplot

print("Diagrama de cajas (boxplot):")
plt.boxplot(datos)
plt.show()

## ---- Diagrama de barras

print("Diagrama de barras a partir de la tabla de frecuencias:")
posiciones = valoresUnicos
alturas = freqAbs
plt.bar(posiciones, alturas, color='tan')
plt.show()

## ---- Histograma

print("Histograma:")
plt.hist(datos, bins=len(valoresUnicos), color='tan')
plt.show()

print(linea)

## ---- Media aritmetica y medidas de dispersion.

## ---- Media aritmetica

print("Media aritmética:")
mediaAritmetica = np.mean(datos)
print(mediaAritmetica)

## ---- Varianza Poblacional

print("Varianza poblacional")
varPoblacional = np.var(datos, ddof=0)
print(varPoblacional)

## ---- Cuasiarianza muestral

print("Cuasivarianza muestral")
cuasivarMuestral = np.var(datos, ddof=1)
print(cuasivarMuestral)

## ---- Desviacion tipica poblacional

print("Desviación típica poblacional")
desvestPoblacional = np.std(datos, ddof=0)
print(desvestPoblacional)

## ---- Cuasidesviacion tipica muestral

print("Cuasidesviación típica muestral")
cuasidesvestMuestral = np.std(datos, ddof=1)
print(cuasidesvestMuestral)

print(linea)



