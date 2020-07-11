# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 10:48:55 2020

@author: Antonio
"""

def absoluto (n): #funcion de valor absoluto
    if n < 0:
        nf = -(n);
    else:
        nf = n
    return nf;

archivo = open("Aterrizaje.txt", "r"); #apertura de archibo / recoleccion de datos
linea = archivo.readline().strip();
#distancia 1 / distancia 2
D = float(linea);
d2 = D;
va2 = 0 #valor absoluto 2
aterrizaje = False
rc = 0

for linea in archivo: #ciclo 
    v = (D - d2); 
    va = absoluto(v); #valor absoluto
    
    if va < va2 and rc == 0: #chequeo de activacion de cohetes
        comienzo = d2;
        rc += 1
    
    if va > va2 and rc > 0: #chequeo de cohetes para aterrizaje
        aterrizaje = True;
    
    d2 = D
    D = float(linea);
    va2 = va

#resumen de recoleccion de datos
print(f"el retro cohete comenzo a operarse desde {comienzo} mts de distancia");

if aterrizaje:
    print("La sonda posiblemente se estrelló en la superficie");
else:
    print("La sonda posiblemente aterrizó sin problemas");