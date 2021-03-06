########################################################
# www.postdata-statistics.com
# POSTDATA. Introducción a la Estadística
# Tutorial 02.  
# Plantilla de comandos R para Estadística Descriptiva
# Una variable cuantitativa, datos no agrupados.
########################################################


# ATENCION: para empezar a trabajar es necesario establecer 
# el directorio de trabajo en la siguiente línea de código. 
# y el nombre del fichero (más opciones) en la línea 18.
# De lo contrario este fichero no funcionará.
setwd("")

# Leemos el fichero de datos, y lo guardamos en la variable vectorDatos.
# El fichero debe estar en la subcarpeta datos del directorio de trabajo.
# Debes introducir el nombre del fichero. Se supone que los datos están 
# en la primera columna del fichero. Si no es así, debes modificar la 
# siguiente orden, indicando la columna que contiene los datos.
vectorDatos = read.table(file="./datos/", header=TRUE)[,1]

# Calculamos máximo, minimo y rango.
( minimo = min(vectorDatos) )
( maximo = max(vectorDatos) )
( rango = range(vectorDatos) )

# Determinamos la longitud del vector de datos.
( n = length( vectorDatos ) )

# Hallamos las tablas de frecuencias: 
# (1) absoluta,  (2) relativa,
# (3) acumulada, (4) acumulada relativa.
( tablaFrecAbs = table(vectorDatos) )
( tablaFrecRel = tablaFrecAbs / n )
( tablaFrecAcu = cumsum(tablaFrecAbs)  )
( tablaFrecRelAcu = cumsum(tablaFrecRel) )

# Dibujamos un gráfico de barras de las frecuencias.
barplot(tablaFrecAbs, col = heat.colors(15))

# Y el diagrama de caja.
boxplot(vectorDatos)

# Calculo de la media aritmética,
( media = mean(vectorDatos))

# la cuasivarianza muestral,
( varMuestral = var(vectorDatos))

# y la cuasidesviación típica.
( desvTipMuestral = sd(vectorDatos))

# La varianza y desviación típica poblacionales
# se obtienen así:
( varPobl= ( (n-1) / n ) * varMuestral )
( desvTipPobl = sqrt( varPobl ) )

# Calculamos la mediana.
( mediana = median(vectorDatos))

# La función summmary muestra la media y varias
# medidas de posición (cuartiles).
summary(vectorDatos)

# El rango intercuartílico.
( rangoIntCuart= IQR(vectorDatos))

# Y algunos percentiles: 5%, 15%, 58% y 75%. 
# Si deseas otros percentiles, modifica los 
# valores del vector.

( percentiles = quantile(vectorDatos, c(0.05, 0.15, 0.58, 0.75)) )

# Fin del fichero


