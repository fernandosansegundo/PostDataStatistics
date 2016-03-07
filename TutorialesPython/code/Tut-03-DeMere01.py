print("## ---- deMere01ch001")
import random as rnd

rnd.seed(2016)

n = 1000

partidas = []
for i in range(0, n):
  partida = []
  for j in range(0, 4):
    partida.append(rnd.randrange(1, 7))
  partidas.append(partida)
print(partidas[0:5])
print("## ---- deMere01ch002")

rnd.seed(2016)

partidas = [[rnd.randrange(1, 7) for _ in range(0, 4)] for _ in range(0, n) ]

print(partidas[0:5])
print("## ---- deMere01ch003")

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

print("## ---- deMere01ch004")

# Tabla de frecuencia

import collections as cl
ganadorasCounter = cl.Counter(partidasGanadoras)
freqGanadoras = ganadorasCounter.most_common()
print(freqGanadoras)

print("## ---- deMere01ch005")

print(sum(partidasGanadoras))

print("## ---- deMere01ch006")

# Proporcion de partidas ganadoras

proporcionGanadoras = sum(partidasGanadoras) / n
print(proporcionGanadoras)

## dadoCargado = [1, 2, 3, 4, 5, 6, 6, 6]
