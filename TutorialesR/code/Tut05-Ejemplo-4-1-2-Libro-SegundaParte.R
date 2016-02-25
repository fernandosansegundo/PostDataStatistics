rm(list = ls())
set.seed(2014)

pintarCirculo = function(){
plot(c(seq(-1, 1, length.out = 1000), rep(1, 1000), seq(-1, 1, length.out = 1000), rep(-1, 1000))
     , c(rep(-1, 1000), seq(-1, 1, length.out = 1000),rep(1, 1000),seq(-1, 1, length.out = 1000)),
     ,xlab="", ylab="", bty="n")
curve(sqrt(1-x^2),from = -1,to = 1, lwd=3, col="blue", add=TRUE)
curve(-sqrt(1-x^2),from = -1,to = 1, lwd=3, col="blue",add = TRUE)
}
pintarCirculo()


# Vamos a lanzar n puntos al interior de un cuadrado de lado 2.
n = 10000

# En realidad, los vamos a elegir de entre los nodos de una malla rectangular 
# de n x n puntos superpuesta sobre el cuadrado.

# Construyo las coordenadas x de los puntos de la malla. 
valoresx = seq(-1, 1, length.out = n +1 )
head(valoresx)
tail(valoresx)

# Y sus coordenadas y
valoresy = seq(-1, 1, length.out = n + 1)

#points(rep(valoresx,n+1),rep(valoresy, rep(n+1,n+1)), pch="+", cex=1.2, col="red")


# Los puntos se obtienen eligiendo su coordenadas con sample.
x = sample(valoresx, n, replace = TRUE)
y = sample(valoresy, n, replace = TRUE)

points(x,y, cex=1, col="blue", pch="+")

# Y ahora me quedo sólo con los del círculo
enCirculo = ( x^2 + y^2 < 1)

xC = x[enCirculo]
yC = y[enCirculo]
pintarCirculo()
points(xC,yC, pch = "+", cex=1.5)


A = (0 < xC) & (xC < 1/2)
xA =xC[A]
yA =yC[A]
head(xA)

points(xA, yA, col="red", pch="+", cex=1)


(pA = sum(A) / sum(enCirculo))

pi * pA 


