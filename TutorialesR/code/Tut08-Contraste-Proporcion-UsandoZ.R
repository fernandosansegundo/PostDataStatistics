####################################################
# www.postdata-statistics.com
# POSTDATA. Introducción a la Estadísitica
# Tutorial-08.  
#
# Fichero de instrucciones R para calcular un contraste de 
# hipotesis para la proporcion, a partir de una
#
#         MUESTRA GRANDE 
#
# con n >> 30 datos.
#
# El fichero no funcionara si no introduces todos los datos.
#
################################################################

    rm(list=ls())
# Numero de elementos en la muestra
    (n= ) #SE SUPONE QUE LA MUESTRA ES GRANDE, n>30
# Proporcion muestral (¡es una fraccion! Numero de exitos/n)
    (pMuestral= )
# Valor a contrastar de la proporcion (aparece en la hipotesis nula)
    (p0= )    
# ¿Que tipo de contraste estamos haciendo?
    # Escribe 1 si la HIP. ALTERNATIVA es p > p0, 2 si es p < p0, 3 si es p distinto de p0    
    TipoContraste = 
#Nivel de significacion
    (nSig= )
  
###############################################
# NO CAMBIES NADA DE AQUÍ PARA ABAJO
############################################### 

# Calculo de alfa
    (alfa=1-nSig)
# Calculo de q0
    q0 = 1- p0
# Comprobamos la condicion sobre n
if((n<=30)|(n*p0<5)|(n*q0<5)){
  warning("NO SE CUMPLEN LAS CONDICIONES")
}
# Calculo del estadistico del contraste
    (Estadistico=(pMuestral-p0) / sqrt( (p0 * q0) / n ))
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
        (regionRech=paste("valores del Estadistico mayores que ",qnorm(1-alfa)) )
      }
      if(tipoCon==2){
        (regionRech=paste("valores del Estadistico menores que ",qnorm(alfa)) )
      }
      if(tipoCon==3){
        (regionRech=paste("valores del Estadistico mas alejados del origen que ",qnorm(1-alfa/2)) )
      }    
      regionRech=paste("La region de rechazo la forman los ",regionRech,sep="",collapse="")
      return(regionRech)
    }

# Y ahora se aplican ambas funciones para mostrar los resultados
    pValor(Estadistico,TipoContraste)  
    Estadistico
    RegionRechazo(alfa,TipoContraste)
    
    
    
    
    
    
    
    
    
    
    