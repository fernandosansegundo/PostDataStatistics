# Limpieza inicial
rm(list=ls())

# Generamos las 4000 tiradas del dado
dado4000 = sample(1:6, 4000, replace = TRUE)

# Los agrupamos en partidas cada cuatro tiradas.
deMere1 = matrix(dado4000, ncol = 4, byrow = TRUE)

# Localizamos las apariciones del 6.
esSeis = (deMere1 == 6)

# Contamos cuantas apariciones del seis hay en cada partida.
cuantosSeis = rowSums(esSeis)

# Localizamos aquellas partidas con al menos un 6.
partidasGanadoras = (cuantosSeis > 0)

# Y medimos la proporcion de partidas ganadoras.
(proporcion = table(partidasGanadoras)/length(partidasGanadoras))
