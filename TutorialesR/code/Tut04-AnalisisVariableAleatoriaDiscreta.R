########################################################
# www.postdata-statistics.com
# POSTDATA. Introducción a la Estadística
# Tutorial 04.  
# Plantilla de comandos R para el estudio de una variable 
# aleatoria discreta X con  un número finito de valores.
########################################################
rm(list = ls())

# La tabla de densidad de la variable se debe definir mediante los 
# dos siguientes vectores (de la misma longitud)
# El fichero NO FUNCIONARÁ hasta que se hayan definido ambos vectores.
valoresX = 
probabilidadesX = 


# Representación gráfica de la densidad
barplot(probabilidadesX, names.arg=valoresX, col="lightseagreen")

# Cálculo de la media teórica de la variable:
(muX = sum(valoresX * probabilidadesX) )

# Cálculo de la varianza teórica y de la desviación típica.
(varianzaX = sum((valoresX - muX)^2 * probabilidadesX) )
(sigmaX = sqrt(varianzaX) )


# Tabla de distribución de probabilidad acumulada.  
rbind(valoresX,cumsum(probabilidadesX))



# Función de distribución de X
FdistribX = function(x, valores = valoresX, probs = probabilidadesX){
  if(x >= min(valores)){
    colocaX = max(which(valores <= x))
    return( cumsum(probs)[colocaX])    
  } else {
    return(0)
  }
}


# Representación de esa función en un gráfico de escalera
graficoEscalera = function(valores = valoresX, probs = probabilidadesX){
  probs = probs /sum(probs)
  y0 = c(0,cumsum(probs), 1)
  x0 = c(min(valores)-1,valores, max(valores)+1)
  xA = x0[-length(x0)]
  xB = x0[-1]
  yA = y0[-length(y0)]
  plot(x0, y0, type="n", xlab="valores", ylab="probabilidades", las=3, xaxt="n")
  segments(xA,yA,xB,yA, lwd=4, col="red")
  points(xA, yA, pch=16, col="red", cex=1.5)
  axis(1, at=xA, labels=xA)
  segments(valores, yA[-length(yA)] , valores, yA[-1], lty=2, col="blue", lwd=4)
}
graficoEscalera(valoresX, probabilidadesX)

# Para generar valores aleatorios de X

randomX = function(valores = valoresX, probs = probabilidadesX, n=1){
  sample(valores, size = n, replace = TRUE, prob = probs)
}

