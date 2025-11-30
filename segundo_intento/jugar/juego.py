import pygame
import random
from datos.datos import DATOS
import os

def lista_de_dados_elegidos (lista_dados):
    dados_elegidos = []
  
    for i in range  (5):
        dados_elegidos.append(lista_dados[i][0])
    
    return dados_elegidos

def nombre_dados (datos, dados):
    for i in range(6):
        if datos["nombres"][i][1] == dados:
            return datos["nombres"][i][0]

def tirada_de_dados (dados):
        for j in range (5):
            if dados[j][1] == False:
                numero_del_dado = random.randint (1,6)
                dados[j][0] = numero_del_dado

        return (dados)
    
    

def seleccion_puntaje (opciones_de_seleccion,dados,font,pantalla):

    while True:
        Puntaje = 0
            
        match opciones_de_seleccion:
            case 0:
                if DATOS ["puntos"][0]["bandera_uso"] == True:
                    DATOS ["puntos"] [0]["bandera_uso"] = False 
                    for i in range (5):
                        if 1 == dados[i]:
                            Puntaje += dados[i]
                
            case 1:
                if DATOS ["puntos"][1]["bandera_uso"] == True:
                    DATOS ["puntos"] [1]["bandera_uso"] = False 
                    for i in range (5):
                        if 2 == dados[i]:
                            Puntaje += dados[i]
                            
            case 2:
                if DATOS ["puntos"][2]["bandera_uso"] == True:
                    DATOS ["puntos"] [2]["bandera_uso"] = False 
                    for i in range (5):
                        if 3 == dados[i]:
                            Puntaje += dados[i]  
                    
            case 3:
                if DATOS ["puntos"][3]["bandera_uso"] == True:
                    DATOS ["puntos"] [3]["bandera_uso"] = False 
                    for i in range (5):
                        if 4 == dados[i]:
                            Puntaje += dados[i]
                      
            case 4:
                if DATOS ["puntos"][4]["bandera_uso"] == True:
                    DATOS ["puntos"] [4]["bandera_uso"] = False 
                    for i in range (5):
                        if 5 == dados[i]:
                            Puntaje += dados[i]
                   
            case 5:
                if DATOS ["puntos"][5]["bandera_uso"] == True:
                    DATOS ["puntos"] [5]["bandera_uso"] = False 
                    for i in range (5):
                        if 6 == dados[i]:
                            Puntaje += dados[i]
                 
            case 6:
                if DATOS ["puntos"][6]["bandera_uso"] == True:
                    DATOS ["puntos"][6]["bandera_uso"] = False
                    Lista_Escalera_correcta_1 =[1,2,3,4,5]
                    Lista_Escalera_correcta_2 = [2,3,4,5,6]
                
                    Dados_auxiliar = dados
                    Dados_auxiliar.sort()
                    
                    if Dados_auxiliar == Lista_Escalera_correcta_1 or Dados_auxiliar == Lista_Escalera_correcta_2:
                        Puntaje = 20
                   
            case 7:
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
                    
            case 8:
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
               
            case 9:
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
           
        return (Puntaje, opciones_de_seleccion)
            

    
        

def modificacion_generala (puntaje:int, opcion):
    DATOS ["puntos"] [opcion]["valor"] = puntaje
    
def suma_puntos ():
    puntaje_total = 0
    for i in range(len(DATOS["puntos"])):
        puntaje_total +=  DATOS ["puntos"][i]["valor"]
    return puntaje_total

def guardar_puntuacion(nombre, puntuacion):
    archivo = "puntuaciones.csv"
    puntuaciones = []
    
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            lineas = f.readlines()

        for linea in lineas:
            partes = linea.strip().split(",")
            if len(partes) == 2 and partes[1].isdigit():
                n = partes[0]
                p = int(partes[1])
                puntuaciones.append((n, p))

    
    puntuaciones.append((nombre, puntuacion))

    n = len(puntuaciones)
    for i in range(n):
        for j in range(0, n - i - 1):
            if puntuaciones[j][1] < puntuaciones[j + 1][1]:
                temp = puntuaciones[j]
                puntuaciones[j] = puntuaciones[j + 1]
                puntuaciones[j + 1] = temp

    if len(puntuaciones) > 10:
        puntuaciones = puntuaciones[:10]

    with open(archivo, "w", encoding="utf-8") as f:
        for n, p in puntuaciones:
            f.write(f"{n},{p}\n")
