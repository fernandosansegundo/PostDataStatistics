
    #######################################################################
    # media poblacion normal,varianza desconocida, muestra grande  n>30.
    #######################################################################
    
    rm(list=ls())
    
    # Numero de elementos en la muestra
    (n= ) #SE SUPONE QUE LA MUESTRA ES GRANDE
    
    # Media muestral
    (xbar=)
    
    # Cuasidesviacion tipica muestral (o sigma si fuera conocida)
    (s= )
    
    # Valor a contrastar de la media (aparece en la hipotesis nula)
    (mu0= )
    
    ##Nivel de significacion
    (nc=  )
    (alfa=1-nc)

    ##############################################################
    # Si necesitas fabricar la muestra, descomenta las siguientes 
    # tres lineas
    ##############################################################
    
    # library(MASS)
    # (muestra=round(as.vector(mvrnorm(n,mu=x_barra,Sigma=s^2,empirical=T)),3))
    # mean(muestra); sd(muestra); length(muestra) #esto es una comprobacion
    
    
    
    
    
    
    
    
    
    
    
    
    
    # Calculo del estadistico del contraste
    (Estadistico=(xbar-mu0)/(s/sqrt(n)))
    
    # Calculo del p-valor
    TipoContraste=1 # 1 para Hip. alternativa mu > mu0, 2 para mu < mu0, 3 para mu = mu0
    
    if(TipoContraste==1){(pValor=1-pnorm(Estadistico))}
    if(TipoContraste==2){(pValor=pnorm(Estadistico))}
    if(TipoContraste==3){
      if(xbar>mu0)(pValor=2*(1-pnorm(Estadistico)))
      else(pValor=2*(pnorm(Estadistico)))
    }
    
    
