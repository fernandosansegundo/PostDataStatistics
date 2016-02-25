## ---- ejercicio12sol

# Limpieza inicial
rm(list=ls())
# Generamos las 6000 tiradas del dado
dado6000 = sample(1:6, 6000, replace = TRUE)
# Los agrupamos en partidas cada dos tiradas.
deMere1a = matrix(dado6000 , ncol = 2, byrow = TRUE)
# Localizamos las apariciones del 6.
esSeis = (deMere1a == 6)
# Contamos cuantas apariciones del seis hay en cada partida.
cuantosSeis = rowSums(esSeis)
# Localizamos aquellas partidas con al menos un 6.
partidasGanadoras = (cuantosSeis > 0)
# Y medimos la proporcion de partidas ganadoras.
(proporcion = table(partidasGanadoras)/length(partidasGanadoras))