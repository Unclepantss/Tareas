# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 20:06:53 2020

@author: Antonio
"""


print("buenas tardes, bienvenido al calculador de ecuaciones cuadraticas");
import math;

A = float(input("porfavor ingrese la incognita cuadratica:"));
B = float(input("porfavor ingrese la incognita lineal:"));
C = float(input("porfavor ingrese el termino independiente:"));

discriminante = (B*B) -4 * A * C ;
print ("el discriminante es igual a", discriminante, "por lo tanto");

if discriminante == 0:
    print ("la ecuacion tiene solamente una solucion");
    resultado = (-B) / (2 * A);
    print ("X es igual a ", resultado);
elif discriminante > 0:
    print ("la ecuacion tiene dos soluciones");
    resultado = (-B + math.sqrt(discriminante)) / (2 * A);
    resultado2 = (-B - math.sqrt(discriminante)) / (2 * A);
    print ("X1 es igual a", resultado , "\nX2 es igual a", resultado2);
else:   
    print ("la ecuacion no tiene soluciones reales");     
    resultado = (-B + (discriminante ** 0.5));
    resultado2 = (-B - (discriminante ** 0.5));
    print("X1 es igual a", complex (resultado) ,"/", (2 * A));
    print("X2 es igual a", complex (resultado2),"/", (2 * A));