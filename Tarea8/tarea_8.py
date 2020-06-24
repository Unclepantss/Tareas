# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 10:59:16 2020

@author: Antonio
"""


entrada = open("FilaBanco.txt","r");
linea = entrada.readline().strip();
datos = linea.split(",");
nombre = datos[0];
apellido = datos [1];
temp = float(datos[2]);
temp2 = 0;
temp3 = 0;
Pc = 0;
for linea in entrada:
    if temp3 >= 37.5 and temp >= 37.5 and temp2 < 37.5:
        print(nombre, apellido)
        Pc += 1
    nombre = datos[0];
    apellido = datos [1];
    datos = linea.split(",")
    temp3 = temp2
    temp2 = temp
    temp = float(datos[2])
print(f"hay un total de {Pc} sospechosos")