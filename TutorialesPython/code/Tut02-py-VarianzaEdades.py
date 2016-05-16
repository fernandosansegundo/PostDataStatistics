edades = [22, 21, 18, 19, 17, 21, 18, 20, 17, 18, 17, 22, 20, 19, 18, 19, 18, 22, 
          20, 19, 22, 18, 20, 21, 20]
mediaEdad = sum(edades) / len(edades)

cuadradosDesviaciones = []
for edad in edades:
  cuadradosDesviaciones = cuadradosDesviaciones + [(edad - mediaEdad)**2]

varianzaEdades = sum(cuadradosDesviaciones) / len(edades)
print(varianzaEdades)
edades = [22, 21, 18, 19, 17, 21, 18, 20, 17, 18, 17, 22, 20, 19, 18, 19, 18, 22, 
          20, 19, 22, 18, 20, 21, 20]
mediaEdad = sum(edades) / len(edades)

cuadradosDesviaciones = []
for edad in edades:
  cuadradosDesviaciones = cuadradosDesviaciones + [(edad - mediaEdad)**2]
  varianzaEdades = sum(cuadradosDesviaciones) / len(edades)
  print(varianzaEdades)
