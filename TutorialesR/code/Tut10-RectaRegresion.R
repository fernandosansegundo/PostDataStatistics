####################################################
# www.postdata-statistics.com
# POSTDATA. Introducción a la Estadísitica
# Tutorial-10.  
#
# La recta de regresion lineal
# de dos vectores x e y.
# 
# El fichero no funcionara si no introduces los 
# dos vectores de datos, o los lees de un fichero.
#
################################################################

rm(list=ls())

# Descomenta estas lineas si las usas.
#(x = c())  
#(y = c())


# Si los vas a leer de un fichero csv con dos columnas,
# en el que cada vector ocupa una columna, descomenta y 
# completa las opciones de estos 4 comandos.
# Recuerda que el fichero debe estar en la carpeta datos
# de tu directorio de trabajo.
# Si el fichero csv no tiene ese formato tendras que hacer
# mas cambios en este codigo, de forma manual.

#datos = read.table(file="./datos/", sep=" " ,dec="." ,header=TRUE)
#x = datos[ ,1]
#y = datos[ ,2]

# Calculamos la longitud y comprobamos que coincidan
(n = length(x))
if(n != length(y)) warning("LAS LONGITUDES NO COINCIDEN")


# Dibujamos el diagrama de dispersión.
plot(x, y, lwd=2, col="red", cex.lab=2, cex.axis=1.5)
box(lwd=3)

# Calculamos las medias, cuasivarianzas y covarianza

(barX = mean(x))
(barY = mean(y))

(varX = var(x))
(varY = var(y))

(covXY = cov(x,y))

# Ahora los coeficientes de la recta de regresion:

(b1 = cov(x,y)/var(x))
(b0 = mean(y) - mean(x) * b1)

# Dibujamos la recta:

abline(b0, b1, lwd=2, col="blue")

# Calculamos el coeficiente de correlacion

(r = cor(x,y))

# Vamos a calcular los terminos de la descomposicion ANOVA

#Empezamos por los valores que predice la recta

(yRecta = b0 + b1 * x )

# Ahora los residuos

(residuos = y - yRecta)

# Y los terminos de ANOVA son

# SS total

(SSTotal = (n - 1) * var(y))

# EC, el error cuadratico.
# Tambien se llama SS error, o  residual.

(EC = sum(residuos^2))

# SS del modelo
# dispersion explicada por la recta
(SSModelo = sum((yRecta - mean(y))^2))

# Comprobacion de la identidad ANOVA
SSTotal
EC + SSModelo

