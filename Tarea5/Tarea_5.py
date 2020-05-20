# -*- coding: utf-8 -*-
"""
Created on Wed May 20 14:57:58 2020

@author: Antonio
"""


"""
El tipo de triangulo de cada quinteto de datos.
El área de cada triangulo escaleno.
Las estadísticas finales:
Número de triángulos isósceles.
 El porcentaje de triángulos equiláteros.
El área total del terreno procesado
"""

T_equilatero = 0
T_isoceles = 0
T_escaleno = 0
T_triangulos = 0
T_area = 0

for i in range(3):
    a, b, c = input(f"porfavor ingrese los datos del triangulo {i+1} separados por un espacio ").split();
    base = input("porfavor ingrese la medida de la base ");
    
    while base != a and base != b and base != c:
        base = input("la base tiene que ser igual a uno de los lado porfavor intente nuevamente ");   
    
    h = float(input("ingrese la altura "));
    area = (float(base) * h) / 2;
    
    if a == b == c:
        T_equilatero += 1;
        T_triangulos += 1;
        T_area += area;
    elif a == b or b == c or c == a:
        T_isoceles += 1;
        T_triangulos += 1;
        T_area += area;
    elif a != b != c:
        T_escaleno += 1;
        T_triangulos += 1;
        T_area += area;

Pescaleno = (T_escaleno / T_triangulos)*100
print (f"la cantidad de triangulos isoceles entregados fue de: {T_isoceles}\n");
print (f"el {Pescaleno}% de los triangulos fueron escalenos \n");
print (f"el area total del los angulos entregados fue de {T_area}m al cuadrado");


