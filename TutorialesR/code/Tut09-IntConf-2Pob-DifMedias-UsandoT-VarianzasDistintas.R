####################################################
# www.postdata-statistics.com
# POSTDATA. Introducción a la Estadísitica
# Tutorial-09.  
#
# Fichero de instrucciones R para calcular 
# un intervalo de confianza para la 
# DIFERENCIA DE MEDIAS DE 2 POBLACIONES NORMALES 
# Es el caso de 
# MUESTRAS PEQUEÑAS
# bajo la hipotesis de 
# VARIANZAS IGUALES. 
############################################################## 

# Introducimos los tamaños de las muestras:
n1 = 
n2 =
# Medias muestrales: 
barX1 = 
barX2 = 
# Cuasidesviaciones tipicas muestrales:
s1 = 
s2 =

# Nivel de confianza deseado: 
nc = 

################################################
#NO CAMBIES NADA DE AQUI PARA ABAJO
################################################

# Calculamos los grados de libertad:
(k = n1 + n2 - 2)

# Calculamos el valor critico: 
(alfa = 1 - nc)

(t_alfa2 = qt(1 - alfa/2, df=k))

# La semianchura del intervalo es
(semianchura = t_alfa2 * sqrt((((n1 - 1) * s1^2 + (n2 - 1) * s2^2) /k) * (1/n1 + 1/n2)))


# Intervalo de confianza
(intervalo = (barX1 - barX2) + c(-1, 1) * semianchura  )