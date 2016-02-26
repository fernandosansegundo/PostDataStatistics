# Es MUY IMPORTANTE reiniciar la sesión de R antes.

      rm(list=ls())  
      library(knitr)   

      fichero = "Tutorial-00-py.Rnw"
      knit2pdf(input=fichero, encoding="UTF-8")
      
#       fichero = "Tutorial-01.Rnw"
#       knit2pdf(input=fichero, encoding="UTF-8")
      
      
      fichero = "Tutorial-02-py.Rnw"
      knit2pdf(input=fichero, encoding="UTF-8")
      