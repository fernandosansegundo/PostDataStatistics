# Es MUY IMPORTANTE reiniciar la sesión de R antes.

      rm(list=ls())  
      library(knitr)   


            
#       (fichero = paste("000-CursoEstadistica", ".tex", sep="",collapse=""))      
#       knit2pdf(input=fichero, encoding="UTF-8")
          
      fichero = "Tutorial-00.Rnw"
      knit2pdf(input=fichero, encoding="UTF-8")
      
      fichero = "Tutorial-01.Rnw"
      knit2pdf(input=fichero, encoding="UTF-8")
      
      fichero = "Tutorial-02.Rnw"
      knit2pdf(input=fichero, encoding="UTF-8")
      
            
      for(i in 2:9){
        (numTutorial = paste("0",i,collapse="", sep=""))
        (fichero = paste("Tutorial-", numTutorial, ".Rnw", sep="",collapse=""))
        knit2pdf(input=fichero, encoding="UTF-8")
      }
 
Sys.setlocale("LC_ALL", "C")      
           
      for(i in 10:13){
        (numTutorial = i)
        (fichero = paste("Tutorial-", numTutorial, ".Rnw", sep="",collapse=""))
        knit2pdf(input=fichero, encoding="UTF-8")        
      }  

