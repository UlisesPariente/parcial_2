import random
Puntos_GENERALA = [["[UNO]",0],["[DOS]",0],["[TRES]",0],["[CUATRO]",0],["[CINCO]",0],["[SEIS]",0],["[ESCALERA (20)]",0],["[FULL (30)]",0],["[POKER (40)]",0],["[GENERALA (50)]",0]]
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
    dado_permanentes =[0]*5
        
    for i in range (3): #turnos de tirada
        flag_fin =True
        for i in range (5): #tira dados
            numero_del_dado = random.randint (1,6)
            dados.append (numero_del_dado) 
            print (f"[{dados[i]} -> {Nombre_de_dados[i]}]")
            
        for i in range(5): #dados a mantener
            
            dado_que_desea_mantener = str(input("Indique por el nombre cual dado desea mantener(de querer salir utilizar '*'): "))
            
            if dado_que_desea_mantener == "*":
                flag_fin = False    
                break
            
            for i in range (len(Nombre_de_dados)):
                if dado_que_desea_mantener.lower() == Nombre_de_dados[i].lower():
                    dado_permanentes [i] = dados[i]
                    
        if flag_fin == False:
            break
        
    print(dado_permanentes)
print (tirada_de_dados())