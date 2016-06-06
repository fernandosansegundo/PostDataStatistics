print('## ---- dosDados-chunk-0001') 
dado1 = range(1,7) 
print(list(dado1))
print('## ---- dosDados-chunk-0002') 
dado2 = range(1,7)
print('## ---- dosDados-chunk-0003') 
suma = [d1 + d2 for d1 in dado1 for d2 in dado2] 
print(suma)
print('## ---- dosDados-chunk-0004') 
import collections as cl 
sumaCounter = cl.Counter(suma) 
recuentoValoresSuma = sumaCounter.most_common() 
recuentoValoresSuma.sort() 
print(recuentoValoresSuma)
print('## ---- dosDados-chunk-0005') 
n = len(suma) 
print("n=", n) 
probabilidadesSuma = [[item[0], item[1]/n] for item in recuentoValoresSuma] 
print("probabilidadesSuma=", probabilidadesSuma)
print('## ---- dosDados-chunk-0006') 
print(probabilidadesSuma)
print('## ---- dosDados-chunk-0007') 
X = probabilidadesSuma
print('## ---- dosDados-chunk-0008') 
media = sum([x[0] * x[1] for x in X]) 
print("Media de X = {0:0.4f}".format(media)) 
import math as m 
varianza = sum([(x[0] - media)**2 * x[1] for x in X]) 
print("varianza = {0:0.4f}".format(varianza)) 
sigma = m.sqrt(varianza) 
print("desviacion tipica = {0:0.4f}".format(sigma))
print('## ---- dosDados-chunk-0009') 
diferencia = [abs(d1 - d2) for d1 in dado1 for d2 in dado2]
print('## ---- dosDados-chunk-0010') 
diferenciaCounter = cl.Counter(diferencia) 
recuentoValoresDiferencia = diferenciaCounter.most_common() 
recuentoValoresDiferencia.sort() 
print(recuentoValoresDiferencia)
print('## ---- dosDados-chunk-0011') 
n = len(diferencia) 
print("n=", n) 
probabilidadesDiferencia = [[item[0], item[1]/n] for item in recuentoValoresDiferencia] 
print("probabilidadesDiferencia=", probabilidadesDiferencia)
print('## ---- dosDados-chunk-0012') 
Y = probabilidadesDiferencia 
 
media = sum([y[0] * y[1] for y in Y]) 
print("Media de Y = {0:0.4f}".format(media)) 
import math as m 
varianza = sum([(y[0] - media)**2 * y[1] for y in Y]) 
print("varianza = {0:0.4f}".format(varianza)) 
sigma = m.sqrt(varianza) 
print("desviacion tipica = {0:0.4f}".format(sigma))
