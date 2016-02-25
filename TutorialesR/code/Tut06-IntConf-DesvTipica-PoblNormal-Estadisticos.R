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
# Este fichero usa los estadisticos  de una muestra,
# previamente calculados (numero de datos, media muestral, etc.) 
##############################################################

rm(list=ls()) #limpieza inicial

# ATENCIÓN:
# Para usar este fichero 
# la población debe ser (al menos aprox.) normal
# EN OTROS CASOS NO USES ESTE FICHERO!!
# ASEGURATE DE HABER ENTENDIDO ESTAS INSTRUCCIONES

# Introducimos el valor de la desviacion tipica muestral,
s = 

# el tamaño de la muestra,
n = 

# y el nivel de confianza deseado.
nc = 

################################################
#NO CAMBIES NADA DE AQUI PARA ABAJO
################################################
# Calculamos alfa
alfa = 1 - nc

# y los grados de libertad:

(k= n - 1)

# Calculamos los valores criticos necesarios:

(chiAlfa2 = qchisq(1 - (alfa/2), df=k))

(chiUnoMenosAlfa2 = qchisq(alfa/2, df=k))


#Para la varianza, el intervalo de confianza sera
# extremo inferior
(intervaloVar = s^2 * k / c(chiAlfa2, chiUnoMenosAlfa2))

# Y para la desviacion tipica el intervalo de confianza es este:
(intervaloS = s * sqrt(k / c(chiAlfa2, chiUnoMenosAlfa2)))





