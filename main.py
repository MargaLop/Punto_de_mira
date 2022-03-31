import matplotlib.pyplot as plt

arr = [[6,6], [-1,8], [9,1], [6,-5]]

def coordenadas(lista):

    cont = 0

    while(cont < len(lista)-1):
        for coord in lista:
            x = lista[cont][0]
            y = lista[cont][1]
            cont += 1


            plt.scatter(x, y)
    
    plt.legend(lista)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()



coordenadas(arr)




if __name__ == "__main__":
   print(f'mi nombres es >> {__name__}<<')

else:
    print (f'Importado como modulo: >>{__name__}<<')

     