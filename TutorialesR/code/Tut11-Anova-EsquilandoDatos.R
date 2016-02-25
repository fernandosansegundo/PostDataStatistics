## ---- Tut11-Anova-EsquilandoDatos
####################################################
# www.postdata-statistics.com
# POSTDATA. Introducción a la Estadísitica
# Tutorial-11.
#
# Fichero de instrucciones R para esquilar (preparar) una tabla de 
# datos "sucios", y obtener un fichero "limpio" para un ANOVA unifactorial .
#
# Se supone que:
#  -Los datos "sucios" estan en un fichero de texto (p.ej. csv o txt) con 
#   tantas columnas como niveles del factor.
#  -Por tanto, cada columna corresponde a una nivel.
#  -No se supone que todas las columnas tengan el mismo número de observaciones.
#  -Los nombres de los niveles aparecen en la primera fila.
# El fichero de salida contendra datos "limpios". Es decir:
#  -Cada columna corresponde a una variable.
#  -Cada fila corresponde a una observación particular.
# Los títulos de las columnas (nombres de variables) 
# aparecerán en la primera fila.
#############################################################
# INSTRUCCIONES:
# - No olvides fijar el directorio de trabajo
# - Escribe el nombre del fichero de entrada y el separador en la línea 38. 
# - Escribe el nombre del fichero de salida en la línea 41. 
#############################################################
#rm(list=ls())

#########################################
# LECTURA DE LOS DATOS
#########################################
# Fijamos el directorio de trabajo.
#setwd("")

#Leemos datos del fichero (NO OLVIDES SEPARADOR Y SÍMBOLO DECIMAL)
datosSucios = read.table(file="ANOVA Figura 1.csv",sep=";",dec=",",header=T,na.strings=c("NA"," ","") )


datosSucios

# Recuerda introducir aqui el nombre del fichero de salida
ficheroSalida=""

# Descomenta esta línea para comprobar que la lectura ha sido correcta.
#View(datosSucios)

(niveles=names(datosSucios))


# Numero de columnas (niveles)
numCol=ncol(datosSucios)

# Ahora usamos un bucle for para crear los dos vectores
# del data.frame de datos limpios. El trabajo mas delicado
# consiste en detectar la longitud  de cada columna, que nos 
# dice el numero de replicas de ese nivel del factor.
Respuesta=c()
Tratamiento=c()
for(i in 1:numCol){
  # primero se detectan si esta columna tiene huecos
  localizarNA=!is.na(datosSucios[,i]) 
  # nos quedamos con los datos que contiene
  columnaSinNA=datosSucios[localizarNA,i]
  # los unimos al vector Respuesta
  Respuesta=c(Respuesta,columnaSinNA)
  numFilas=length(columnaSinNA)
  # Ahora fabricamos un vector con tantas
  # repeticiones del nombre del nivel como
  # elementos tenga esa columna
  replicasNivel=rep(niveles[i],numFilas)
  # Y lo unimos al vector Tratamiento
  Tratamiento=c(Tratamiento,replicasNivel)
} 
Respuesta
Tratamiento

# Ya podemos armar el data.frame de datos limpios
datosLimpios=data.frame(Tratamiento, Respuesta)

# Y guardarlo en el fichero de salida
write.table(datosLimpios,file=ficheroSalida,sep=",",row.names=FALSE,col.names=TRUE)

