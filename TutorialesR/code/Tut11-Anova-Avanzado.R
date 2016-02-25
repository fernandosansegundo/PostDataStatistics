####################################################
# www.postdata-statistics.com
# POSTDATA. Introducción a la Estadísitica
# Tutorial-11.
#
# Fichero de instrucciones R para calcular un contraste
# ANOVA unifactorial .
#
# Se supone que:
#  -Los datos estan en un fichero csv con dos columnas.
#  -Son datos "limpios". Es decir:
#       -cada columna corresponde a una variable.
#       -cada fila corresponde a una observación particular.
#  -Los títulos de las columnas (nombres de variables)
#   aparecen en la primera fila (y no incluyen espacios).
#  -No hay elementos ausentes: las filas están todas completas.
#  -No se supone que todos los tratamientos tengan el
#   mismo número de observaciones.
#############################################################
# INSTRUCCIONES:
# - No olvides cambiar el directorio de trabajo
#   para que sea el que contiene el fichero csv.
# - Escribe el nombre del fichero y el tipo de separador.
# - Indica que columna contiene el factor (tratamiento).
#############################################################
#rm(list=ls())

#########################################
# LECTURA DE LOS DATOS
#########################################
# Recuerda que debes fijar el directorio de trabajo.
# setwd()

#Leemos los datos del fichero
datos = read.table(file="./datos/", sep=" ", header=T)

# Descomenta esta línea para comprobar que la lectura ha sido correcta.
# View(datos)

# IMPORTANTE: introduce el número de columna ( 1 o 2 ) que contiene el factor (tratamiento).
colFactor = 1

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

# Y traducimos los niveles en numeros para facilitar su manejo.
numeroNivel = as.numeric(datos$Tratamiento)


#######################################
# TABLA ANOVA
# Usando las funciones lm y anova
#########################################

datos.lm = lm(datos$Respuesta ~ datos$Tratamiento)

anova(datos.lm)

summary(datos.lm)

#########################################
# Representacion grafica
#########################################

# Boxplots paralelos de los datos

par(font.axis=2,cex.axis=1.5,lwd=4)
boxplot(datos$Respuesta ~ datos$Tratamiento,col=terrain.colors(k),notch=TRUE)
par(font.axis=2,cex.axis=1,lwd=1)
# Histogramas de cada uno de los grupos
par(mfrow=c(k%/%2+k%%2,2),font.axis=1.5,cex.axis=1.5,lwd=2,font.lab=2,cex.lab=1.5)
histogramas = tapply(datos$Respuesta,datos$Tratamiento, hist, breaks=10,
       main="", ylab="Frecuencia", xlab="", col=heat.colors(10))
par(mfrow=c(1,1))
#########################################
# Gráficos para el análisis mediante
# residuos de las hipótesis del modelo.
#########################################

datos.aov = aov(datos$Respuesta ~ datos$Tratamiento, datos)
par(mfrow=c(2,2), cex.axis=1.5, lwd=2, font.lab=1.5)
plot(datos.aov)
par(mfrow=c(1,1))
#########################################
# Comparaciones a posteriori, dos a dos
#########################################
# En caso de un Anova significativo, podemos comparar los grupos dos a dos
# Los p-valores de las comparaciones se obtienen con este comando:

(ptt=pairwise.t.test(datos$Respuesta, datos$Tratamiento,
                     p.adj="bonferroni", pool.sd=FALSE))
#########################################
# REPRESENTACIONES GRAFICAS DE LOS GRUPOS
#########################################

IntervaloConfMedia=function(x,nivelConfianza){
  xbarra=mean(x)
  s=sd(x)
  n=length(x)
  alfa=1-nivelConfianza
  if(n>30){
    valCritico=qnorm(1-alfa/2)
  } else{
    valCritico=qt(1-alfa/2,df=n-1)
  }
  c(-1,1)*valCritico*s/sqrt(n)+xbarra
}

intervalos=c()
for(i in 1:k){
  intervalos=rbind(intervalos,IntervaloConfMedia(datos$Respuesta[ numeroNivel==i ],0.9))
}


(mediasMuestrales=tapply(datos$Respuesta,datos$Tratamiento, mean))
(cuasiDesvTipMuestrales=tapply(datos$Respuesta,datos$Tratamiento,sd))
(longitudesMuestrales=tapply(datos$Respuesta,datos$Tratamiento,length))
(sem=cuasiDesvTipMuestrales/sqrt(longitudesMuestrales))
#(stripchart(datos$Respuesta ~ datos$Tratamiento,method="jitter",jitter=0.05, pch=16, vert=T,plot=FALSE))
plot(c(1:k,1:k),c(intervalos[,1],intervalos[,2]),col="white",xlab="",ylab="")
arrows(1:k,intervalos[,1],1:k,intervalos[,2],angle=90,code=3,length=.1,lwd=4,col="blue")
(lines(1:k,mediasMuestrales,pch=10,type="b",cex=2))


#########################################################
# Comparaciones a posteriori, representaciones gráficas
#########################################################

library(multcomp)
datos.aov = aov(Respuesta ~ Tratamiento, datos)
attach(datos)
(glh = summary(glht(model=datos.aov, linfct = mcp(Tratamiento = "Tukey"))))
cld(glh)

numGrupos = k
par(mai=c(2, 1.5, (numGrupos-1)/2, 1))
plot(cld(glh), col=heat.colors(k))
segments((1:k) -1/5, mediasMuestrales, (1:k) + 1/5, mediasMuestrales, lty=2)
par(mai=c(1,1,1,1))

require(multcompView)
multcompBoxplot(Respuesta~Tratamiento,data=datos)

#########################################
# Descomentar para obtener un
# grafico de columnas con barras de error
# Bargraphs (se desaconseja su uso)

#  b=barplot(mediasMuestrales, ylim=c(min(intervalos)*0.8, max(intervalos)*1.2), xpd=F)
#  arrows(b, intervalos[,2], b, intervalos[,1],angle=90, code=3,lwd=3)
#  box(bty="l")

