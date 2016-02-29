edades = [22, 21, 18, 19, 17, 21, 18, 20, 17, 18, 17, 22, 20, 19, 18, 19, 18, 22, 
20, 19, 22, 18, 20, 21, 20]
print("La lista de edades es:")
print(edades)
mediaAritmetica = sum(edades) / len(edades)
print("La media aritmética es:")
print(mediaAritmetica)
terminosVarianza = []
for edad in edades:
  terminosVarianza = terminosVarianza + [(edad - mediaAritmetica)**2] 
varianzaPob = sum(terminosVarianza) / len(edades)
print("La varianza poblacional es:")
print(varianzaPob)
import math as m
print("La desviación típica poblacional es:")
print(m.sqrt(varianzaPob))