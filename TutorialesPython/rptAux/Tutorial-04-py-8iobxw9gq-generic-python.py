print('## ---- generic-python-chunk-0001') 
dado1 = range(1,7) 
print(list(dado1))
print('## ---- generic-python-chunk-0002') 
dado2 = range(1,7)
print('## ---- generic-python-chunk-0003') 
suma = [d1 + d2 for d1 in dado1 for d2 in dado2] 
print(suma)
print('## ---- generic-python-chunk-0004') 
import collections as cl 
sumaCounter = cl.Counter(suma) 
recuentoValoresSuma = sumaCounter.most_common() 
recuentoValoresSuma.sort() 
print(recuentoValoresSuma)
print('## ---- generic-python-chunk-0005') 
n = len(suma) 
print("n=", n) 
probabilidadesSuma = [[item[0], item[1]/n] for item in recuentoValoresSuma] 
print("probabilidadesSuma=", probabilidadesSuma)
print('## ---- generic-python-chunk-0006') 
print(4/36)
print('## ---- generic-python-chunk-0007') 
# Definicion de la variable X. 
X = [[2, 1/5], [4, 1/10], [7, 1/10], [8, 2/5], [11, 1/5]]
print('## ---- generic-python-chunk-0008') 
# Calculo de la media. 
 
media = sum([x[0] * x[1] for x in X]) 
print("Media de X = {0:0.4f}".format(media)) 

print('## ---- generic-python-chunk-0009') 
import math as m
print('## ---- generic-python-chunk-0010') 
# Calculo de la varianza y desviacion tipica. 
 
varianza = sum([(x[0] - media)**2 * x[1] for x in X]) 
print("varianza = {0:0.4f}".format(varianza))
print('## ---- generic-python-chunk-0011') 
 
sigma = m.sqrt(varianza) 
print("desviacion tipica = {0:0.4f}".format(sigma)) 

print('## ---- generic-python-chunk-0012') 
import random as rnd 
rnd.seed(2016) 
n = 10000 
dado1 = [rnd.randrange(1, 7) for _ in range(0, n)] 
dado2 = [rnd.randrange(1, 7) for _ in range(0, n)] 
X = [dado1[_] + dado2[_] for _ in range(0, n)] 
W = [3 * x - 4 for x in X]
print('## ---- generic-python-chunk-0013') 
import numpy as np 
mediaW = np.mean(W) 
print("media de W= {0:0.4f}".format(mediaW))
print('## ---- generic-python-chunk-0014') 
V = [x**2 for x in X] 
mediaV = np.mean(V) 
print("media de V= {0:0.4f}".format(mediaV))
print('## ---- generic-python-chunk-0015') 
valoresX = range(2, 13) 
probabilidadesX = list(range(1,7)) + list(range(5, 0, -1)) 
probabilidadesX = [p/36 for p in probabilidadesX] 
muX = sum([valoresX[i] * probabilidadesX[i] for i in range(0, len(valoresX))]) 
print("Media de X = {0:0.4f}".format(muX)) 
varX = sum( [(valoresX[i] - muX)**2 * probabilidadesX[i] for i in range(0, len(valoresX))]) 
print("Varianza de X = {0:0.4f}".format(varX))
print('## ---- generic-python-chunk-0016') 
valoresV = [x**2 for x in valoresX] 
probabilidadesV = probabilidadesX 
muV = sum([valoresV[i] * probabilidadesV[i] for i in range(0, len(valoresV))]) 
print("Media de V = {0:0.4f}".format(muV))
print('## ---- generic-python-chunk-0017') 
print("varX ={0:0.4f}".format(varX)) 
print("muV - (muX)^2 ={0:0.4f}".format(muV - (muX)**2))
print('## ---- generic-python-chunk-0018') 
X = [[2, 1/5], [4, 1/10], [7, 1/10], [8, 2/5], [11, 1/5]] 
valoresX = [item[0] for item in X] 
probabilidadesX = [item[1] for item in X] 
print(probabilidadesX)
print('## ---- generic-python-chunk-0019') 
FdistX = np.cumsum(probabilidadesX).tolist() 
print(FdistX)
print('## ---- generic-python-chunk-0020') 
import matplotlib.pyplot as plt
print('## ---- generic-python-chunk-0021') 
# Grafico de barras de la funcion de densidad. 
 
plt.suptitle("Grafico de barras de la funcion de densidad:") 
plt.xticks(valoresX) 
plt.axis([min(valoresX) - 1,max(valoresX) + 1, 0, 1]) 
plt.bar(valoresX, probabilidadesX, color='tan', align='center') 

print('## ---- generic-python-chunk-0022') 
plt.savefig('../fig/Tut-04-py-01.png')
print('## ---- generic-python-chunk-0023') 
#   Reset grafico. 
 
plt.figure() 

print('## ---- generic-python-chunk-0024') 
# Grafico de escalera de la funcion de distribucion. 
 
plt.suptitle("Grafico de escalera de la funcion de distribucion:") 
plt.xticks(valoresX) 
plt.step([min(valoresX) - 2] + valoresX + [max(valoresX) + 1], 
         [0] + FdistX + [1.00001], where='post', linewidth=4.0, color='red')
print('## ---- generic-python-chunk-0025') 
plt.savefig('../fig/Tut-04-py-02.png')
print('## ---- generic-python-chunk-0026') 
import math as m
print('## ---- generic-python-chunk-0027') 
def esCuadrado(n): 
  """ 
  Devuelve True si el entero n es un cuadrado perfecto y False en caso contrario.   
  """ 
  raiz = m.sqrt(n) 
  raizRedondeada = round(raiz) 
  if(raizRedondeada**2 == n): 
    return(True) 
  else: 
    return(False)
print('## ---- generic-python-chunk-0028') 
import random as rnd 
rnd.seed(2016) 
n = 10000 
dado1 = [rnd.randrange(1, 7) for _ in range(0, n)] 
dado2 = [rnd.randrange(1, 7) for _ in range(0, n)] 
suma = [dado1[_] + dado2[_] for _ in range(0, n)] 
import collections as cl 
sumaCounter = cl.Counter(suma) 
freqAbsolutaSuma = sumaCounter.most_common() 
freqAbsolutaSuma.sort() 
print(freqAbsolutaSuma) 
freqRelativaSuma = [[item[0], item[1]/n] for item in freqAbsolutaSuma] 
print("frecuencias relativas de la suma=") 
print(freqRelativaSuma)
