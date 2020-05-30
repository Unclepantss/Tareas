# -*- coding: utf-8 -*-
"""
Created on Sat May 30 10:00:08 2020

@author: Antonio
"""
#datos / contadores
TT = 0 # total turistas
Tbrazil = 0 #total de turistas brazileños
TBT = 0 #total brazileños con tiempo
BrD = 0 #brazileños con dinero
TedadB = 0 #promedio edad brazil
menor = 100000 #menor dinero
Dedad_1 = 0 #Dinero de edades menores a 30
Dedad_2 = 0 #Dinero de edades menores a 50 y mayores a 30
Dedad_3 = 0 #Dinero de personas mayores a 50
conversor = 809.6;
Tmayor = ""
Tmayor_2 = ""
mayor = 0
Dinero = 0
#datos de entrega
Nacionalidad = input("digite la nacionalidad ");
while Nacionalidad != "atlantida":
    edad = int(input("digite edad "));
    tiempo = int(input("digite los dias de estadia "));
    dolar = int(input("digite el gasto "));
    clp = dolar * conversor;
    #sorteo de datos
    TT += 1
    if Nacionalidad == "brazil" and clp > 100.000:
        BrD += 1;
        TedadB += edad;
        Tbrazil += 1    
    elif Nacionalidad == "brazil":
        Tbrazil += 1    
    elif Nacionalidad == "brazil" and tiempo >= 3 or tiempo <= 5:
        Tbrazil += 1
        TBT += 1
    if edad < 30:
        Dedad_1 += dolar;
    elif edad > 30 and edad < 50:
        Dedad_2 += dolar;
    else:
        Dedad_3 += dolar;
    if clp > mayor:
        Tmayor_2 = Nacionalidad
        Tmayor = Nacionalidad
        mayor_2 = mayor
        mayor = clp
    if clp > mayor_2:
        Tmayor_2 = Nacionalidad
        Dinero_2 = clp
        
    while Nacionalidad != "chile":    
        if dolar < menor:
            Tmenor = Nacionalidad
        break;
    Nacionalidad = input("digite la nacionalidad ");
#resumen de datos
Pedad = TedadB / BrD;
PTB = TBT / Tbrazil;
TdineroM = Dinero + Dinero_2;
if TT > 0:
    if Tbrazil > 0:
        if BrD > 0:
            print("la edad promedio de turistas brazileños que gastaron mas de 100.000 clp fue de:", Pedad);
        else:
            print("los turistas adinerados de brazil no visitaron estas tierras");
        print("el promedio de turistas que visitaron chile durante 3 a 5 dias fue de", PTB);
    else:
        print("los turistas brazileños no visitaron chile");
        
    if Dedad_1 > Dedad_2 > Dedad_3 or Dedad_1 > Dedad_3 > Dedad_2 or Dedad_1 > Dedad_2 == Dedad_3:
        print("los turistas mas gastadores son los menores de 30 años");
    elif Dedad_2 > Dedad_1 > Dedad_3 or Dedad_2 > Dedad_3 > Dedad_2 or Dedad_2 > Dedad_1 == Dedad_3:
        print("los turistas mas gastadores son los entre 30 y 50 años");
    else:
        print("los turistas mas gastadores son los mayores de 50");
    if Tmayor == Tmayor_2:
        print(f"los turistas que gastaron mas dinero fueron {Tmayor} y gastaron {TdineroM}pesos entre los dos")
else:
    print("los turistas no visitaron chile no hay razon para operar");
    
    
