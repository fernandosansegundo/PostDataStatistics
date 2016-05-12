# Es MUY IMPORTANTE reiniciar la sesión de R antes.

      rm(list=ls())  
      library(knitr)   
      
      
      #######################################
      Tut02_py_VolAreaEsfera = FALSE
      Tut02_py_VarianzaEdades = FALSE
      
      Tut02_py_VolAreaEsfera = TRUE
      purl("Tutorial-02-py.Rnw", output="./code/Tut02-py-VolAreaEsfera.py", documentation = 0)
      Tut02_py_VolAreaEsfera = FALSE
      
      Tut02_py_VarianzaEdades = TRUE
      purl("Tutorial-02-py.Rnw", output="./code/Tut02-py-VarianzaEdades.py", documentation = 0)
      Tut02_py_VarianzaEdades = FALSE
      #######################################
      
      
      
      
      
      
      
      

      fichero = "Tutorial-00-py.Rnw"
      knit2pdf(input=fichero, encoding="UTF-8")
      
#       fichero = "Tutorial-01.Rnw"
#       knit2pdf(input=fichero, encoding="UTF-8")
      
      
      fichero = "Tutorial-02-py.Rnw"
      knit2pdf(input=fichero, encoding="UTF-8")
      
      fichero = "Tutorial-03-py.Rnw"
      knit2pdf(input=fichero, encoding="UTF-8")
      