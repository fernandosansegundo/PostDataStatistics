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
# Este fichero usa los datos de la muestra en bruto, en forma 
# de vector o en un fichero csv. Lee las instrucciones mas .
# abajo
##############################################################

rm(list=ls()) #limpieza inicial

##########################################
# EL FICHERO NO FUNCIONARÁ BIEN HASTA
# QUE HAYAS COMPLETADO CORRECTAMENTE 
# TODA LA INFORMACIÓN NECESARIA.
##########################################

# Una posibilidad es que tengas la muestra como un vector. 
muestra =   # SI NO SE USA, ESCRIBE # AL PRINCIPIO DE ESTA LINEA


# Si lees la muestra de un fichero csv:
# 1. selecciona el directorio de trabajo
# Para eso, escribe el nombre entre las comillas. En RStudio puedes usar el tabulador como ayuda.
(setwd(dir=""))  # SI NO SE USA, ESCRIBE # AL PRINCIPIO DE ESTA LINEA
  
# 2. Ahora introduce entre las comillas el nombre del fichero, y el tipo de separador, etc.
muestra = scan(file=" ",sep=" ",dec=".")  # SI NO SE USA, ESCRIBE # AL PRINCIPIO DE ESTA LINEA


# LEE ESTAS INSTRUCCIONES ATENTAMENTE:
# Si la muestra tiene mas de 30 elementos
# calculamos el valor de s, la cuasidesviacion tipica de la poblacion.
# Si la poblacion es normal, y conoces sigma, la desviacion tipica de
# la poblacion, puedes CAMBIAR A MANO s por sigma, aunque sea n<30. 
# 
# SI LA MUESTRA TIENE < 30 ELEMENTOS Y DESCONOCES SIGMA, 
# NO USES ESTE FICHERO!!
# ASEGURATE DE HABER ENTENDIDO ESTAS INSTRUCCIONES

(s = sd(muestra) )   # O sigma, lee las instrucciones.

# y el nivel de confianza deseado.
nc = 

################################################
#NO CAMBIES NADA DE AQUI PARA ABAJO
################################################
# Calculamos la longitud de la muestra

(n = length( muestra ))

# Calculamos la media muestral 
(xbar = mean( muestra ) )

# Calculamos alfa
(alfa = 1 - nc )

# Calculamos el valor critico:

(z_alfa2 = qnorm( 1 - alfa / 2 ) )

#y la semianchura del intervalo
(semianchura=z_alfa2 * s / sqrt(n) )

# El intervalo de confianza (a,b) para mu es este:
(intervalo = xbar + c(-1, 1) * semianchura )

