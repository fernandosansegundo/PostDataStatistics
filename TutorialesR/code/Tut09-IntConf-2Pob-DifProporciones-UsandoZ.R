####################################################
# www.postdata-statistics.com
# POSTDATA. Introducción a la Estadísitica
# Tutorial-09.  
#
# Fichero de instrucciones R para calcular 
# un intervalo de confianza para la 
#      DIFERENCIA DE PROPORCIONES 
# en dos poblaciones tipo Bernouilli independientes. 
# Se supone que AMBAS MUESTRAS SON GRANDES.  
# El fichero no funcionara si no introduces todos los datos.  
################################################################

rm(list=ls())


# PRIMERA MUESTRA 
# Numero de elementos
(n1 = )
# proporcion muestral
(pMuestral1 = )  # Como un cociente (entre 0 y 1)

# SEGUNDA MUESTRA 
# Numero de elementos 
(n2 =  ) 
# proporcion muestral 
(pMuestral2 = )  # Como un cociente (entre 0 y 1)

# Nivel de confianza deseado. 
nc = 

################################################
#NO CAMBIES NADA DE AQUI PARA ABAJO
################################################
 
# Calculamos el valor critico: 

(alfa = 1 - nc)

(z_alfa2= qnorm(1 - alfa/2))

# el valor de los q muestrales
 
(qMuestral1 = 1 - pMuestral1)

(qMuestral2 = 1 - pMuestral2)


#La semianchura del intervalo es

(semianchura = z_alfa2 * sqrt(((pMuestral1 * qMuestral1) / n1) + ((pMuestral2 * qMuestral2) / n2)))
 
# El intervalo de confianza para p1 - p2 es este: 

(intervalo = (pMuestral1 - pMuestral2) + c(-1, 1) * semianchura)





 