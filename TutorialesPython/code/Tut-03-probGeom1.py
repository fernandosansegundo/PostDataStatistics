print("## ---- probGeom1ch001")
# n0 es el numero de subintervalos (puntos menos uno)

n0 = 100000

puntos = [ numero / n0 for  numero in range(0, n0 + 1)]

# imprimimos los primeros y los últimos puntos
print(puntos[0:5])
print(puntos[-5:])
print("## ---- probGeom1ch002")

# k es el numero de puntos elegidos

k = 10000

# importamos el módulo random y usamos seed para tener reproducibilidad

import random as rnd
rnd.seed(2016)

# y usamos choice con comprensión de listas para elegir k puntos

elegidos = [rnd.choice(puntos) for _ in range(0, k)]

# estos son los primeros 10 elegidos

print(elegidos[0:10])

print("## ---- probGeom1ch003")

enA = [punto for punto in elegidos if ((punto >= 2/3) and (punto<= 1))]

# comprobemos que funciona

print(enA[0:10])
print("## ---- probGeom1ch004")

# Ahora ya podemos calcular la proporción de puntos elegidos que pertenecen al intervalo:

proporcion = len(enA) / k
print(proporcion)

## dadoCargado = [1, 2, 3, 4, 5, 6, 6, 6]
