import random
from datos.datos import DATOS

def nombre_dados (datos, dados):
    for i in range(6):
        if datos["nombres"][i][1] == dados:
            return datos["nombres"][i][0]

def tirada_de_dados (dados):
        for j in range (5):
            if dados[j][1] == False:
                numero_del_dado = random.randint (1,6)
                dados[j][0] = numero_del_dado
                
            print (f"[{[j + 1]}.{dados[j][0]} -> {nombre_dados(DATOS,numero_del_dado)}]")

        return (dados)