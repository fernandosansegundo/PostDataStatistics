####################################################
# www.postdata-statistics.com
# POSTDATA. Introducción a la Estadística
# Tutorial-13.
#
# Fichero de instrucciones R para construir un METODO
# CLASIFICADOR basado en regresión logistica, con variable
# respuesta dicotomica Y y variable explicativa continua X.
# Se parte de un fichero de datos (tipo csv). El fichero contiene
# en su primera columna los valores de la variable explicativa y
# en la segunda columna los valores de la variable respuesta.
# Esta variable respuesta deberá necesariamente ser un factor
# con dos niveles. Si el orden de esas dos columnas es el contrario
# se pueden intercambiar mediante el valor de la variable colFactor.
#############################################################
# INSTRUCCIONES:
#   Fija el directorio de trabajo (con la subcarpeta datos con el csv.)
#############################################################

##################################
## Lectura del fichero de datos.
## No olvides los parametros de read.table (sep, dec, etc.)

datosFichero = read.table("../datos/", header = TRUE, sep=",")
head(datosFichero)

######################################
# Fijamos los nombres de las variables
# y creamos un data.frame con ellos.

colX = 1
if(colX == 1){
  X = datosFichero[ , 1]
  Y = datosFichero[ , 2]
} else {
  X = datosFichero[ , 2]
  Y = datosFichero[ , 1]
}
datos = data.frame(X, Y)

########################################################
# Construccion del modelo logistico.

glmXY = glm(Y ~ X, family = binomial(link = "logit"), data = datos)

(summGlmXY = summary(glmXY))

datos$probs = glmXY$fitted.values

cp = 0.5
clasificacion = ifelse(glmXY$fitted.values > cp, 1, 0)
## Cargamos la libreria caret

library(caret)

clasifUmbral = function(glmXY, cp){
  Y = glmXY$y
  clasificacion = ifelse(glmXY$fitted.values > cp, 1, 0)
  clasificacion_f = factor(clasificacion, levels = 1:0)
  Y_f =  factor(Y, levels = 1:0)
  confMat = confusionMatrix(clasificacion_f, Y_f)
  return(c(confMat$byClass[1], confMat$byClass[2], confMat$overall[1]))
}


cp_v = seq(1, 0, by = -0.001)

sens = sapply(cp_v, FUN = function(cp){clasifUmbral(glmXY, cp)[1]})

espec = sapply(cp_v, FUN = function(cp){clasifUmbral(glmXY, cp)[2]})

plot(cp_v, sens, type="l", col="red", lwd=3, lty=1, xlab="punto de corte", ylab="")

points(cp_v, espec, type="l", col="blue", lwd=3, lty=2)

legend(x="bottom", legend=c("sensibilidad", "especificidad"),
       col = c("red", "blue"), bty=1, lty=c(1,2),lwd=3)
accur = sapply(cp_v, FUN = function(cp){clasifUmbral(glmXY, cp)[3]})

plot(cp_v, accur, type="l", col="black", lwd=3, lty=1,
     xlab="punto de corte", ylab="Tasa de aciertos")

library(ROCR)
