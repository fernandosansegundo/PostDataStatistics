setwd("")

var3 = read.table(file="./datos/Tut02-var3.csv", header=TRUE)[,1]

( minimo = min(var3) )
( maximo = max(var3) )
( rango = range(var3) )

( tablaFrecAbs = table(var3) )

( n = length( var3 ) )

( tablaFrecRel = tablaFrecAbs / n )
( tablaFrecAcu = cumsum(tablaFrecAbs)  )
( tablaFrecRelAcu = cumsum(tablaFrecRel) )


barplot(tablaFrecAbs, col = heat.colors(15))

boxplot(var3)

( media = mean(var3))

( varMuestral = var(var3))

( desvTipMuestral = sd(var3))

( varPobl= ( (n-1) / n ) * varMuestral )

( desvTipPobl = sqrt( varPobl ) )

( mediana = median(var3))

summary(var3)

( rangoIntCuart= IQR(var3))

( percentiles = quantile(var3, c(0.05, 0.15, 0.58, 0.75)) )


