####################################################
# www.postdata-statistics.com
# POSTDATA. Introducción a la Estadísitica
# Tutorial-06.  
#
# Fichero de instrucciones R para calcular
# un intervalo de confianza (1-alfa) para la 
#
#    DESVIACION TIPICA de una  poblacion normal N(mu,sigma), 
#
# a partir de una muestra de tamaño n.
# Este fichero usa los datos de la muestra en bruto, en forma 
# de vector o en un fichero csv. Lee las instrucciones mas .
# abajo
##############################################################

rm(list=ls()) #limpieza inicial

# ATENCIÓN:
# Para usar este fichero 
# la población debe ser (al menos aprox.) normal
# EN OTROS CASOS NO USES ESTE FICHERO!!
# ASEGURATE DE HABER ENTENDIDO ESTAS INSTRUCCIONES

##########################################
# EL FICHERO NO FUNCIONARÁ BIEN HASTA
# QUE HAYAS COMPLETADO CORRECTAMENTE LA
# INFORMACIÓN DE LAS LINEAS 
#     32, 43 Y 47
##########################################

# Una posibilidad es que tengas la muestra como un vector. 
muestra =   # SI NO SE USA, ESCRIBE # AL PRINCIPIO DE LA LINEA
  
  
# Si lees la muestra de un fichero csv:
# 1. selecciona el directorio de trabajo
# Para eso, escribe el nombre entre las comillas. En RStudio puedes usar el tabulador como ayuda.
setwd(dir="")  # SI NO SE USA, ESCRIBE # AL PRINCIPIO DE LA LINEA


# 2. Ahora introduce entre las comillas el nombre del fichero, y el tipo de separador, etc.

muestra = read.table(file=" ", header = , sep=" ",dec=".")[ , 1]  # SI NO SE USA, ESCRIBE # AL PRINCIPIO DE LA LINEA


# Introducimos el nivel de confianza deseado.
nc=

################################################
#NO CAMBIES NADA DE AQUI PARA ABAJO
################################################

# alfa
(alfa = 1 - nc )

# Numero de datos de la muestra, grados de libertad
(n = length(muestra))
k = n - 1

# Cuasidesviacion tipica muestral
(s = sd(muestra))

# Calculamos los valores criticos necesarios:

(chiAlfa2 = qchisq(1 - (alfa/2), df=k))

(chiUnoMenosAlfa2 = qchisq(alfa/2, df=k))

#Para la varianza, el intervalo de confianza sera
# extremo inferior
(intervaloVar = s^2 * k / c(chiAlfa2, chiUnoMenosAlfa2))

# Y para la desviacion tipica el intervalo de confianza es este:
(intervaloS = s * sqrt(k / c(chiAlfa2, chiUnoMenosAlfa2)))





