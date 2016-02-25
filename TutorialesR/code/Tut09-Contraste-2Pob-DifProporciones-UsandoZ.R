####################################################
# www.postdata-statistics.com
# POSTDATA. Introducción a la Estadísitica
# Tutorial-09.  
#
# Fichero de instrucciones R para calcular 
# un contraste de hipotesis para la 
#      DIFERENCIA DE PROPORCIONES 
# de dos poblaciones tipo Bernouilli independientes. 
# Se supone que AMBAS MUESTRAS SON GRANDES.  
# El fichero no funcionara si no introduces todos los datos.  
################################################################

rm(list=ls())

# PRIMERA MUESTRA 
# Numero de elementos
(n1 = )
# proporcion muestral
(pMuestral1 = )

# SEGUNDA MUESTRA 
# Numero de elementos 
(n2 =  ) 
# proporcion muestral 
(pMuestral2 = )

# ¿Que tipo de contraste estamos haciendo?
# Escribe 1 si la HIP. ALTERNATIVA es p1 > p2, 2 si es p1 < p2, 3 si es bilateral
TipoContraste = 
  #Nivel de significacion
  (nSig= )

############################################### 
# NO CAMBIES NADA DE AQUÍ PARA ABAJO
###############################################
(alfa=1-nSig)

# Calculo de qMuestral1 y qMuestral2

qMuestral1 = 1 - pMuestral1 
qMuestral2 = 1 - pMuestral2

# Calculo de p y q ponderados

(pMuestral = (n1 * pMuestral1 + n2 * pMuestral2) / (n1 + n2) ) 
qMuestral = 1- pMuestral

# Calculo del estadistico del contraste
(Estadistico=( pMuestral1 - pMuestral2 ) / sqrt( pMuestral * qMuestral * ((1/n1) + (1/n2)) ) )
# Funcion para el calculo del p-valor
pValor=function(EstadCon,tipoCon){
  if(tipoCon==1){
    (pV=1-pnorm(EstadCon))
  }
  if(tipoCon==2){
    (pV=pnorm(EstadCon))
  }
  if(tipoCon==3){
    pV=2*(1-pnorm(abs(EstadCon)))
  }
  return(paste("El p-Valor es ",pV,sep="",collapse=""))
}
# Funcion para el calculo del límite de la región de rechazo
RegionRechazo=function(alfa,tipoCon){
  if(tipoCon==1){
    (regionRech=paste("Valores del Estadistico mayores que ",qnorm(1-alfa)) )
  }
  if(tipoCon==2){
    (regionRech=paste("Valores del Estadistico menores que ",qnorm(alfa)) )
  }
  if(tipoCon==3){
    (regionRech=paste("Valores del Estadistico mas alejados del origen que ",qnorm(1-alfa/2)) )
  }
  regionRech=paste("La region de rechazo la forman los ",regionRech,sep="",collapse="")
  return(regionRech)
}

# Y ahora se aplican ambas funciones para mostrar los resultados
pValor(Estadistico,TipoContraste)
Estadistico
RegionRechazo(alfa,TipoContraste)
 