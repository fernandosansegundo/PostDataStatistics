####################################################
# www.postdata-statistics.com
# POSTDATA. Introducción a la Estadísitica
# Tutorial-13.
#
# Fichero de instrucciones R para construir un modelo 
# sencillo de regresión logistica, a partir de un fichero 
# de datos (tipo csv). El fichero contiene en su primera columna
# los valores de la variable explicativa y en la segunda columna
# los valores de la variable respuesta. Esta variable respuesta
# deberá necesariamente ser un factor con dos niveles.
# Si el orden de esas dos columnas es el contrario se pueden 
# intercambiar mediante el valor de la variable colFactor.
#############################################################
# INSTRUCCIONES:
#   Fija el directorio de trabajo (con la subcarpeta datos con el csv.)
#############################################################

##################################
## Lectura del fichero de datos.
## No olvides los parametros de read.table (sep, dec, etc.)

datosFichero = read.table("./datos/", header = TRUE, sep=",")
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
#################################
## Diagrama de dispersion.

colores = c()
colores[datos$Y == 0] = "blue"
colores[datos$Y == 1] = "orange"
plot(datos$X, datos$Y, pch = 21, bg = colores, cex=1.3,font=2,
     xlab = "X", ylab = "Y", font.lab=2)
legend("left", c("Y = 0", "Y = 1"), pch = 21, pt.bg =  c("blue", "orange"))
box(lwd=3)

########################################################
# Funcion glm para la construccion del modelo logistico.

(glmXY = glm(Y ~ X, family = binomial(link = "logit"), data = datos))

# Con summary ampliamos la informacion del modelo:

(summGlmXY = summary(glmXY))

# Los coeficientes de la curva logistica del modelo son

(b0glm = summGlmXY$coefficients[1])
(b1glm = summGlmXY$coefficients[2])

##############################################
# Incorporamos la curva logistica a la grafica

curvaLogisticaGLM = function(x){
  return(exp(b0glm + b1glm * x)/(1 + exp(b0glm + b1glm * x)))
}

curve(curvaLogisticaGLM, from = min(X), to = max(X), 
      col="red", lwd="2", add=TRUE, lty="dashed")

###########################
# Verosimilitud del modelo

(logVerosimilitud = logLik(glmXY)[1])


(verosimilitud = exp(logVerosimilitud))

plogis(b0glm + b1glm * x0)
################################
# Devianza del modelo logistico

summGlmXY$deviance

############################
# Devianza del modelo nulo

summGlmXY$null.deviance

############################
# Estadistico G

(G = summGlmXY$null.deviance - summGlmXY$deviance) 

#######################################
# p-valor del contraste sobre beta1 = 0

(pValor = pchisq(G, lower.tail = FALSE, df=1))

#######################################
# Intervalos de confianza para beta0 y beta1

nc= 0.95

confint.default(glmXY, level = nc)
g = 10
(puntosCorte = quantile(fitted(glmXY), probs = seq(0, 1, 1/g)))
datos$claseRiesgo = cut(fitted(glmXY), breaks = puntosCorte, 
                        include.lowest = TRUE)
(n.i = table(datos$claseRiesgo))
min(n.i)
(Obs1 = with(datos, tapply(Y, INDEX = claseRiesgo, FUN = sum)) )
(Esp1 = with(datos, tapply(probs, INDEX = claseRiesgo, FUN = sum)) )
(Obs0 = n.i - Obs1)

(Esp0 = n.i -Esp1)
(HL.estadistico = sum((Obs1 - Esp1)^2/Esp1) + sum((Obs0 - Esp0)^2/Esp0))
(HL.df = length(Obs1) - 2)
(HL.pValor =  pchisq(HL.estadistico, df = HL.df, lower.tail = FALSE))
library(ResourceSelection)
(HL.test= hoslem.test(datos$Y, datos$probs, g = 10))
HL.test$statistic
HL.test$observed
HL.test$expected
