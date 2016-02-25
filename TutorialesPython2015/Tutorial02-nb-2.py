# In[ ]:

var3 = read_csv("../datos/Tut02-var3.csv", names=["v"])
var3 = var3["v"].tolist()
print(var3)


# ## Recorrido de una lista de números.  

# In[ ]:

min(var3)


# In[ ]:

max(var3)


# In[ ]:

np.ptp(var3) # max - min (peak to peak)


# ## Tablas de frecuencia.

# In[ ]:

from collections import Counter
var3_counter = Counter(var3)
freqVar3 = var3_counter.most_common()
print(freqVar3)


# In[ ]:

sorted(freqVar3)


# ## Gráficos.

# In[ ]:

get_ipython().magic('matplotlib inline')


# In[ ]:

import matplotlib.pyplot as plt
bpVar3 = plt.boxplot(var3, patch_artist=True)
plt.setp(bpVar3['boxes'], facecolor='tan')  
plt.show()


# In[ ]:

posiciones = [item[0] for item in sorted(freqVar3)]
print(posiciones)
alturas = [item[1] for item in sorted(freqVar3)]
print(alturas)
plt.bar(posiciones, alturas, align='center', color='tan')
plt.show()


# In[ ]:

plt.hist(var3, bins=15, color='tan')
plt.show()


# In[ ]:




# ## Media aritmética.

# In[ ]:

len(var3)


# In[ ]:

sum(var3)


# In[ ]:

mediaVar3 = sum(var3) / len(var3)
print(mediaVar3)


# ### Con NumPy.

# In[ ]:

np.mean(var3)


# ## Varianza y desviación típica (poblacional y muestral).

# ### Varianza Poblacional.

# In[ ]:

varPoblacional = sum([(valor - mediaVar3)**2 for valor in var3]) / len(var3)
print(varPoblacional)


# ### Varianza muestral.

# In[ ]:

varMuestral = sum([(valor - mediaVar3)**2 for valor in var3]) / (len(var3) - 1)
print(varMuestral)


# ### Desviación típica poblacional.

# In[ ]:

from math import sqrt
desvestPoblacional = sqrt(varPoblacional)
print(desvestPoblacional)


# ### Desviación típica muestral.

# In[ ]:

desvestMuestral = sqrt(varMuestral)
print(desvestMuestral)


# ### Con NumPy.

# In[ ]:

np.var(var3, ddof=1)


# In[ ]:

np.var(var3, ddof=0)


# In[ ]:

np.var(var3)


# In[ ]:

np.std(var3, ddof=1)


# In[ ]:

np.std(var3)


# ## Medidas de posición: mediana, cuartiles y percentiles. Rango intercuartílico.

# ## Mediana.

# In[ ]:

np.median(var3)


# ## Cuartiles y percentiles.

# In[ ]:

np.percentile(var3, 25)


# In[ ]:

list(np.percentile(var3, [0, 25, 50, 75, 100]))


# In[ ]:

IQR = np.percentile(var3, 75) - np.percentile(var3, 25)
print(IQR)


# In[ ]:




# # Ficheros de comandos Python. Comentarios.

# In[ ]:




# In[ ]:




# # Más operaciones con listas. 

# In[ ]:




# ## Números aleatorios.

# In[ ]:

import random
random.randint(1, 6)


# In[ ]:

dado100 = [random.randint(1, 6) for i in range(0, 100)]
print(dado100)


# In[ ]:

dado100_counter = Counter(dado100)
freqDado100 = dado100_counter.most_common()
sorted(freqDado100)


# In[ ]:

print(edades)
print(freqEdades)
import numpy
numpy.random.choice(edades, size=100, replace=True, p=None)


# In[ ]:

numpy.random.choice(edades, size=100, replace=True, p=None)


# In[ ]:

numpy.random.choice(edades, size=100, replace=True, p=None)


# In[ ]:

numpy.random.seed(seed=2016)
numpy.random.choice(edades, size=100, replace=True, p=None)


# In[ ]:

numpy.random.seed(seed=2016)
numpy.random.choice(edades, size=100, replace=True, p=None)


# ## Conjuntos.

# In[ ]:

set(edades)


# In[ ]:

datos = numpy.random.choice(range(1,100), size=100, replace=True, p=None)
print(sorted(datos))


# In[ ]:

print(set(datos))


# In[ ]:

import statistics as st
np.percentile(a, 25)


# In[ ]:




# ## Listas de cadenas de texto. 

# In[ ]:

list('hello')


# In[ ]:

import string
string.ascii_lowercase
string.ascii_uppercase
string.ascii_letters


# In[ ]:

numpy.random.seed(seed=2016)
letras = list(numpy.random.choice(list(string.ascii_lowercase), size=10, replace=True, p=None))
print(letras)


# In[ ]:

print(sorted(letras))


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# # Valores booleanos y condiciones.

# In[ ]:




# ## El operador `==`.

# In[ ]:




# ## Interpretación de `True` y `False` como 1 y 0 respectivamente.

# In[ ]:

sum([True, True, False, True, False, True, False, False, False, False, True, True, True])


# ## Selección de elementos de una lista mediante condiciones.

# In[ ]:

print(dado100)


# In[543]:

numpy.random.seed(seed=2016)
mayoresQue3 = [valor for valor in dado100 if valor > 3]
print(mayoresQue3)
