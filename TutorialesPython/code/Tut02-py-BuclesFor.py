edades = [22, 21, 18, 19, 17, 21, 18, 20, 17, 18, 17, 22, 20, 19, 18, 19,
18, 22, 20, 19, 22, 18, 20, 21, 20]

mediaEdad = sum(edades) / len(edades)

diferenciasCuad = [ ]


edad =  22
diferencia = edad - mediaEdad
cuadradoDif = diferencia**2
diferenciasCuad = diferenciasCuad + [cuadradoDif]

print(diferenciasCuad)

