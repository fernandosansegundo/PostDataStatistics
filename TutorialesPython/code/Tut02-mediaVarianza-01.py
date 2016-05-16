edades = [22, 21, 18, 19, 17, 21, 18, 20, 17, 18, 17, 22, 20, 19, 18, 19, 18, 22, 
20, 19, 22, 18, 20, 21, 20]
m = sum(edades) / len(edades)
print(m)
nV = []
for edad in edades:
  nV = nV + [(edad - m)**2] 
v = sum(nV) / len(edades)
print(v)
import math as m
print(m.sqrt(v))
