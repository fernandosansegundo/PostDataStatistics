####################################################
# www.postdata-statistics.com
# POSTDATA. Introduccion a la Estadistica
# Tutorial-06.  
#
# Fichero de instrucciones R para calcular
# un intervalo de confianza (1-alfa) para la media de una
# poblacion normal N(mu,sigma), a partir de una
# muestra con n datos.
#
# Este fichero usa los resumenes de una muestra,
# previamente calculados (numero de datos, media muestral, etc.) 
#
##############################################################

rm(list=ls()) #limpieza inicial

# Introduce el numero de datos de la muestra,
n =   

# Introduce aqui el valor de xbar, la media muestral 
xbar = 

# LEE ESTAS INSTRUCCIONES ATENTAMENTE:
# Si la muestra tiene mas de 30 elementos
# introduce el valor de s, la cuasidesviacion tipica de la poblacion.
# Si la poblacion es normal, y conoces sigma, la desviacion tipica de
# la poblacion, puedes usarla en lugar de s, aunque sea n<30. 
# 
# SI LA MUESTRA TIENE < 30 ELEMENTOS Y DESCONOCES SIGMA, 
# NO USES ESTE FICHERO!!
# ASEGURATE DE HABER ENTENDIDO ESTAS INSTRUCCIONES

s =    # O sigma, lee las instrucciones.

# y el nivel de confianza deseado.
nc = 

################################################
# NO CAMBIES NADA DE AQUI PARA ABAJO
################################################
(alfa = 1 - nc )

# Calculamos el valor critico:

(z_alfa2 = qnorm( 1 - alfa / 2 ) )

#y la semianchura del intervalo
(semianchura=z_alfa2 * s / sqrt(n) )

# El intervalo de confianza (a,b) para mu es este:
(intervalo = xbar + c(-1, 1) * semianchura )

