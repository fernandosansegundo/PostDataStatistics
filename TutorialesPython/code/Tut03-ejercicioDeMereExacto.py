# -*- coding: utf-8 -*-
"""
www.postdata-statistics.com
POSTDATA. Introducción a la Estadística
Tutorial 03.
Fichero de comandos Python para obtener
el resultado exacto del primer juego
del caballero de Mere.
"""

# Importamos el módulo itertools.
import itertools as it

# Generamos la lista de tiradas posibles.
tiradas = list(it.product(range(1, 7), repeat=4))


# Mostramos las primeras 10 y las últimas 10:
print("Primeras 10 tiradas:")
print(tiradas[0:10])
print("y las 10 últimas:")
print(tiradas[-10:])

print("El número de tiradas posibles es")
posibles = len(tiradas)
print(posibles)
print("que coincide con el valor teórico 6**4")
print(6**4)


# Obtenemos una lista de booleanos que caracteriza a las partidas ganadoras
# que son las que contienen al menos un 6.
 
tiradasGanadoras = []
for tirada in tiradas:
    if 6 in tirada:
        tiradasGanadoras.append(True)
    else:
        tiradasGanadoras.append(False)

# Número de partidas ganadoras:
print("El número de partidas ganadoras es:")
favorables = sum(tiradasGanadoras)
print(favorables)

# Proporcion de partidas ganadoras
print("Así que la probabilidad calculada por la regla de Laplace es la fracción:")
print("{0}/{1}".format(favorables, posibles))
print("que es aproximadamente igual a ")
print(favorables/posibles)
