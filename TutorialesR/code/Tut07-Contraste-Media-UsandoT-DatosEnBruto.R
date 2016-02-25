####################################################
# www.postdata-statistics.com
# POSTDATA. Introducción a la Estadísitica
# Tutorial-07.  
#
# Fichero de instrucciones R para calcular
# un contraste de hipotesis para la media de una
# poblacion normal N(mu,sigma), a partir de 
# un fichero con una muestra de esa poblacion.
#
# El fichero no funcionara si no introduces todos los datos.
# Además tendrás que descomentar algunas lineas para elegir 
# la forma en la que lees los datos.
#
################################################################


#################################################################
# CASO:  sigma desconocida, muestra pequeña  n<30.
#################################################################

rm(list = ls())

# Una posibilidad es que tengas la muestra como un vector. 

#muestra =   


# Si lees la muestra de un fichero csv:

# 1. Recuerda seleccionar el directorio de trabajo.

# 2. Ahora introduce entre las comillas el nombre del fichero, y el tipo de separador, etc.

#muestra = scan(file="",sep=" ",dec=".")  


# Valor a contrastar de la media (aparece en la hipotesis nula)

(mu0 = )

# ¿Que tipo de contraste estamos haciendo?
# Escribe 1 si la HIP. ALTERNATIVA es mu > mu0, 2 si es mu < mu0, 3 si es mu distinto de mu0    

(TipoContraste = )

##Nivel de significacion

(nSig = )

###############################################
# NO CAMBIES NADA DE AQUÍ PARA ABAJO

###############################################

    
(alfa = 1 - nSig)

# Numero de elementos en la muestra

(n = length(muestra)) 

# Grados de libertad
  
(k = n - 1)

# Media muestral

(xbar = mean(muestra))

# Cuasidesviacion tipica muestral 

(s = sd(muestra))


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

