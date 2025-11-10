import random
Puntos_GENERALA = [["[1] ","[UNO]",0,True],
                   ["[2] ","[DOS]",0,True],
                   ["[3] ","[TRES]",0,True],
                   ["[4] ","[CUATRO]",0,True],
                   ["[5] ","[CINCO]",0,True],
                   ["[6] ","[SEIS]",0,True],
                   ["[7] ","[ESCALERA (20)]",0,True],
                   ["[8] ","[FULL (30)]",0,True],
                   ["[9] ","[POKER (40)]",0,True],
                   ["[10] ","[GENERALA (50)]",0,True]]

def modificacion_generala (puntaje:int, opcion):
    numero_opcion = int (opcion)
    Puntos_GENERALA [numero_opcion-1][2] = puntaje

def seleccion_puntaje (dados):

    while True:
        opciones_de_seleccion = input(f"Asigne el puntaje: ")
        Puntaje = 0
            
        match opciones_de_seleccion:
            case "1":
                if Puntos_GENERALA[0][3] == True:
                    Puntos_GENERALA [0][3] = False 
                    for i in range (5):
                        if 1 in dados[i]:
                            Puntaje += dados[i]
                    break
                else:
                    print ("opcion invalida")
                    
                # 2,5,4,4,4
                
            case "2":
                if Puntos_GENERALA[1][3] == True:
                    Puntos_GENERALA [1][3] = False 
                    for i in range (5):
                        if 2 in dados[i]:
                            Puntaje += dados[i]
                    break
                else:
                    print ("opcion invalida")
                    
            case "3":
                if Puntos_GENERALA[2][3] == True:
                    Puntos_GENERALA [2][3] = False 
                    for i in range (5):
                        if 3 in dados[i]:
                            Puntaje += dados[i]
                    break
                else:
                    print ("opcion invalida")
                    
            case "4":
                if Puntos_GENERALA[3][3] == True:
                    Puntos_GENERALA [3][3] = False 
                    for i in range (5):
                        if 4 in dados[i]:
                            Puntaje += dados[i]
                    break
                else:
                    print ("opcion invalida")
                    
            case "5":
                if Puntos_GENERALA[4][3] == True:
                    Puntos_GENERALA [4][3] = False 
                    for i in range (5):
                        if 5 in dados[i]:
                            Puntaje += dados[i]
                    break
                else:
                    print ("opcion invalida")
                   
            case "6":
                if Puntos_GENERALA[5][3] == True:
                    Puntos_GENERALA [5][3] = False 
                    for i in range (5):
                        if 6 in dados[i]:
                            Puntaje += dados[i]
                    break
                else:
                    print ("opcion invalida")
                    
            case "7":
                if Puntos_GENERALA[6][3] == True:
                    Puntos_GENERALA[6][3] = False
                    Lista_Escalera_correcta_1 =[1,2,3,4,5]
                    Lista_Escalera_correcta_2 = [2,3,4,5,6]
                
                    Dados_auxiliar = dados
                    Dados_auxiliar.sort()
                    if Dados_auxiliar == Lista_Escalera_correcta_1 or Dados_auxiliar == Lista_Escalera_correcta_2:
                        Puntaje = 20
                        break
                else:
                    print("Opcion invalida")
            case "8":
                if Puntos_GENERALA[7][3] == True:
                    Puntos_GENERALA[7][3] = False
                    contador_full = [0,0,0,0,0,0]
                    for i in range (5):
                        match dados[i]:
                            case 1:
                                contador_full [0] += 1
                            case 2:
                                contador_full[1] += 1
                            case 3:
                                contador_full[2] += 1
                            case 4:
                                contador_full[3] += 1  
                            case 5:
                                contador_full[4] += 1
                            case 6:
                                contador_full[5] += 1
                                        
                    if 3 in contador_full and 2 in contador_full:
                        Puntaje = 30
                        break
                else:
                    print ("Opcion invalida")
            case "9":
                if Puntos_GENERALA[8][3] == True:
                    Puntos_GENERALA[8][3] = False
                    lista_contador =[0,0,0,0,0,0]
                    
                    for i in range (5):
                        match dados[i]:
                            case 1:
                                lista_contador[0] += 1
                            case 2:
                                lista_contador[1] += 1
                                
                            case 3:
                                lista_contador[2] += 1
                                
                            case 4:
                                lista_contador[3] += 1
                                
                            case 5:
                                lista_contador[4] += 1
                                
                            case 6:
                                lista_contador[5] += 1
                                
                    if 4 in lista_contador:
                        Puntaje = 40
                        break
                else:
                    print ("Opcion invaldia")
                
            case "10":
                if Puntos_GENERALA[9][3] == True:
                    Puntos_GENERALA[9][3] = False
                    lista_contador =[0,0,0,0,0,0]
                    
                    for i in range (5):
                        match dados[i]:
                            case 1:
                                lista_contador[0] += 1
                            case 2:
                                lista_contador[1] += 1
                                
                            case 3:
                                lista_contador[2] += 1
                                
                            case 4:
                                lista_contador[3] += 1
                                
                            case 5:
                                lista_contador[4] += 1
                                
                            case 6:
                                lista_contador[5] += 1
                                
                    if 5 in lista_contador:
                        Puntaje = 50
                        break
                else:
                    print ("Opcion invalida")        
            case _:
                print(f"Opcion invalida...")

        return Puntaje, opciones_de_seleccion
        
def puntuaciones ():
    print("═════════════════════════\n\tPLANTILLA DE PUNTAJES\n═════════════════════════\n")
    Puntos_totales = 0
    for i in range (len(Puntos_GENERALA)):
        print (f" {Puntos_GENERALA[i][0]}\t:{Puntos_GENERALA[i][1]}")
        Puntos_totales += Puntos_GENERALA[i][1]
    print(f"═════════════════════════\nPUNTAJE TOTAL: {Puntos_totales}\n═════════════════════════\n")
    return Puntos_totales

Nombre_de_dados = ["A","B","C","D","E"]

def tirada_de_dados ():
    dados = []
    
    for g in range (4): 
        print(f"------ tirada numero {g + 1} ------")
        if g == 0:
            for l in range (5): 
                numero_del_dado = random.randint (1,6)
                dados.append ([numero_del_dado,False]) 
                print (f"[{[l + 1]}.{dados[l][0]} -> {Nombre_de_dados[l]}]")
        else:
            for j in range (5):
                if dados[j][1] == False:
                    numero_del_dado = random.randint (1,6)
                    dados[j][0] = numero_del_dado
                print (f"[{[j + 1]}.{dados[j][0]} -> {Nombre_de_dados[j]}]")


        if g < 3 :   
            while True:
                opcion = str(input("Desea hacer otra tirada? s/n\n")).lower()
                if opcion == "s":
            
                    for k in range(5): 
                        while True:
                            dado_que_desea_mantener = (input("Indique la posicion del dado desea mantener(de querer salir utilizar '10'): "))

                            if not dado_que_desea_mantener.isdigit():
                                print("debe de poner solo numeros, intente de nuevo")
                            else:
                                break
                    
                        dado_que_desea_mantener = int(dado_que_desea_mantener)

                        if dado_que_desea_mantener == 10:
                            break
                    
                        for i in range (len(dados)):
                            if dado_que_desea_mantener - 1 == i:
                                dados[i][1] = True
                elif  opcion ==  "n":
                    print (f"Fin de la tirada...")
                    return dados 
                else:
                    print(f"Opcion invalida, reintentar...")
        
        return dados
                    
print (tirada_de_dados()) 

def dados_elegidos (dados):
    dados_elegidos = []
    for i in range  (5):
        dados_elegidos[i].append(dados[i][0])
    
    return dados_elegidos

