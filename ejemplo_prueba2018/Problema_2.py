# -*- coding: utf-8 -*-
"""
Created on Thu May 21 23:07:37 2020

@author: Antonio
"""
#recursos / contadores:

import math;
Tbajos = 0
Tintermedios = 0
Taltos = 0
mayor = 0
#determinador de ciclos:

Ns = int(input("porfavor ingrese la cantidad de sismos ocurridos en un dia: ")); #numero de sismos
while Ns <= 0 :
    Ns = int(input("valor no valido intente nuevamente. \n"));
for i in range(Ns):
#petición de datos:
    
    P = float(input("porfavir ingrese la profundidad del sismo (en kilometros): "));
    T = float(input("porfavor ingrese el tiempo transcurrido durante el sismo: "));
    A = float(input("porfavor ingrese la amplitud del sismo: "));
    zona = input("ingrese la ubicacion del sismo: ");
    lugar = input("porfavor ingrese el lugar del sismo: ");
#contadores:
    
    M = math.log10(A) + (3 * math.log10(8 * T)) - 2.92;
    
    if M >= 1 and M <= 3:
        print(f"el sismo es de nivel bajo con una magnitud de: {M}");
        Tbajos += 1;
    elif M > 3 and M < 7:
        print(f"el sismo es de nivel intermedio con una magnitud de: {M}");
        Tintermedios += 1;
    else:
        print(f"el sismo es de nivel alto con una magnitud de: {M}");
        Taltos += 1;   
#resultado mas alto:
        
    if M > mayor:
        mayor = M
        Mnom = lugar
        Mprof = P
#resumen total del programa:
        
Psisb = (Tbajos / Ns) * 100;
Psism = (Tintermedios / Ns) * 100;
Psisa = 100 - (Psism + Psisb);
    #totales de sismos
print (f"la cantidad de sismos bajos fueron de: {Tbajos}.");
print (f"representando un {Psisb}% de los sismos ocurrdos. \n");

print (f"la cantidad de sismos de nivel intermedio fueron de: {Tintermedios}.");
print (f"representando un {Psism}% de los sismos ocurrdos. \n");

print (f"la cantidad de sismos altos fueron de: {Taltos}.");
print (f"representando un {Psisa}% de los sismos ocurrdos. \n");
    #sismo mayor
print(f"el sismo con mayor magnitud fue de {mayor} en {Mnom} con una profundidad de {Mprof}");
    

