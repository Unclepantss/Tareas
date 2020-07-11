# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 09:13:50 2020

@author: Antonio
"""
tp = 0
tj = 0
tv = 0
def vprimo (ver): #verficacion de numero primo
    for i in range(2, ver):

        if (ver % i) == 0:
            return False;
            break;

        else:
            return True;

def validacion (num, ver): #suma de numeros y comparacion con verificador
    total = 0
    n = [int(d) for d in str(num)]
    
    for i in range(len(n)):
        total += n[i];
    
    if total == ver:
        return True;
    
    else:
        return False;

archivo = open("Carnet.txt", "r"); #apertura de archivos
salida = open("Validos.txt", "w");

linea = archivo.readline().strip();
datos = linea.split("-");

num = int(datos[0]);    #separacion de datos
ver = int(datos[1]);
nombre = datos[2];
edad = datos[3];
tp += 1;

for linea in archivo:   #ciclo
    
    vp = vprimo(ver); #verificador primo
    ns = validacion(num, ver);  #numeros suma

    if vp and ns:
        salida.write(f"{num}-{ver} {nombre}");
        salida.write("\n");
        tv += 1; #total verificados

    if vp and ns and int(edad) < 35:
        tj += 1 #total jovenes

    datos = linea.split("-");
    num = datos[0];
    ver = int(datos[1]);
    nombre = datos[2];
    edad = datos[3];
    tp += 1;
porcentaje = (tj / tv)*100;

print(f"El porcentaje de menores recuperados es  {porcentaje}");
print(f"Total de registros procesados  {tp}");
print(f"Total de registros válidos grabados en archivo {tv}");

archivo.close();
salida.close();








