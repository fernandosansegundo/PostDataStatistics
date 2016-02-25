####################################################
# www.postdata-statistics.com
# POSTDATA. Introducción a la Estadísitica
# Tutorial-09.  
#
# Fichero de instrucciones R para calcular 
# un contraste de  hipotesis para el
#      COCIENTE DE VARIANZAS 
# de dos poblaciones normales independientes.  
#
# El fichero no funcionara si no introduces todos los datos. 
################################################################

 rm(list=ls())
 
 
 
 # PRIMERA MUESTRA 
 # Numero de elementos
 (n1 = )
 # Cuasidesviacion tipica muestral
 (s1 = )
 
 # SEGUNDA MUESTRA
 # Numero de elementos
 (n2 = )
 # Cuasidesviacion tipica  muestral
 (s2 = )
 
 
 # TIPO DE CONTRASTE:
 # Escribe 1 si la HIP. ALTERNATIVA es sigma > sigma2, 
 #         2 si es sigma1 < sigma2, 
 #         3 si es bilateral.
 TipoContraste = 
 
 #NIVEL DE SIGNIFICACION:
 (nSig = )
 
 
 ############################################### 
 # NO CAMBIES NADA DE AQUÍ PARA ABAJO
 ###############################################

 
 # Calculo de alfa
   (alfa=1-nSig)

 # Calculo del estadistico del contraste
    (Estadistico=s1^2/s2^2)
 # Funcion para el calculo del p-valor
     pValor=function(EstadCon,tipoCon){
       if(tipoCon==1){
         (pV=1-pf(EstadCon,df1=n1-1,df2=n2-1))
       }
       if(tipoCon==2){
         (pV=pf(EstadCon,df1=n1-1,df2=n2-1))
       }
       if(tipoCon==3){
         if(s1>s2)(pV=2*(1-pf(EstadCon,df1=n1-1,df2=n2-1)))
         else(pV=2*(pf(EstadCon,df1=n1-1,df2=n2-1)))
       }
       return(paste("El p-Valor es ",pV,sep="",collapse=""))
     }

 # Y ahora se aplican ambas funciones para mostrar los resultados
     pValor(Estadistico,TipoContraste)
     Estadistico
