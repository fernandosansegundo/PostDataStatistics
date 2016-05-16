"""
www.postdata -statistics.com
POSTDATA. Introducción a la Estadística.
Tutorial 02 (versión Python).
Ejemplo de cálculo de media, varianza y desv. típica
para una variable cuantitativa, datos no agrupados.
"""

import math as m

# Esta es la lista de datos sobre la que vamos a trabajar:
edades = [22, 21, 18, 19, 17, 21, 18, 20, 17, 18, 17, 22, 20, 19, 18, 19, 18, 22, 
20, 19, 22, 18, 20, 21, 20]

# La lista se muestra en pantalla:
print("La lista de edades es:")
print(edades)

# Media aritmética de la lista:
mediaEdad = sum(edades) / len(edades)
print("La media aritmética es:")
print(mediaEdad)

# Varianza poblacional de la lista
diferenciasCuad = []
# diferenciasCuad acumula resultados parciales del numerador de la 
# varianza en cada iteración del siguiente bucle for.
for edad in edades:
  diferencia = edad - mediaEdad
  cuadradoDif = diferencia**2
  diferenciasCuad = diferenciasCuad + [cuadradoDif]
varianzaPob = sum(diferenciasCuad) / len(edades)
print("La varianza poblacional es:")
print(varianzaPob)

# Desviación típica poblacional.
print("La desviación típica poblacional es:")
print(m.sqrt(varianzaPob))
