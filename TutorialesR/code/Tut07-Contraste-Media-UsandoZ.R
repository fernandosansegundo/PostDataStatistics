####################################################
# www.postdata-statistics.com
# POSTDATA. Introducción a la Estadísitica
# Tutorial-07.  
#
# Fichero de instrucciones R para calcular
# un contraste de hipotesis para la media de una
# poblacion normal N(mu,sigma), a partir de 
# los valores precalculados la media muestral y valor de 
# s (o sigma) de  una muestra con n datos.
#
# El fichero NO FUNCIONARA si no introduces todos los datos.
#
################################################################


#################################################################
# CASO:  sigma conocida o desconocida, pero muestra grande  n>30.
#################################################################  
    rm(list=ls())
# Numero de elementos en la muestra
    (n = ) #SE SUPONE QUE LA MUESTRA ES GRANDE, salvo que se conozca sigma
# Media muestral
    (xbar = )
# Cuasidesviacion tipica muestral (o sigma, si fuera conocida)
    (s = )    
# Valor a contrastar de la media (aparece en la hipotesis nula)
    (mu0 = )    
# ¿Que tipo de contraste estamos haciendo?
    # Escribe 1 si la HIP. ALTERNATIVA es mu > mu0, 2 si es mu < mu0, 3 si es mu distinto de mu0    
    (TipoContraste = )
#Nivel de significacion
    (nSig = )
  
###############################################
# NO CAMBIES NADA DE AQUÍ PARA ABAJO
############################################### 
    (alfa = 1 - nSig)
# Calculo del estadistico del contraste
    (Estadistico = (xbar - mu0) / (s / sqrt(n)))
# Funcion para el calculo del p-valor
    pValor = function(EstadCon, tipoCon){
      if(tipoCon == 1){
        (pV = 1 - pnorm(EstadCon))
      }
      if(tipoCon == 2){
        (pV = pnorm(EstadCon))
      }
      if(tipoCon == 3){
        pV = 2 * (1 - pnorm(abs(EstadCon)))
      }    
      return(paste("El p-Valor es ", pV, sep="", collapse=""))
    }
# Funcion para el calculo del límite de la región de rechazo    
    RegionRechazo=function(alfa, tipoCon){
      if(tipoCon == 1){
        (regionRech = paste("Valores del Estadistico mayores que ", qnorm(1-alfa)) )
      }
      if(tipoCon == 2){
        (regionRech = paste("Valores del Estadistico menores que ", qnorm(alfa)) )
      }
      if(tipoCon == 3){
        (regionRech = paste("Valores del Estadistico mas alejados del origen que ",
                            qnorm(1 - alfa/2)) )
      }    
      regionRech = paste("La region de rechazo la forman los ", regionRech, sep="", 
                         collapse="")
      return(regionRech)
    }

# Y ahora se aplican ambas funciones para mostrar los resultados

pValor(Estadistico, TipoContraste)

paste0("El valor del estadístico es ", Estadistico, collapse = "")

RegionRechazo(alfa, TipoContraste)
