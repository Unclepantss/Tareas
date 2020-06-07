# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 12:48:09 2020

@author: Antonio
"""

entrada = open("secuencias.txt","r");
linea = entrada.readline().strip();
valor = 0
N = 1
for linea in entrada:
    datos = linea.split(",");
    num = int(datos[0])
    if num > valor:
       valor = num
    elif num < valor:
        valor = num
        N += 1
print(f"las secuencias existentes en este archivo son {N}")