from dados.lanzada_dados import tirada_de_dados

def dados_manetener (dados):
    
    for i in range (2):
        opcion = str(input("Desea hacer otra tirada? s/n\n")).lower()
        if opcion == "s":
            for k in range(5):
                 
                while True:
                    dado_que_desea_mantener = (input("Indique la posicion del dado desea mantener(de querer salir utilizar'10'): "))
                    if not dado_que_desea_mantener.isdigit():
                        print("debe de poner solo numeros, intente de nuevo")
                    else:
                        break    
                
                if dado_que_desea_mantener == "10":
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


def nombre_dados (datos, dados):
    for i in range(6):
        if datos["nombres"][i][1] == dados:
            return datos["nombres"][i][0]