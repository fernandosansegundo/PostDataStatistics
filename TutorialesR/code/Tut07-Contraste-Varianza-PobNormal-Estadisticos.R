####################################################
# www.postdata-statistics.com
# POSTDATA. Introducción a la Estadísitica
# Tutorial-07.  
#
# Fichero de instrucciones R para calcular
# un contraste de hipotesis para la VARIANZA de una
# poblacion normal N(mu,sigma), a partir de 
# los valores precalculados la media muestral y valor de 
# s (o sigma) de  una muestra con n datos.
#
# El fichero NO FUNCIONARA si no introduces todos los datos.
#
################################################################
  
    rm(list = ls())
    
# Numero de elementos en la muestra
(n = ) 
# Cuasidesviacion tipica muestral 
(s = )
# Valor a contrastar de la DESVIACION TIPICA que aparece en la hipotesis nula.
# CUIDADO: NO INTRODUZCAS LA VARIANZA POR ERROR
(sigma0 = )
  
# ¿Que tipo de contraste estamos haciendo?
# Escribe 1 si la HIP. ALTERNATIVA es sigma > sigma0, 2 si es sigma < sigma0, 3 si es sigma distinto de sigma0    
TipoContraste = 
    
##Nivel de significacion
(nSig = )
    
###############################################
# NO CAMBIES NADA DE AQUÍ PARA ABAJO
###############################################

(alfa = 1 - nSig)

# Grados de libertad

  k = n - 1

# Calculo del estadistico del contraste
  
  (Estadistico = (n - 1) * s^2/sigma0^2)

# Funcion para el calculo del p-valor

pValor = function(EstadCon,tipoCon){
  if(tipoCon == 1){
    (pV = 1 - pchisq(EstadCon, df = k))
      }
      if(tipoCon == 2){
        (pV = pchisq(EstadCon, df = k))
      }
      if(tipoCon == 3){
        if(TipoContraste == 3){
          if(s > sigma0){
            pV = 2 * (1 - pchisq(EstadCon, df=k))
          } else {
            pV = 2 * (pchisq(EstadCon, df=k))
          }
        }
      }
      pV = signif(pV, digits =4)
      return(paste("El p-Valor es ", pV, sep="", collapse=""))
    }
    
## Funcion para el calculo del límite de la región de rechazo    
    
    RegionRechazo = function(alfa, tipoCon){
      if(tipoCon == 1){
        (regionRech = paste("Valores del Estadistico mayores que ", 
                            qchisq(1 - alfa, df = k)) )
      }
      if(tipoCon == 2){
        (regionRech = paste("Valores del Estadistico menores que ", qchisq(alfa, df = k)) )
      }
      if(tipoCon == 3){
        (regionRech = paste("Valores del Estadistico que no pertenecen al intervalo ", "(",
                            qchisq(alfa/2, df = k), ",", qchisq(1 - alfa/2, df = k), ")") )
      }    
      regionRech=paste("La region de rechazo la forman los ", regionRech, sep="", collapse="")
      return(regionRech)
    }
    
# Y ahora se aplican ambas funciones para mostrar los resultados

paste0("El valor del estadístico es ", Estadistico, collapse = "")
    
pValor(Estadistico, TipoContraste)

RegionRechazo(alfa, TipoContraste)
