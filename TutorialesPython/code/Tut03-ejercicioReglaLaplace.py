# -*- coding: utf-8 -*-
"""
www.postdata-statistics.com
POSTDATA. Introducción a la Estadística
Tutorial 03.
Fichero de comandos Python para comprobar la
regla de Laplace en un juego en el que tiramos dos
veces un dado y queremos calcular la probabilidad del suceso
A =obtener al menos un seis en las dos tiradas.
"""

# Importamos el módulo random y usamos seed
import random as rnd

rnd.seed(2016)

# Fijamos el número n de partidas.
n = 10000

# Generamos la lista de partidas. 
# Cada partida es una lista de 2 numeros de 1 a 6.
partidas = []
for i in range(0, n):
  partida = []
  for j in range(0, 2):
    partida.append(rnd.randrange(1, 7))
  partidas.append(partida)

# Mostramos las primeras 5 partidas.
print("Estas son las cinco primeras partidas:")
print(partidas[0:5])

# Obtenemos una lista de booleanos que caracteriza a las partidas ganadoras
# que son las que contienen al menos un 6.
 
partidasGanadoras = []
for partida in partidas:
    if 6 in partida:
        partidasGanadoras.append(True)
    else:
        partidasGanadoras.append(False)

# Se muestran las 5 primeras para comprobar.
print("Y esta indica cuáles de esas cinco primeras partidas son ganadoras:")
print(partidasGanadoras[0:5])

# Tabla de frecuencia

import collections as cl
ganadorasCounter = cl.Counter(partidasGanadoras)
freqGanadoras = ganadorasCounter.most_common()
#print(freqGanadoras)

# El mismo resultado sumando booleanos:
print("El número de partidas ganadoras es:")
print(sum(partidasGanadoras))

# Proporcion de partidas ganadoras
print("Y supone una frecuencia relativa de partidas ganadoras igual a:")
proporcionGanadoras = sum(partidasGanadoras) / n
print(proporcionGanadoras)
print("El valor predicho por la reglad de Laplace es 11/36, que es aproximadamente =")
print(11/36)
print("mientras la probabilidad ingenua  predice 1/3, que es 0.333333.")
