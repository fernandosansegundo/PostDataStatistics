####################################################
# www.postdata-statistics.com
# POSTDATA. Introducción a la Estadísitica
# Tutorial-09.  
#
# Fichero de instrucciones R para calcular un
# INTERVALO DE CONFIANZA PARA EL COCIENTE DE VARIANZAS
# al nivel (1-alfa)   en dos poblaciones normales.
#
# El fichero no funcionara si no introduces todos los datos. 
##############################################################


# Introducimos los valores de las desviaciones tipicas muestrales,
s1 =
s2 =


# los tamaños de las muestras,
n1 = 
n2 = 

# y el nivel de confianza deseado.
nc = 

## --- NO CAMBIES NADA DE AQUI PARA ABAJO

(alfa = 1 - nc)

# Calculamos los valor criticos necesarios:

(f_alfamedios = qf(alfa/2, df1=n1 - 1, df2=n2 - 1))

(f_unomenosalfamedios = qf(1 - alfa/2, df1=n1 - 1, df2= n2-1))


# El intervalo de confianza para el cociente de varianzas es este:
(intervalo = c( (1/f_unomenosalfamedios), (1/f_alfamedios)) * (s1^2/s2^2))
