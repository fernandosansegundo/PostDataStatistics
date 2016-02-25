## ---- ejercicio11sol
# Limpieza inicial
rm(list=ls())

# Generamos las 24000 tiradas del dado
dado24000 = sample(1:36, 24000, replace = TRUE)

# Los agrupamos en partidas cada 24 tiradas.
deMere2 = matrix(dado24000, ncol = 24, byrow = TRUE)

# Localizamos las apariciones del 36 (representa 6 doble).
es36 = (deMere2 == 36)

# Contamos cuantas apariciones del 36 hay en cada partida.
cuantos36 = rowSums(es36)

# Localizamos aquellas partidas con al menos un 36.
partidasGanadoras = (cuantos36 > 0)

# Y medimos la proporcion de partidas ganadoras.
(proporcion = table(partidasGanadoras)/length(partidasGanadoras))
