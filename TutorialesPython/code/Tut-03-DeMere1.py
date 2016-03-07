# -*- coding: utf-8 -*-

## ---- Tut03-probabilidad
########################################################
# www.postdata-statistics.com
# POSTDATA. Introducción a la Estadística
# Tutorial 03.  
# Comandos Python del tutorial03
# para simular el primer juego del
# Caballero de Mere.
########################################################


# Importacion de modulos 

import random as rnd
import collections as cl


# Generamos la lista de n partidas de cuatro tiradas de un dado

n = 1000

rnd.seed(2016)
partidas = []
for i in range(0, n):
    partida = []
    for j in range(0, 4):
        partida.append(rnd.randrange(1, 7))
    partidas.append(partida)

 # Se muestran las 10 primeras

print(partidas[0:10])

# Las mismas partidas, generadas de otra manera

rnd.seed(2016)
partidas = [[rnd.randrange(1, 7) for _ in range(0, 4)] for _ in range(0, n) ]

# Comprobacion de que son las mismas
print(partidas[0:10])

# Obtenemos una lista de booleanos que caracteriza a las partidas ganadoras
# que son las que contienen al menos un 6.
 
partidasGanadoras = []
for partida in partidas:
    if 6 in partida:
        partidasGanadoras.append(True)
    else:
        partidasGanadoras.append(False)

# Se muestran las 10 primeras para comprobar.

print(partidasGanadoras[0:10])

# Tabla de frecuencia

ganadorasCounter = cl.Counter(partidasGanadoras)
freqGanadoras = ganadorasCounter.most_common()
print(freqGanadoras)


# Proporcion de partidas ganadoras

proporcionGanadoras = sum(partidasGanadoras) / n
print(proporcionGanadoras)