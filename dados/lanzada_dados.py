import random

def tirada_de_dados (dados):
        for j in range (5):
            if dados[j][1] == False:
                numero_del_dado = random.randint (1,6)
                dados[j][0] = numero_del_dado
                
            print (f"[{[j + 1]}.{dados[j][0]}")

        return (dados)