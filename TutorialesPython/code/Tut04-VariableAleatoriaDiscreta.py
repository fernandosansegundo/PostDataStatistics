## ---- Tut04-VariableAleatoriaDiscreta
########################################################
# www.postdata-statistics.com
# POSTDATA. Introducción a la Estadística
# Tutorial 04.  
# Plantilla de comandos Python para el estudio de 
# una variable aleatoria discreta.
########################################################

## Importacion de Modulos

import numpy as np 
import matplotlib.pyplot as plt
import math as m 


# Definicion de X a partir de valores y probabilidades.

valoresX = [2, 4, 7, 8, 11]
probabilidadesX = [1/5, 1/10, 1/10, 2/5, 1/5]
X = [[valoresX[_], probabilidadesX[_]] for _ in range(0, len(valoresX))]

# Alternativamente, definicion de la variable X como lista de pares [valor, probabilidad].
# Descomentar la siguiente linea para usarla.

# X = [[2, 1/5], [4, 1/10], [7, 1/10], [8, 2/5], [11, 1/5]]

# En cualquier caso:

valoresX = [x[0] for x in X]
probabilidadesX = [x[1] for x in X]

# Calculo de la media.

media = sum([x[0] * x[1] for x in X])
print("Media de X = {0:0.4f}".format(media))

# Calculo de la varianza y desviacion tipica.

varianza = sum([(x[0] - media)**2 * x[1] for x in X])
print("varianza = {0:0.4f}".format(varianza))

sigma = m.sqrt(varianza)
print("desviacion tipica = {0:0.4f}".format(sigma))

# Funcion de distribucion.

FdistX = np.cumsum(probabilidadesX).tolist()

# y su tabla:

k = len(valoresX)
print("\nTabla de la variable aleatoria X:\n")
linea = "_" * 49
print(linea)
print("| Valor x | Probabilidad p | Fun. de dist. F(x) |")
print(linea)
for i in range(0, k):
    print("| {0: 7d} | {1: 14.2f} | {2: 18.2f} |".format(valoresX[i],\
          probabilidadesX[i], FdistX[i]))
print(linea)

# Grafico de barras de la funcion de densidad.

plt.suptitle("Grafico de barras de la funcion de densidad:")
plt.xticks(valoresX)
plt.axis([min(valoresX) - 1,max(valoresX) + 1, 0, 1])
plt.bar(valoresX, probabilidadesX, color='tan', align='center')

#   Reset grafico.

plt.figure()

# Grafico de escalera de la funcion de distribucion.

plt.suptitle("Grafico de escalera de la funcion de distribucion:")
plt.xticks(valoresX)
plt.step([min(valoresX) - 2] + valoresX + [max(valoresX) + 1],
         [0] + FdistX + [1.00001], where='post', linewidth=4.0, color='red')
