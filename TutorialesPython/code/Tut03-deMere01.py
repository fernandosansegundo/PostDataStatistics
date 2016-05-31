## # -*- coding: utf-8 -*-
## """
## www.postdata-statistics.com
## POSTDATA. Introducción a la Estadística
## Tutorial 03.
## Fichero de comandos Python para simular el primer
## juego del Caballero de Mere.
## """
## 

# Importamos el módulo random y usamos seed
import random as rnd

rnd.seed(2016)

# Fijamos el número n de partidas.
n = 1000

# Generamos la lista de partidas. 
# Cada partida es una lista de cuatro numeros de 1 a 6.
partidas = []
for i in range(0, n):
  partida = []
  for j in range(0, 4):
    partida.append(rnd.randrange(1, 7))
  partidas.append(partida)

# Mostramos las primeras 5 partidas.
print(partidas[0:5])

# Generamos las mismas partidas con comprensión de listas.
# Empezamos reiniciando el generador pseudoaleatorio con seed.
rnd.seed(2016)

# Comprensión de listas:
partidas = [[rnd.randrange(1, 7) for _ in range(0, 4)] for _ in range(0, n) ]

# Y mostramos las 5 primeras para comprobar que coinciden:
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

print(partidasGanadoras[0:5])

# Tabla de frecuencia

import collections as cl
ganadorasCounter = cl.Counter(partidasGanadoras)
freqGanadoras = ganadorasCounter.most_common()
print(freqGanadoras)

# El mismo resultado sumando booleanos:

print(sum(partidasGanadoras))

# Proporcion de partidas ganadoras

proporcionGanadoras = sum(partidasGanadoras) / n
print(proporcionGanadoras)

