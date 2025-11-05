import random
Puntos_GENERALA = [["[UNO]",0],
                   ["[DOS]",0],
                   ["[TRES]",0],
                   ["[CUATRO]",0],
                   ["[CINCO]",0],
                   ["[SEIS]",0],
                   ["[ESCALERA (20)]",0],
                   ["[FULL (30)]",0],
                   ["[POKER (40)]",0],
                   ["[GENERALA (50)]",0]]
def puntuaciones ():
    print("═════════════════════════\n\tPLANTILLA DE PUNTAJES\n═════════════════════════\n")
    Puntos_totales = 0
    for i in range (len(Puntos_GENERALA)):
        print (f" {Puntos_GENERALA[i][0]}\t:{Puntos_GENERALA[i][1]}")
        Puntos_totales += Puntos_GENERALA[i][1]
    print(f"═════════════════════════\nPUNTAJE TOTAL: {Puntos_totales}\n═════════════════════════\n")
    return Puntos_GENERALA, Puntos_totales
puntuaciones()

Nombre_de_dados = ["A","B","C","D","E"]

def tirada_de_dados ():
    dados = []
    
   
    for g in range (3): 
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


        if g < 2 :   
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
       
       
                    
                    
print (tirada_de_dados()) 