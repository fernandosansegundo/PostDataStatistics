####################################################
# www.postdata-statistics.com
# POSTDATA. Introducción a la Estadísitica
# Tutorial-06.  
#
# Fichero de instrucciones R para calcular
# un intervalo de confianza nc=(1-alfa) para la 
#
#     MEDIA de una poblacion normal N(mu,sigma)
#
# a partir de una  muestra con n datos.
# Este fichero usa los datos de la muestra en bruto, en forma 
# de vector o en un fichero csv. Lee las instrucciones mas .
# abajo
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
# LA INFORMACIÓN NECESARIA.
##########################################

# Una posibilidad es que tengas la muestra como un vector. 
muestra =   # SI NO SE USA, ESCRIBE # AL PRINCIPIO DE LA LINEA
  
  
# Si lees la muestra de un fichero csv:
# 1. selecciona el directorio de trabajo
# Para eso, escribe el nombre entre las comillas. En RStudio puedes usar el tabulador como ayuda.
(setwd(dir=""))  # SI NO SE USA, ESCRIBE # AL PRINCIPIO DE LA LINEA


# 2. Ahora introduce entre las comillas el nombre del fichero, y el tipo de separador, etc.

muestra = read.table(file=" ", header = , sep=" ",dec=".")[ , 1]  # SI NO SE USA, ESCRIBE # AL PRINCIPIO DE LA LINEA

# Nivel de confianza deseado.
nc = 


################################################
#NO CAMBIES NADA DE AQUI PARA ABAJO
################################################
# Numero de datos de la muestra,
(n = length(muestra))

# Calculamos el valor de xbar, la media muestral 
(xbar = mean(muestra))

# Cuasidesviacion tipica muestral
s = sd(muestra)

# alfa
(alfa = 1 - nc )

# Calculamos el valor critico:

(t_alfa2 = qt( 1 - alfa / 2 , df=n-1 ) )

#y la semianchura del intervalo
(semianchura = t_alfa2 * s / sqrt(n) )

# Y el intervalo de confianza (a,b) para mu es este:
xbar + c(-1, 1) * semianchura
