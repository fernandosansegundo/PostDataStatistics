## # -*- coding: utf-8 -*-
## """
## www.postdata-statistics.com
## POSTDATA. Introducción a la Estadística
## Tutorial 03.
## Fichero de comandos Python para simular el segundo
## juego del Caballero de Mere.
## """
## 

# Importamos el módulo random y usamos seed
import random as rnd

rnd.seed(2016)

# Fijamos el número n de partidas.
n = 1000

# Generamos la lista de partidas. 
# Cada partida es una lista de 24 numeros de 1 a 36.
partidas = []
for i in range(0, n):
  partida = []
  for j in range(0, 24):
    partida.append(rnd.randrange(1, 37))
  partidas.append(partida)

# Mostramos las primeras 5 partidas.
print("Estas son las cinco primeras partidas:")
print(partidas[0:5])

# Obtenemos una lista de booleanos que caracteriza a las partidas ganadoras
# que son las que contienen al menos un 6.
 
partidasGanadoras = []
for partida in partidas:
    if 36 in partida:
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

