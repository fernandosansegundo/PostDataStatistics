####################################################
# www.postdata-statistics.com
# POSTDATA. Introducción a la Estadísitica
# Tutorial-11.
#
# Fichero de instrucciones R para calcular un contraste
# ANOVA unifactorial .
# Se supone que:
#  + Los datos estan en un fichero csv con dos columnas.
#  + Son datos "limpios". Es decir:
#       · cada columna corresponde a una variable.
#       · cada fila corresponde a una observación particular.
#  + Los títulos de las columnas (nombres de variables)
#   aparecen en la primera fila (y no incluyen espacios).
#  + No hay elementos ausentes: las filas están todas completas.
#  + No se supone que todos los tratamientos tengan el
#   mismo número de observaciones.
#############################################################
# INSTRUCCIONES:
# + No olvides cambiar el directorio de trabajo, en la línea 31,
#   para que sea el que contiene la carpeta datos donde esta el csv.
# + Escribe el nombre del fichero y el tipo de separador en la línea 32.
# + Indica que columna contiene el factor (tratamiento) en la linea 38.
#############################################################

#########################################
# LECTURA DE LOS DATOS
#########################################
#Leemos los datos del fichero
datos = read.table(file="./datos/", sep=" ",header=T)

# Descomenta esta línea si quieres comprobar que la lectura ha sido correcta.
# View(datos)

# IMPORTANTE: introduce el número de columna ( 1 o 2 ) que contiene el factor (tratamiento).
colFactor =

#########################################
# ANALISIS DE LOS DATOS
# No es necesario cambiar nada de aquí para abajo.
#########################################

# Renombramos las columnas del data.frame
if(colFactor==1){
  colnames(datos) = c("Tratamiento","Respuesta")
}else{
  colnames(datos) = c("Respuesta","Tratamiento")
}
colnames(datos)

# Etiquetas de los niveles del factor.

(niveles=levels(datos$Tratamiento))

# El número total de observaciones.

(N=nrow(datos))

# Calculamos el número de niveles del factor

(k=length(niveles))

#######################################
# Construccion manual de la tabla ANOVA

# La media de todas las respuestas, sin distinguir niveles del factor

(mediaDatos = mean(datos$Respuesta))

# La suma total de cuadrados.

(SStotal = sum((datos$Respuesta-mediaDatos)^2) )

# La media de cada uno de los niveles

(mediasPorNivel = tapply(datos$Respuesta, datos$Tratamiento, mean))

# Cuantos elementos hay en cada nivel

(replicas = table(datos$Tratamiento) )

# Ya podemos  calcular la suma de cuadrados del modelos

(SSmodelo = sum( replicas * (mediasPorNivel-mediaDatos)^2  ) )

# Para calcular la suma residual vamos a crear un vector que nos dice,
# para cada fila, cual es el número de nivel del factor que le corresponde.

numeroNivel = as.numeric(datos$Tratamiento)

# Y lo usamos para calcular la suma de cuadrados residual

(SSresidual=sum( ( datos$Respuesta -  mediasPorNivel[numeroNivel] )^2 ) )

# La identidad ANOVA es la coincidencia entre los dos siguientes numeros:

SStotal
SSmodelo + SSresidual

# Ahora podemos calcular el estadistico

(Estadistico = ( SSmodelo / (k - 1) ) / ( SSresidual / ( N - k ) ))

# Y el p-valor:

(pValor=1-pf(Estadistico,df1= k-1, df2= N-k ))

##############################
# Representacion grafica.
##############################

# Boxplots paralelos de los datos
par(font.axis=2, cex.axis=1.5, lwd=2)
boxplot(datos$Respuesta ~ datos$Tratamiento, col=terrain.colors(k), notch = TRUE)

#############################################
# Coeficiente de correlacion.
#############################################

# El coeficiente de correlacion lineal es:

(R2 = SSmodelo / SStotal)

# Mientras que el coeficiente de correlacion lineal ajustado es:

(adjR2 = 1 - ((SSresidual / (N - k)) / (SStotal / (N - 1))))

##################################################
# Ahora vamos a obtener los mismos resultados
# usando las funciones lm,  anova y summary:
##################################################

datos.lm = lm(Respuesta ~ Tratamiento, data = datos)

anova(datos.lm)

summary(datos.lm)

