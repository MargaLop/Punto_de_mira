import random as rd
import math
import main

coord = [
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

def hipopotanusa(lista):
    cont = 0

    while(cont < len(lista)-1):

        for numero in lista:
            hipot = math.sqrt((lista[cont][0]**2)+(lista[cont][1]**2))
            list_hip.append(hipot)
            cont +=1

    return list_hip
hipopotanusa(coord)



def azar(lista):

    cont = 0
    list_azar = []
    while(cont < len(lista)-1):
        rand_rango = rd.uniform(list_hip[cont]*-1, list_hip[cont])
        list_azar.append(rand_rango)
        cont += 1
    return  list_azar

print(azar(coord))