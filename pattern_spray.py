import random as rd
import math
import main

coord_base = [
    [0,0],
    [0.2,0.3],
    [-0.4,0.6], 
    [-0.5,1.1],
    [-0.9,2],
    [-0.2,3.3],
    [-0.7,6.8],
    [-3,7.1]
    ]

list_hip = []
list_azar_x = []
list_azar_y = []
list_incr = []

def hipopotanusa(lista):
    cont = 0

    while(cont < len(lista)-1):

        for numero in lista:
            hipot = math.sqrt((lista[cont][0]**2)+(lista[cont][1]**2))
            list_hip.append(hipot)
            cont +=1

    return list_hip


def azar(lista,hipotenusa):
    
    cont = 0 

    while(cont < len(lista)-1):
        rand_rango = rd.uniform(hipotenusa[cont]*-1, hipotenusa[cont])
        
        inc_x = lista [cont][0] + rand_rango 
        inc_y = lista [cont][1] + rand_rango 

        list_azar_x.append(inc_x)
        list_azar_y.append(inc_y)
        cont += 1
    

    return  list_azar_x,list_azar_y



hipopotanusa(coord_base)

print(azar(coord_base,list_hip))
