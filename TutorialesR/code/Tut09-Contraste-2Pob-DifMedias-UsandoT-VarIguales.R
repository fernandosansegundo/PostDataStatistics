####################################################
# www.postdata-statistics.com
# POSTDATA. Introducción a la Estadísitica
# Tutorial-09.  
#
# Fichero de instrucciones R para calcular 
# un contraste de  hipotesis para la 
#      DIFERENCIA DE MEDIAS 
# de dos poblaciones normales independientes.  
# Se  supone que 
# ALGUNA DE LAS MUESTRAS ES PEQUEÑA  
# Y LAS VARIANZAS DE LAS DOS POBLACIONES SON IGUALES.
# El fichero no funcionara si no introduces todos los datos. 
################################################################

 rm(list = ls())

 # PRIMERA MUESTRA # Numero de elementos
 (n1 = )
 # Media muestral
 (xbar1 = )
 # Cuasidesviacion tipica muestral 
 (s1 = )


 # SEGUNDA MUESTRA 
 # Numero de elementos 
 (n2 = ) 
 # Media muestral 
 (xbar2 = ) 
 # Cuasidesviacion tipica  muestral  
 (s2 = )


# ¿Que tipo de contraste estamos haciendo?
# Escribe:    1 si la HIP. ALTERNATIVA es mu1 > mu2, 
#             2 si es mu1 < mu2, 
#             3 si es mu1 distinto de mu2
TipoContraste = 

#Nivel de significacion
(nSig = )

 ############################################### 
 # NO CAMBIES NADA DE AQUÍ PARA ABAJO
 ###############################################

 

 # Calculo de alfa
   (alfa = 1 - nSig)

 # Grados de libertad

 k = n1 + n2 -2

 # Calculo del estadistico del contraste
   denomEstad=
   sqrt(((1/n1) + (1/n2)) * ((n1 - 1) * s1^2 + (n2-1) * s2^2) / k)

     (Estadistico=(xbar1 - xbar2) / denomEstad)
 # Funcion para el calculo del p-valor
     pValor=function(EstadCon, tipoCon){
       if(tipoCon == 1){
         (pV=1 - pt(EstadCon, df=k))
       }
       if(tipoCon == 2){
         (pV = pt(EstadCon,df=k))
       }
       if(tipoCon == 3){
         pV=2 * (1 - pt(abs(EstadCon), df=k))
       }
       return(paste("El p-Valor es ", pV, sep="", collapse=""))
     }
 # Funcion para el calculo del límite de la región de rechazo
     RegionRechazo = function(alfa, tipoCon){
       if(tipoCon == 1){
         (regionRech = paste("Valores del Estadistico mayores que ", 
                           qt(1 - alfa, df=k)))
       }
       if(tipoCon == 2){
         (regionRech = paste("Valores del Estadistico menores que ", 
                             qt(alfa, df=k)) )
       }
       if(tipoCon == 3){
         (regionRech = paste("Valores del Estadistico mas alejados del origen que ", 
                             qt(1 - alfa/2, df=k)) )
       }
       regionRech=paste("La region de rechazo la forman los ",
                        regionRech, sep="", collapse="")
       return(regionRech)
     }

 # Y ahora se aplican ambas funciones para mostrar los resultados
     pValor(Estadistico, TipoContraste)
     Estadistico
     RegionRechazo(alfa, TipoContraste)
