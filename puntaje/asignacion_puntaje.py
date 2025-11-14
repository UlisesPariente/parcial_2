
from datos.datos import DATOS

def seleccion_puntaje (dados):

    while True:
        opciones_de_seleccion = input(f"Asigne categoria del puntaje: ")
        Puntaje = 0
            
        match opciones_de_seleccion:
            case "1":
                if DATOS ["puntos"][0]["bandera_uso"] == True:
                    DATOS ["puntos"] [0]["bandera_uso"] = False 
                    for i in range (5):
                        if 1 == dados[i]:
                            Puntaje += dados[i]
                    break
                else:
                    print ("opcion invalida")
                    
                
                
            case "2":
                if DATOS ["puntos"][1]["bandera_uso"] == True:
                    DATOS ["puntos"] [1]["bandera_uso"] = False 
                    for i in range (5):
                        if 2 == dados[i]:
                            Puntaje += dados[i]
                    break
                else:
                    print ("opcion invalida")
                    
            case "3":
                if DATOS ["puntos"][2]["bandera_uso"] == True:
                    DATOS ["puntos"] [2]["bandera_uso"] = False 
                    for i in range (5):
                        if 3 == dados[i]:
                            Puntaje += dados[i]
                    break
                else:
                    print ("opcion invalida")
                    
            case "4":
                if DATOS ["puntos"][3]["bandera_uso"] == True:
                    DATOS ["puntos"] [3]["bandera_uso"] = False 
                    for i in range (5):
                        if 4 == dados[i]:
                            Puntaje += dados[i]
                    break
                else:
                    print ("opcion invalida")
                    
            case "5":
                if DATOS ["puntos"][4]["bandera_uso"] == True:
                    DATOS ["puntos"] [4]["bandera_uso"] = False 
                    for i in range (5):
                        if 5 == dados[i]:
                            Puntaje += dados[i]
                    break
                else:
                    print ("opcion invalida")
                   
            case "6":
                if DATOS ["puntos"][5]["bandera_uso"] == True:
                    DATOS ["puntos"] [5]["bandera_uso"] = False 
                    for i in range (5):
                        if 6 == dados[i]:
                            Puntaje += dados[i]
                    break
                else:
                    print ("opcion invalida")
                    
            case "7":
                if DATOS ["puntos"][6]["bandera_uso"] == True:
                    DATOS ["puntos"][6]["bandera_uso"] = False
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
                if DATOS ["puntos"][7]["bandera_uso"] == True:
                    DATOS ["puntos"][7]["bandera_uso"] = False
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
                if DATOS ["puntos"][8]["bandera_uso"] == True:
                    DATOS ["puntos"][8]["bandera_uso"] = False
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
                if DATOS ["puntos"][9]["bandera_uso"] == True:
                    DATOS ["puntos"][9]["bandera_uso"] = False
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
        
    return (Puntaje, opciones_de_seleccion)
        

def modificacion_generala (puntaje:int, opcion):
    numero_opcion = int (opcion)
    DATOS ["puntos"] [numero_opcion-1]["valor"] = puntaje