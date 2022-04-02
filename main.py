import matplotlib.pyplot as plt

arr = [[6,8], [-12,68], [0,1], [32,-5]]

def maximo_abs(lista):
    max_coord =abs(max(max(lista)))
    min_coord =abs(min(min(lista)))

    return max(max_coord, min_coord)


def coordenadas(lista):
    max_coord = maximo_abs(arr)+1
    cont = 0
    plt.plot(0,0,'k+')
    
    while(cont < len(lista)-1):

        plt.xlim(-1*max_coord, max_coord)
        plt.ylim(-1* max_coord, max_coord)

        for coord in lista:
            x = lista[cont][0]
            y = lista[cont][1]
            cont += 1


            plt.scatter(x, y)
            plt.pause(0.50)
    
    
    plt.legend(['punto de mira'] + lista)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()






if __name__ == "__main__":
    coordenadas(arr)
    


     