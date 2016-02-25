####################################################
# www.postdata-statistics.com
# POSTDATA. Introducción a la Estadísitica
# Tutorial-09.  
#
# Fichero de instrucciones R para calcular 
# un intervalo de confianza para la 
# DIFERENCIA DE MEDIAS DE 2 POBLACIONES NORMALES 
# usando la distribución Z 
# Es el caso de MUESTRAS GRANDES o (poco frecuente)
# de varianzas poblacionales conocidas.
##############################################################


rm(list=ls())

# PRIMERA MUESTRA
# Numero de elementos
(n1 = ) 
# Media muestral
(xbar1 = )
# Cuasidesviacion tipica muestral o sigma (descomenta el que uses)
#(s1 = )
#(sigma1 = )


# SEGUNDA MUESTRA
# Numero de elementos
(n2 = ) 
# Media muestral
(xbar2 = )
# Cuasidesviacion tipica muestral o sigma (descomenta el que uses)
#(s2 = )    
#(sigma2 = )

# Nivel de confianza deseado:
nc = 

################################################
#NO CAMBIES NADA DE AQUI PARA ABAJO
################################################

(alfa = 1 - nc)

# Calculamos el valor critico:
(z_alfa2 = qnorm( 1 - alfa / 2))

# La diferencia de las medias muestrales es:

(xbar1 - xbar2)

# Comprobamos si se ha usado sigma como sustituto de s.

if(exists("sigma1")){s1 = sigma1}
if(exists("sigma2")){s2 = sigma2}

# La semianchura del intervalo es:
(semianchura = z_alfa2 * sqrt(s1^2/n1 + s2^2/n2))

# El intervalo de confianza es este:

(intervalo = xbar1 - xbar2 + c(-1, 1) * semianchura )

