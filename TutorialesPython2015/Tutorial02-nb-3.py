
var3 = read_csv("../datos/Tut02-var3.csv", names=["v"])
var3 = var3["v"].tolist()
print(var3)

# ## Recorrido de una lista de números.  

min(var3)

max(var3)

np.ptp(var3) # max - min (peak to peak)

# ## Tablas de frecuencia.

from collections import Counter
var3_counter = Counter(var3)
freqVar3 = var3_counter.most_common()
print(freqVar3)

sorted(freqVar3)

# ## Gráficos.

get_ipython().magic('matplotlib inline')

import matplotlib.pyplot as plt
bpVar3 = plt.boxplot(var3, patch_artist=True)
plt.setp(bpVar3['boxes'], facecolor='tan')  
plt.show()

posiciones = [item[0] for item in sorted(freqVar3)]
print(posiciones)
alturas = [item[1] for item in sorted(freqVar3)]
print(alturas)
plt.bar(posiciones, alturas, align='center', color='tan')
plt.show()

plt.hist(var3, bins=15, color='tan')
plt.show()

# ## Media aritmética.

len(var3)

sum(var3)

mediaVar3 = sum(var3) / len(var3)
print(mediaVar3)

# ### Con NumPy.

np.mean(var3)

# ## Varianza y desviación típica (poblacional y muestral).

# ### Varianza Poblacional.

varPoblacional = sum([(valor - mediaVar3)**2 for valor in var3]) / len(var3)
print(varPoblacional)

# ### Varianza muestral.

varMuestral = sum([(valor - mediaVar3)**2 for valor in var3]) / (len(var3) - 1)
print(varMuestral)

# ### Desviación típica poblacional.

from math import sqrt
desvestPoblacional = sqrt(varPoblacional)
print(desvestPoblacional)

# ### Desviación típica muestral.

desvestMuestral = sqrt(varMuestral)
print(desvestMuestral)

# ### Con NumPy.

np.var(var3, ddof=1)

np.var(var3, ddof=0)

np.var(var3)

np.std(var3, ddof=1)

np.std(var3)

# ## Medidas de posición: mediana, cuartiles y percentiles. Rango intercuartílico.

# ## Mediana.

np.median(var3)

# ## Cuartiles y percentiles.

np.percentile(var3, 25)

list(np.percentile(var3, [0, 25, 50, 75, 100]))

IQR = np.percentile(var3, 75) - np.percentile(var3, 25)
print(IQR)

# # Ficheros de comandos Python. Comentarios.

# # Más operaciones con listas. 

# ## Números aleatorios.

import random
random.randint(1, 6)

dado100 = [random.randint(1, 6) for i in range(0, 100)]
print(dado100)

dado100_counter = Counter(dado100)
freqDado100 = dado100_counter.most_common()
sorted(freqDado100)

print(edades)
print(freqEdades)
import numpy
numpy.random.choice(edades, size=100, replace=True, p=None)

numpy.random.choice(edades, size=100, replace=True, p=None)

numpy.random.choice(edades, size=100, replace=True, p=None)

numpy.random.seed(seed=2016)
numpy.random.choice(edades, size=100, replace=True, p=None)

numpy.random.seed(seed=2016)
numpy.random.choice(edades, size=100, replace=True, p=None)

# ## Conjuntos.

set(edades)

datos = numpy.random.choice(range(1,100), size=100, replace=True, p=None)
print(sorted(datos))

print(set(datos))

import statistics as st
np.percentile(a, 25)

# ## Listas de cadenas de texto. 

list('hello')

import string
string.ascii_lowercase
string.ascii_uppercase
string.ascii_letters

numpy.random.seed(seed=2016)
letras = list(numpy.random.choice(list(string.ascii_lowercase), size=10, replace=True, p=None))
print(letras)

print(sorted(letras))

# # Valores booleanos y condiciones.

# ## El operador `==`.

sum([True, True, False, True, False, True, False, False, False, False, True, True, True])

# ## Selección de elementos de una lista mediante condiciones.

print(dado100)

numpy.random.seed(seed=2016)
mayoresQue3 = [valor for valor in dado100 if valor > 3]
print(mayoresQue3)
