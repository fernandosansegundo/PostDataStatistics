edades = [22, 21, 18, 19, 17, 21, 18, 20, 17, 18, 17, 22, 20, 19, 18, 19, 18, 22, 
          20, 19, 22, 18, 20, 21, 20]
edadMedia = sum(edades) / len(edades)

cuadradosDesviaciones = []
for edad in edades:
  cuadradosDesviaciones = cuadradosDesviaciones + [(edad - edadMedia)**2]

varianzaEdades = sum(cuadradosDesviaciones) / len(cuadradosDesviaciones)
print(varianzaEdades)
