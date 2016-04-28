## ----setup, echo=FALSE, cache=FALSE--------------------------------------
## numbers >= 10^5 will be denoted in scientific notation,
## and rounded to 2 digits
options(scipen = 2, digits = 3, cache=FALSE)

## ----echo=FALSE, eval=FALSE, results='hide', message=FALSE, error=TRUE, warning=FALSE----
## jupyterCol = "#ffffe6"
## codeColor = "#e6f7ff"
## python01=TRUE
## #library(knitr)
## # setwd("~/Dropbox/PostDataFernando/TutorialesPython")
## # source("~/Dropbox/Code/R/raptor/raptor.R")
## # raptor("Tutorial-04-py.Rnw", language = "python", pdfOverwrite = TRUE)
## # purl("Tutorial-04-py.Rnw", output="./code/prueba.py")

## ----raptor="python"-----------------------------------------------------
dado1 = range(1,7)
print(dado1)

## ----raptor="python"-----------------------------------------------------
dado2 = range(1,7)

## ----raptor="python"-----------------------------------------------------
suma = [d1 + d2 for d1 in dado1 for d2 in dado2]
print(suma)

## ----raptor="python"-----------------------------------------------------
import collections as cl
sumaCounter = cl.Counter(suma)
recuentoValoresSuma = sumaCounter.most_common()
recuentoValoresSuma.sort()
print(recuentoValoresSuma)

## ----raptor="python"-----------------------------------------------------
n = len(suma)
print("n=", n)
probabilidadesSuma = [[item[0], item[1]/n] for item in recuentoValoresSuma]
print("probabilidadesSuma=", probabilidadesSuma)

## ----raptor="python"-----------------------------------------------------
print(4/36)

## ----raptor="python"-----------------------------------------------------
X = [[2, 1/5], [4, 1/10], [7, 1/10], [8, 2/5], [11, 1/5]]

## ----raptor= "python"----------------------------------------------------
media = sum([x[0] * x[1] for x in X])
print("media de X = {0:0.4f}".format(media))

## ----raptor="python"-----------------------------------------------------
varianza = sum([(x[0] - media)**2 * x[1] for x in X])
print("varianza = {0:0.4f}".format(varianza))

## ----raptor="python"-----------------------------------------------------
import math as m
sigma = m.sqrt(varianza)
print("desviacion tipica = {0:0.4f}".format(sigma))

## ----raptor="python"-----------------------------------------------------
import random as rnd
rnd.seed(2016)
n = 10000
dado1 = [rnd.randrange(1, 7) for _ in range(0, n)]
dado2 = [rnd.randrange(1, 7) for _ in range(0, n)]
X = [dado1[_] + dado2[_] for _ in range(0, n)]
W = [3 * x - 4 for x in X]

## ----raptor="python"-----------------------------------------------------
import numpy as np
mediaW = np.mean(W)
print("media de W= {0:0.4f}".format(mediaW))

## ----raptor= "python"----------------------------------------------------
V = [x**2 for x in X]
mediaV = np.mean(V)
print("media de V= {0:0.4f}".format(mediaV))

## ----raptor="python"-----------------------------------------------------
valoresX = range(2, 13)
probabilidadesX = list(range(1,7)) + list(range(5, 0, -1))
probabilidadesX = [p/36 for p in probabilidadesX]
muX = sum([valoresX[i] * probabilidadesX[i] for i in range(0, len(valoresX))])
print("Media de X = {0:0.4f}".format(muX))
varX = sum( [(valoresX[i] - muX)**2 * probabilidadesX[i] for i in range(0, len(valoresX))])
print("Varianza de X = {0:0.4f}".format(varX))

## ----raptor="python"-----------------------------------------------------
valoresV = [x**2 for x in valoresX]
probabilidadesV = probabilidadesX
muV = sum([valoresV[i] * probabilidadesV[i] for i in range(0, len(valoresV))])
print("Media de V = {0:0.4f}".format(muV))

## ----raptor="python"-----------------------------------------------------
print("varX ={0:0.4f}".format(varX))
print("muV - (muX)^2 ={0:0.4f}".format(muV - (muX)**2))

## ----raptor="python"-----------------------------------------------------
X = [[2, 1/5], [4, 1/10], [7, 1/10], [8, 2/5], [11, 1/5]]
valores = [item[0] for item in X]
probabilidades = [item[1] for item in X]
print(probabilidades)

## ----raptor="python", purl=pthon01---------------------------------------
FdistX = np.cumsum(probabilidades).tolist()
print(FdistX)

## ----raptor="python"-----------------------------------------------------
k = len(valores)
print("\nTabla de la variable aleatoria X:\n")
linea = "_" * 75
print(linea)
print("Valor x | Probabilidad p | Fun. de dist. F(x) |")
print(linea)
for i in range(0, k):
    print("{0:0.4f} | {0:0.4f} | {0:0.4f} |\
    ".format(valores[i], probabilidades[i], FdistX[i]))
print(linea)

## ----fig.width=4, fig.height=4-------------------------------------------
barplot(probabilidades, names.arg=valores, col="lightseagreen")

## ----fig.width=4, fig.height=4-------------------------------------------
barplot(cumsum(probabilidades), names.arg=valores, col="lightseagreen")

## ----fig.width=6, fig.height=4-------------------------------------------
valoresX = 2:12
probabilidadesX = c(1:6,5:1) / 36

##  NO MODIFIQUES EL RESTO DEL CODIGO ##

graficoEscalera = function(valores, probabilidades ){
  probabilidades = probabilidades/sum(probabilidades)
  y0 = c(0,cumsum(probabilidades), 1)
  x0 = c(min(valores)-1,valores, max(valores)+1)
  xA = x0[-length(x0)]
  xB = x0[-1]
  yA = y0[-length(y0)]
  plot(x0, y0, type="n", xlab="valores", ylab="probabilidades", las=3, xaxt="n")
  segments(xA,yA,xB,yA, lwd=4, col="red")
  points(xA, yA, pch=16, col="red", cex=1.5)
  axis(1, at=xA,   labels=xA)
  segments(valores, yA[-length(yA)] , valores, yA[-1], lty=2, col="blue", lwd=4)
}
graficoEscalera(valores, probabilidades)

## ----raptor="python"-----------------------------------------------------
import random as rnd
rnd.seed(2016)
n = 10000
dado1 = [rnd.randrange(1, 7) for _ in range(0, n)]
dado2 = [rnd.randrange(1, 7) for _ in range(0, n)]
suma = [dado1[_] + dado2[_] for _ in range(0, n)]
import collections as cl
sumaCounter = cl.Counter(suma)
freqAbsolutaSuma = sumaCounter.most_common()
freqAbsolutaSuma.sort()
print(freqAbsolutaSuma)
freqRelativaSuma = [[item[0], item[1]/n] for item in freqAbsolutaSuma]
print("frecuencias relativas de la suma=")
print(freqRelativaSuma)

