import random as rd
import math
import grafica_coordenadas
import json_armas


coord_base = json_armas.arma_escoger("Fusil de asalto")


lista_final =[]

def hipopotanusa(lista):
    list_hip = []

    for pareja in lista:
        hipot = math.sqrt((pareja[0]**2)+(pareja[1]**2))
        list_hip.append(hipot)
        
    return list_hip


def increment (lista,hipotenusa):
    list_incr_x = []
    list_incr_y = []
    cont = 0 

    while(cont < len(lista)):
        rand_rango = rd.uniform(hipotenusa[cont]*-1, hipotenusa[cont])
        
        inc_x = lista [cont][0] + rand_rango 
        inc_y = lista [cont][1] + rand_rango 

        list_incr_x.append(inc_x)
        list_incr_y.append(inc_y)
        cont += 1
    

    return  list_incr_x,list_incr_y


def pattern (lista_x, lista_y):

    lista_resultado =[]

    for i in range(len(lista_x)):
        lista_coord_nueva = []
        
        lista_coord_nueva.append(lista_x[i])
        lista_coord_nueva.append(lista_y[i])
        
        lista_resultado.append( lista_coord_nueva)
    
    
    return grafica_coordenadas.coordenadas(lista_resultado)
    
    
list_hipp = hipopotanusa(coord_base)
list_inc_x , list_inc_y = increment(coord_base,list_hipp)
pattern(list_inc_x , list_inc_y)