# -*- coding: utf-8 -*-
"""
Created on Sat May 30 17:11:36 2020

@author: Antonio
"""

cables = open ("cables.txt")
linea = cables.readline().strip();
cables = linea.split(" ");

if linea == 3:
    if cable_1 == "rojo":
        print("corte el segundo cable");
    elif cable_3 == "blanco":
        print("corte el ultimo cable");
    elif cable_1 == "azul" == cable_2:
        print ("corte el segundo cable azul");
    else:
        print("corte el ultimo cable");
elif linea == 4:
    if "rojo" > 1:
        print("corte el ultimo cable")
    elif cable_4 == "amarillo" and 0 < "rojo":
        print("corte el primer cable")
    elif "rojo" == 1:
        print ("corte el segundo cable")
    elif cable_2 == cable_3 == "amarillo":
        print("corte el ultimo cable")
    else:
        print("corte el ultimo cable")   
elif linea == 5:
    if cable == "negro":
        print("corte el cuarto cable")
    elif cable_3 == "rojo":
        print("corte el tercer cable")
    elif "negro" > 1:
        print("corte el segundo cable")
    else:
        print("corte el primer cable")