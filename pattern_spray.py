import random as rd
import math
import main 


coord_base = [
    [0, 0],
    [0.2, 0.3],
    [-0.4, 0.6], 
    [-0.5, 1.1],
    [-0.9, 2],
    [-0.2, 3.3],
    [-0.7, 6.8],
    [-3, 7.1]
    ]



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
    
    
    return main.coordenadas(lista_resultado)
    
    
list_hipp = hipopotanusa(coord_base)
list_inc_x , list_inc_y = increment(coord_base,list_hipp)
pattern(list_inc_x , list_inc_y)