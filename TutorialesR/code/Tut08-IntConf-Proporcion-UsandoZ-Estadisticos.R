####################################################
# www.postdata-statistics.com
# POSTDATA. Introducción a la Estadísitica
# Tutorial-08.  
#
# Fichero de instrucciones R para calcular
# un intervalo de confianza (1-alfa) para la proporcion p de 
# una poblacion tipo Binomial (Bernouilli), a partir de una
# muestra con n datos.
#
# Este fichero usa los valores de una muestra,
# previamente calculados (numero de datos, proporcion muestral) 
#
##############################################################

rm(list=ls()) #limpieza inicial

# Introduce el numero de datos de la muestra:

n = 

# Introduce aqui el valor de pMuestral, la proporcion muestral .
# Recuerda que pMuestral es el numero de casos favorables en la muestra 
# dividido por n.
  
pMuestral = 

# LEE ESTAS INSTRUCCIONES ATENTAMENTE:
# SI LA MUESTRA TIENE < 30 ELEMENTOS O SI N*p<5 O SI n*q<5, 
# NO USES ESTE FICHERO!!
# ASEGURATE DE HABER ENTENDIDO ESTAS INSTRUCCIONES

# Nivel de confianza deseado.
  
nc = 

################################################
#NO CAMBIES NADA DE AQUI PARA ABAJO
################################################
(alfa = 1 - nc )

# Calculamos el valor critico:

(z_alfa2 = qnorm( 1 - alfa / 2 ) )


# Calculamos qMuestral

qMuestral = 1 - pMuestral

# Comprobamos la condicion sobre n
if((n<=30)|(n*pMuestral<5)|(n*qMuestral<5)){
  warning("NO SE CUMPLEN LAS CONDICIONES")
}


# Semianchura del intervalo
(semianchura=z_alfa2 * sqrt(pMuestral * qMuestral / n) )

# Y el intervalo de confianza (a,b) para mu es este:

(intervalo = pMuestral + c(-1, 1) * semianchura )

