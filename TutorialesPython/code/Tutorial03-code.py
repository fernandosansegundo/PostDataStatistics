# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 18:19:55 2016

@author: Fernando San Segundo
"""

## ---- Tut03-probabilidad
########################################################
# www.postdata-statistics.com
# POSTDATA. Introducción a la Estadística
# Tutorial 03.  
# Comandos Python del tutorial.
########################################################

## ---- chunk01

import random as rnd

rnd.seed(2016)

a = 20

b = 80

n = 100

datos = [rnd.randrange(a, b + 1) for _ in range(0, n)]

print(datos)

## ---- chunk02

muchosUnos = [1,1,1,1,1,1,1,1,1,2]

muestra = [rnd.choice(muchosUnos) for _ in range(0, 100)]

print(muestra)

## ---- Ejercicio01
import random as rnd

rnd.seed(2016)

caja = 35 * [1] + 15 * [2] + 10 * [3] + 10 * [4] + 30 * [5] 

print(caja)

n = 20

sorteo1 =  [rnd.choice(caja) for _ in range(0, n)]
print(sorteo1)

sorteo2 = rnd.sample(caja, n) 
print(sorteo2)


import collections as cl

sorteo1_counter = cl.Counter(sorteo1)
tablaFreqAbs1 = sorteo1_counter.most_common()
tablaFreqAbs1.sort()
valoresUnicos1 =  [item[0] for item in tablaFreqAbs1]
freqAbs1 =  [ item[1] for item in tablaFreqAbs1]
print(freqAbs1)
freqRel1 = [item/n for item in freqAbs1]
print(freqRel1)


sorteo2_counter = cl.Counter(sorteo2)
tablaFreqAbs2 = sorteo2_counter.most_common()
tablaFreqAbs2.sort()
valoresUnicos2 =  [item[0] for item in tablaFreqAbs2]
freqAbs2 =  [ item[1] for item in tablaFreqAbs2]
print(freqAbs2)
freqRel2 = [item/n for item in freqAbs2]
print(freqRel2)


sorteo2a = rnd.sample(caja, 1000) 


## ---- chunk03

import random as rnd
rnd.seed(2016)

partidas = []
for i in range(0, 1000):
    partida = []
    for j in range(0, 4):
        partida.append(rnd.randrange(1, 7))
    partidas.append(partida)

print(partidas[0:10])



## ---- chunk04

import random as rnd
rnd.seed(2016)

partidas = [[rnd.randrange(1, 7) for _ in range(0, 4)] for _ in range(0, 1000) ]

print(partidas[0:10])

## ---- chunk05

partidasGanadoras = []
for partida in partidas:
    if 6 in partida:
        partidasGanadoras.append(True)
    else:
        partidasGanadoras.append(False)


print(partidasGanadoras[0:10])

## ---- chunk06

import collections as cl
ganadorasCounter = cl.Counter(partidasGanadoras)
freqGanadoras = ganadorasCounter.most_common()
print(freqGanadoras)

## ---- chunk07

sum(partidasGanadoras)

## ---- chunk08

proporcionGanadoras = sum(partidasGanadoras) / len(partidasGanadoras)
print(proporcionGanadoras)

















