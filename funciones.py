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

def modificacion_generala (opcion_seleccionada, acumulador, puntos_generala):
    pass

def seleccion_puntaje (dados):
    opciones_de_seleccion = input(f"Asigne el puntaje: ")
    acumulador = 0
    
    while True:
            
        match opciones_de_seleccion:
            case 1:
                
                for i in range (5):
                    if 1 in dados[i]:
                        acumulador += dados[i]
                
                
                
            case 2:
                for i in range (5):
                    if 2 in dados[i]:
                        acumulador += dados[i]
                
            
            case 3:
                for i in range (5):
                    if 3 in dados[i]:
                        acumulador += dados[i]
    
            
            case 4:
                for i in range (5):
                    if 4 in dados[i]:
                        acumulador += dados[i]
                
            
            case 5:
                for i in range (5):
                    if 5 in dados[i]:
                        acumulador += dados[i]
                
            
            case 6:
                for i in range (5):
                    if 6 in dados[i]:
                        acumulador += dados[i]
                
            
            case 7:# [5,3,2,1,4]
                Lista_Escalera_correcta =[[1,False], [2,False],[3,False],[4,False],[5,False]]
                flag_escalera_incorrecta = False
                
                for i in range (5):
                    for j in range (5):
                        if Lista_Escalera_correcta [i][0] == dados[j]:
                            Lista_Escalera_correcta [i][1] = True
                            break
                        
                for i in range (5):
                    if Lista_Escalera_correcta [i][1] == False:
                        flag_escalera_incorrecta = True
                        
                if flag_escalera_incorrecta == False :
                    acumulador = 20
                    
                
            case 8:
                #opcion = [3,3,3,2,2]
                #dados = [2,3,2,3,3]
                contador_1=0
                contador_2=0
                contador_3=0
                contador_4=0
                contador_5=0
                contador_6=0
                flag_full = True
                for i in range (5):
                    match dados[i]:
                        case 1:
                            contador_1 += 1
                            pass
                        case 2:
                            contador_2 += 1
                            pass
                        case 3:
                            contador_3 += 1
                            pass
                        case 4:
                            contador_4 += 1
                            pass
                        case 5:
                            contador_5 += 1
                            pass
                        case 6:
                            contador_6 += 1
                            pass
                
                            
            case 9:
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
                            
                for i in range (5):
                    if lista_contador [i] == 4:
                        acumulador= 40
                        return acumulador                
            
            case 10:
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
                            
                for i in range (5):
                    if lista_contador [i] == 5:
                        acumulador= 50
                        return acumulador
                           
            case _:
                print(f"Opcion invalida...")

        return acumulador, opciones_de_seleccion
        
def puntuaciones ():
    print("═════════════════════════\n\tPLANTILLA DE PUNTAJES\n═════════════════════════\n")
    Puntos_totales = 0
    for i in range (len(Puntos_GENERALA)):
        print (f" {Puntos_GENERALA[i][0]}\t:{Puntos_GENERALA[i][1]}")
        Puntos_totales += Puntos_GENERALA[i][1]
    print(f"═════════════════════════\nPUNTAJE TOTAL: {Puntos_totales}\n═════════════════════════\n")
    return Puntos_totales
puntuaciones()

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

