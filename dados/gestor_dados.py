from dados.lanzada_dados import tirada_de_dados

def dados_manetener (dados):
    for i in range (2):
        while True:
            opcion = str(input(f"TIRADAS DISPOBINLES {i+1} de 3\n»Desea tirar otra vez? s/n\n»")).lower()
            if opcion == "s" or opcion == "n":
                break
            else:
                print ("Opcion invalida, reintentar....")
                
        if opcion == "s":
            for k in range(5):
                 
                while True:
                    dado_que_desea_mantener = (input(f"»Indique la posicion del dado desea mantener (de querer salir presione '0'):\n "))
                    if not dado_que_desea_mantener.isdigit():
                        print("debe de poner solo numeros, intente de nuevo")
                    else:
                        break
                       
                if dado_que_desea_mantener == "0":
                    break
                
                dado_que_desea_mantener = int(dado_que_desea_mantener)
                                    
                for i in range (len(dados)):
                    if (dado_que_desea_mantener - 1) == i:
                        dados[i][1] = True
                
            tirada_de_dados(dados)
                        
        elif  opcion ==  "n":
            print (f"Fin de la tirada...")
            return dados                     
        else:
            print(f"Opcion invalida, reintentar...")

    return dados


def lista_de_dados_elegidos (lista_dados):
    dados_elegidos = []
  
    for i in range  (5):
        dados_elegidos.append(lista_dados[i][0])
    
    return dados_elegidos


