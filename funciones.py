import random
import os
Puntos_GENERALA = [{"jugada":"[UNO]", "valor":0, "bandera_uso":True},
                   {"jugada":"[DOS]","valor":0,"bandera_uso":True},
                   {"jugada":"[tRES]","valor":0,"bandera_uso":True},
                   {"jugada":"[CUATRO]","valor":0,"bandera_uso":True},
                   {"jugada":"[CINCO]","valor":0,"bandera_uso":True},
                   {"jugada":"[SEIS]","valor":0,"bandera_uso":True},
                   {"jugada":"[ESCALERA (20)]","valor":0,"bandera_uso":True},
                   {"jugada":"[FULL (30)]","valor":0,"bandera_uso":True},
                   {"jugada":"[POKER (40)]","valor":0,"bandera_uso":True},
                   {"jugada":"[GENERALA (50)]","valor":0,"bandera_uso":True}]

def modificacion_generala (puntaje:int, opcion):
    numero_opcion = int (opcion)
    Puntos_GENERALA [numero_opcion-1]["valor"] = puntaje


def suma_puntos ():
    puntaje_total = 0
    for i in range(len(Puntos_GENERALA)):
        puntaje_total +=  Puntos_GENERALA[i]["valor"]
    return puntaje_total

def seleccion_puntaje (dados):

    while True:
        opciones_de_seleccion = input(f"Asigne categoria del puntaje: ")
        Puntaje = 0
            
        match opciones_de_seleccion:
            case "1":
                if Puntos_GENERALA[0]["bandera_uso"] == True:
                    Puntos_GENERALA [0]["bandera_uso"] = False 
                    for i in range (5):
                        if 1 == dados[i]:
                            Puntaje += dados[i]
                    break
                else:
                    print ("opcion invalida")
                    
                
                
            case "2":
                if Puntos_GENERALA[1]["bandera_uso"] == True:
                    Puntos_GENERALA [1]["bandera_uso"] = False 
                    for i in range (5):
                        if 2 == dados[i]:
                            Puntaje += dados[i]
                    break
                else:
                    print ("opcion invalida")
                    
            case "3":
                if Puntos_GENERALA[2]["bandera_uso"] == True:
                    Puntos_GENERALA [2]["bandera_uso"] = False 
                    for i in range (5):
                        if 3 == dados[i]:
                            Puntaje += dados[i]
                    break
                else:
                    print ("opcion invalida")
                    
            case "4":
                if Puntos_GENERALA[3]["bandera_uso"] == True:
                    Puntos_GENERALA [3]["bandera_uso"] = False 
                    for i in range (5):
                        if 4 == dados[i]:
                            Puntaje += dados[i]
                    break
                else:
                    print ("opcion invalida")
                    
            case "5":
                if Puntos_GENERALA[4]["bandera_uso"] == True:
                    Puntos_GENERALA [4]["bandera_uso"] = False 
                    for i in range (5):
                        if 5 == dados[i]:
                            Puntaje += dados[i]
                    break
                else:
                    print ("opcion invalida")
                   
            case "6":
                if Puntos_GENERALA[5]["bandera_uso"] == True:
                    Puntos_GENERALA [5]["bandera_uso"] = False 
                    for i in range (5):
                        if 6 == dados[i]:
                            Puntaje += dados[i]
                    break
                else:
                    print ("opcion invalida")
                    
            case "7":
                if Puntos_GENERALA[6]["bandera_uso"] == True:
                    Puntos_GENERALA[6]["bandera_uso"] = False
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
                if Puntos_GENERALA[7]["bandera_uso"] == True:
                    Puntos_GENERALA[7]["bandera_uso"] = False
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
                if Puntos_GENERALA[8]["bandera_uso"] == True:
                    Puntos_GENERALA[8]["bandera_uso"] = False
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
                if Puntos_GENERALA[9]["bandera_uso"] == True:
                    Puntos_GENERALA[9]["bandera_uso"] = False
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
        
def mostrar_puntuaciones ():
    print("═════════════════════════\n\tPLANTILLA DE PUNTAJES\n═════════════════════════\n")
    Puntos_totales = 0
    for i in range (len(Puntos_GENERALA)):
        print (f"[{i + 1}] {Puntos_GENERALA[i]["jugada"]}\t:{Puntos_GENERALA[i]["valor"]}")
        Puntos_totales += Puntos_GENERALA[i]["valor"]
    print(f"═════════════════════════\nPUNTAJE TOTAL: {Puntos_totales}\n═════════════════════════\n")


Nombre_de_dados = ["A","B","C","D","E"]

def tirada_de_dados (dados):
        for j in range (5):
            if dados[j][1] == False:
                numero_del_dado = random.randint (1,6)
                dados[j][0] = numero_del_dado
                
            print (f"[{[j + 1]}.{dados[j][0]} -> {Nombre_de_dados[j]}]")

        return (dados)
                    
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




def guardar_puntuacion(nombre, puntuacion):
    archivo = "puntuaciones.csv"
    puntuaciones = []

   
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            lineas = f.readlines()

        for linea in lineas:
            partes = linea.strip().split(",")
            if len(partes) == 2:
                n = partes[0]
                p = int(partes[1])
                puntuaciones.append((n, p))

    
    puntuaciones.append((nombre, puntuacion))

  
    n = len(puntuaciones)
    for i in range(n):
        for j in range(0, n - i - 1):
            if puntuaciones[j][1] < puntuaciones[j + 1][1]:
                puntuaciones[j] = puntuaciones[j + 1]
                puntuaciones[j + 1] = puntuaciones[j]

   
    if len(puntuaciones) > 10:
        puntuaciones = puntuaciones[:10]

   
    with open(archivo, "w", encoding="utf-8") as f:
        for n, p in puntuaciones:
            f.write(f"{n},{p}\n")

    print(f"Puntuación guardada: {nombre} - {puntuacion}")