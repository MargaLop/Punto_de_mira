import json

def arma_escoger (arma_nombre):
    with open('tipo_armas.txt','r') as x:
        mi_variable = x.read()

    mi_arma = json.loads(mi_variable)
    return mi_arma[arma_nombre]
