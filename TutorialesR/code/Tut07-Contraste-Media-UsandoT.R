####################################################
# www.postdata-statistics.com
# POSTDATA. Introducción a la Estadísitica
# Tutorial-07.  
#
# Fichero de instrucciones R para calcular
# un contraste de hipotesis para la media de una
# poblacion normal N(mu,sigma), a partir de 
# los valores precalculados la media muestral y la
# cuasidesviacion tipica muestral s de una muestra
# con n datos.
#
# El fichero NO FUNCIONARA si no introduces todos los datos.
#
################################################################


#################################################################
# CASO:  sigma desconocida, muestra pequeña n<30.
#################################################################
    
    rm(list=ls())
    
    # Numero de elementos en la muestra
    (n= ) #SE SUPONE QUE LA MUESTRA ES PEQUEÑA
    
    # Media muestral
    (xbar= )
    
    # Cuasidesviacion tipica muestral
    (s= )
    
    # Valor a contrastar de la media (aparece en la hipotesis nula)
    (mu0= )
    
    # ¿Que tipo de contraste estamos haciendo?
    # Escribe 1 si la HIP. ALTERNATIVA es mu > mu0, 2 si es mu < mu0, 3 si es mu distinto de mu0    
    TipoContraste = 
    
    ##Nivel de significacion
    (nSig= )
    
    ###############################################
    # NO CAMBIES NADA DE AQUÍ PARA ABAJO
    ###############################################
    
    (alfa = 1-nSig)

    (k = n - 1)

# Calculo del estadistico del contraste

(Estadistico = (xbar - mu0) / (s/sqrt(n)))

# Funcion para el calculo del p-valor

pValor = function(EstadCon, tipoCon){
  if(tipoCon == 1){
    (pV = 1 - pt(EstadCon, df=k ))
  }
  if(tipoCon == 2){
    (pV = pt(EstadCon, df=k ))
  }
  if(tipoCon == 3){
    pV = 2 * (1 - pt(abs(EstadCon), df=k ))
  }    
  return(paste0("El p-Valor es ", pV, collapse=""))
}

# Funcion para el calculo del límite de la región de rechazo    

RegionRechazo = function(alfa, tipoCon){
  if(tipoCon == 1){
    (regionRech = paste("mayores que ", 
                        qt(1 - alfa, df=k)))
  }
  if(tipoCon == 2){
    (regionRech = paste("menores que ",
                        qt(alfa, df=k)))
  }
  if(tipoCon == 3){
    (regionRech = paste("mas alejados del origen que ",
                        qt(1 - (alfa/2), df=k)))
  }    
  regionRech = paste0("La region de rechazo la forman los valores del Estadistico ",
                      regionRech, collapse="")
  return(regionRech)
}

# Y ahora se aplican ambas funciones para mostrar los resultados

pValor(Estadistico, TipoContraste)

paste0("El valor del estadístico es ", Estadistico, collapse = "")

RegionRechazo(alfa, TipoContraste)

