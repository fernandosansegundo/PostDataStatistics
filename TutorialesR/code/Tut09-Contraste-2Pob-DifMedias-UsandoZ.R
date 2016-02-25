  ####################################################
  # www.postdata-statistics.com
  # POSTDATA. Introducción a la Estadísitica
  # Tutorial-09.  
  #
  # Fichero de instrucciones R para calcular 
  # un contraste de hipotesis para la 
  #      DIFERENCIA DE MEDIAS 
  # de dos poblaciones normales independientes.
  # 
  # Se supone que AMBAS MUESTRAS SON GRANDES.
  #
  # El fichero no funcionara si no introduces todos los datos.
  #
  ################################################################
  
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
  
  # ¿Que tipo de contraste estamos haciendo?
      # Escribe 1 si la HIP. ALTERNATIVA es mu1 > mu2, 2 si es mu1 < mu2, 3 si es mu1 distinto de mu2    
      TipoContraste = 
  #Nivel de significacion
      (nSig = )
    
  ###############################################
  # NO CAMBIES NADA DE AQUÍ PARA ABAJO
  ############################################### 
  
  # Comprobamos si se ha usado sigma como sustituto de s.
  
  if(exists("sigma1")){s1 = sigma1}
  if(exists("sigma2")){s2 = sigma2}
  
  
  # Calculo de alfa
    (alfa = 1 - nSig)
  
  # Calculo del estadistico del contraste
      (Estadistico = (xbar1 - xbar2) / sqrt( (s1^2 / n1) + (s2^2 / n2) ) )
  
  # Funcion para el calculo del p-valor
      pValor = function(EstadCon,tipoCon){
        if(tipoCon == 1){
          (pV = 1 - pnorm(EstadCon))
        }
        if(tipoCon == 2){
          (pV = pnorm(EstadCon))
        }
        if(tipoCon == 3){
          pV = 2 * (1 - pnorm(abs(EstadCon)))
        }    
        return(paste("El p-Valor es ", pV,sep="", collapse=""))
      }
  # Funcion para el calculo del límite de la región de rechazo    
      RegionRechazo = function(alfa,tipoCon){
        if(tipoCon == 1){
          (regionRech = paste("valores del Estadistico mayores que ", qnorm(1 - alfa)) )
        }
        if(tipoCon == 2){
          (regionRech = paste("valores del Estadistico menores que ", qnorm(alfa)) )
        }
        if(tipoCon == 3){
          (regionRech = paste("Valores del Estadistico mas alejados del origen que ", qnorm(1 - alfa/2)) )
        }    
        regionRech=paste("La region de rechazo la forman los ", regionRech, sep="", collapse="")
        return(regionRech)
      }
  
  # Y ahora se aplican ambas funciones para mostrar los resultados
      pValor(Estadistico, TipoContraste)  
      Estadistico
      RegionRechazo(alfa, TipoContraste)
      
      
      
      
      
      
      
      
      
      
      