## ---- Tut02-mediaVarianza-02
########################################################
# www.postdata -statistics.com
# POSTDATA. Introducción a la Estadística
# Tutorial 02 (versión Python).
# Ejemplo de cálculo de media, varianza y desv. típica
# para una variable cuantitativa, datos no agrupados.
########################################################

import math as m

# Esta es la lista de datos sobre la que vamos a trabajar:
edades = [22, 21, 18, 19, 17, 21, 18, 20, 17, 18, 17, 22, 20, 19, 18, 19, 18, 22, 
20, 19, 22, 18, 20, 21, 20]

# La lista se muestra en pantalla:
print("La lista de edades es:")
print(edades)

# Media aritmética de la lista:
mediaAritmetica = sum(edades) / len(edades)
print("La media aritmética es:")
print(mediaAritmetica)

# Varianza poblacional de la lista
terminosVarianza = []
for edad in edades:
  # Terminos varianza acumula resultados parciales del numerador de la 
  # varianza en cada iteración del bucle for.
  terminosVarianza = terminosVarianza + [(edad - mediaAritmetica)**2] 
varianzaPob = sum(terminosVarianza) / len(edades)
print("La varianza poblacional es:")
print(varianzaPob)

# Desviación típica poblacional.
print("La desviación típica poblacional es:")
print(m.sqrt(varianzaPob))