# -*- coding: utf-8 -*-
"""
Created on Sat May 30 11:42:25 2020

@author: Antonio
"""
TedadE = 0 #Tetal de edad de equipos sanos
TEsanos = 0 #Total equipos sanos
Emenor = 100 #edad menor
Tjugadores = 0 #Total de jugadores
Jsanos = 0 #jugadores sanos
Tse = 0 #total de sospechosos o enfermos
Nmenor = " "
t = int(input("porfavor ingrese el total de equipos "));
for s in range(t):
    Tedad = 0
    totalS = 0
    Equipo = input("ingrese el nombre del equipo ");
    i = int(input("ingrese el total de jugadores "));
    for x in range(i):
        nombre = input("porfavor ingrese el nombre del jugador ");
        edad = int(input("porfavor ingrese la edad del jugador "));
        estado = int(input("digite el estado de jugador "));
        if estado == 1:
            totalS += 1
            Tedad += edad
        if edad < Emenor and estado == 2 or estado == 3:
            Nmenor = nombre;
            Emenor = edad;
            EEM = Equipo;
        if estado == 2 or estado == 3:
            Tse += 1
        Tjugadores += i
    if totalS == i:
        Jsanos += totalS
        Pedad = Tedad / i
        print(f"la edad promedio de los jugadores es de {Pedad} y todos los jugadores estan sanos");
        TedadE += Pedad
        TEsanos += 1;
#resumen de resultado
print(" ")
Pjsospechosos = (Tse / Tjugadores)*100;
PEsanos = TedadE / TEsanos;
if TEsanos >= 4 and TEsanos % 2 == 0:
    print("la liga puede ser reanudada en el 2020");
else:
    print("la liga no puede reanudar sus competencias");
print(f"la edad promedio de los equipos sanos es de {PEsanos}");
if Nmenor != " ":
    print(f"el porcentaje de jugadores en estado sospechoso o enfermo es de {Pjsospechosos}%");
    print(f"el jugador mas joven en estado sospechoso pertenece a {EEM}, su nombre es {Nmenor} de {Emenor} años");
else:
    print("no hubo ningun jugador en estado sospechoso o enfermo");