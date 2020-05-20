# -*- coding: utf-8 -*-
"""
Created on Wed May 13 12:13:25 2020

@author: Antonio
"""
N = 0
x = 100
y = 0
y2 = 0
mod = N
odd = 0
for i in range(50):
    try:
        print("porfavor ingrese un valor mayor o igual a 0 \n")
        N = int(input())
        while N < 0:
            print("porfavor ingrese un valor positivo \n")
            N = int(input())
            break;
    except ValueError: ("porfavor ingrse un numero \n");
    mod = N % 2;
    if N < x:
        x = N;
        print("el nuevo numero menor es: ", x, "\n");
    if N > y:
        y2 = y; 
        y = N;
        print("el nuevo numero mayor es: ", y, "\n");
    elif N > y2 and N < y:
        y2 = N;
    if mod > 0:
        odd += N;
        
print("el numero menor del conjunto de datos fue:", x);
print("el numero mayor fue:", y);
print("el segundo mayor fue: ", y2);
print("el total de la suma de los numeros inpares fue de: ", odd);
            