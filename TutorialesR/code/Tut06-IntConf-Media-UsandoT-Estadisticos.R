####################################################
# www.postdata-statistics.com
# POSTDATA. Introducción a la Estadísitica
# Tutorial-06.  
#
# Fichero de instrucciones R para calcular
# un intervalo de confianza (1-alfa) para la 
#
#     MEDIA de una poblacion normal N(mu,sigma)
#
# a partir de una  muestra con n datos.
# Este fichero usa los estadisticos  de una muestra,
# previamente calculados (numero de datos, media muestral, etc.) 
#
##############################################################

rm(list=ls()) #limpieza inicial

# LEE ESTAS INSTRUCCIONES ATENTAMENTE:
# La distribucion t de Student se usa cuando:
# (1) La población es (al menos aprox.) normal
# (2) Se desconoce sigma, la desviacion tipica de la poblacion
# (3) La muestra es pequeña (<30 elementos) 
# EN OTROS CASOS NO USES ESTE FICHERO!!
# ASEGURATE DE HABER ENTENDIDO ESTAS INSTRUCCIONES
##########################################
# EL FICHERO NO FUNCIONARÁ BIEN HASTA
# QUE HAYAS COMPLETADO CORRECTAMENTE TODA 
# LA INFORMACIÓN NECESARIA
##########################################


# Introduce el numero de datos de la muestra,
n = 

# Introduce aqui el valor de xbar, la media muestral 
xbar = 

# Cuasidesviacion tipica muestral
s = 

# y el nivel de confianza deseado.
nc = 

################################################
#NO CAMBIES NADA DE AQUI PARA ABAJO
################################################
(alfa = 1 - nc )

# Calculamos el valor critico:

(t_alfa2 = qt( 1 - alfa / 2 , df=n-1 ) )

#y la semianchura del intervalo
(semianchura=t_alfa2 * s / sqrt(n) )

# Y el intervalo de confianza (a,b) para mu es este:
xbar + c(-1, 1) * semianchura

