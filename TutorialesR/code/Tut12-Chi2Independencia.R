####################################################
# www.postdata-statistics.com
# POSTDATA. Introducción a la Estadísitica
# Tutorial-12.
#
# Fichero de instrucciones R para calcular un contraste 
# chi-cuadrado de independencia, a partir de una tabla de 
# contingencia.
#
#############################################################
# INSTRUCCIONES:
# Introducir la tabla de contingencia 
#   de una de las siguientes maneras:
#   + un vector por cada fila.
#   + un vector por cada columna.
#   + usando un fichero csv. En este caso no olvides elegir el 
#     directorio de trabajo (con la subcarpeta datos con el csv.)
# Una vez elegida cual de estas maneras vas a usar tendras que
# descomentar algunas lineas de este fichero para que funcione.
#############################################################

# La tabla de contingencia se puede introducir 
# como una matriz, por filas o por columnas, 
# eligiendo el valor adecuado de byrow.

# tablaObservada = matrix( c( ),  nrow= , byrow = )

# O a partir de un fichero csv. 
# En tal caso recuerda que debes fijar el directorio de trabajo.
# setwd("")
# y ahora cargar los datos con read.table. Elige el tipo de separador, e indica  
# si la primera fila contienen los nombres de columnas (con header=TRUE), y si la 
# primera fila contienen los nombres de filas (con row.names=1)

# (tablaObservada = as.matrix(read.table(file="", header=TRUE, sep=",", row.names=1)))
# Calculamos el numero de filas y columnas
(nFilas = nrow(tablaObservada))
(nColumnas = ncol(tablaObservada))

# y también el numero total de observaciones.
(n = sum(tablaObservada) )

# Ponemos nombres a las filas y columnas de la tabla.
# En cualquier caso, si lo prefieres, puedes introducir tus vectores 
# de nombres para filas y columnas. Aqui, incluimos un ejemplo con 
# la  función paste para que veas como puedes utilizarla. 
(colnames(tablaObservada) = paste("Col", 1:(nColumnas), sep=""))
(rownames(tablaObservada) = paste("Fila", 1:(nFilas), sep=""))

# Chequeamos el resultado
tablaObservada

# Calculamos los valores marginales
(tablaObservadaMarg = addmargins(tablaObservada))

# que guardamos en vectores de esta manera.
(marginalesFilas = margin.table(tablaObservada, margin=1) )
(marginalesColumnas = margin.table(tablaObservada, margin=2) )

# Ahora vamos a construir la tabla de valores esperados,
# usando el producto matricial de los dos vectores de
# sumas marginales.

dim(marginalesFilas)=c(nFilas, 1)
tablaEsperada = (marginalesFilas %*% marginalesColumnas) / n

# Copiamos los nombres de filas y columnas de la tabla observada
colnames(tablaEsperada)=colnames(tablaObservada)
rownames(tablaEsperada)=rownames(tablaObservada)

# Ahora calculamos el estadistico del contraste chi cuadrado:
(Estadistico = sum((tablaObservada - tablaEsperada)^2 / tablaEsperada))

# Y el correspondiente p-valor:
(pValor = 1 - pchisq(Estadistico, df=(nFilas - 1) * (nColumnas - 1)))

# Los resultados deben coincidir con los de chisq.test:
(chisqTest = chisq.test(tablaObservada, correct=FALSE))

# Una de las representaciones graficas mas comunes es
# el grafico de mosaico:
mosaicplot(t(tablaObservada), col=terrain.colors(nColumnas), main="Tabla Observada Datos CIS")
pTabla0 + pTabla1 + pTabla2 + pTabla3
