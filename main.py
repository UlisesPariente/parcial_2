from dados import * 
from puntaje import *
from datos.datos import DATOS

while True:
    print  (f"═════════════════════════\n\tMINI GENERALA\n═════════════════════════\n[1] Jugar\n[2] Estadisticas\n[3] Creditos\n[4] Salir\n× Seleccione una opcion:\n ")
    opcion = int(input(""))
    
    match opcion:
        case 1:
            for i in range (len(DATOS ["puntos"])):
                DATOS ["puntos"][i]["valor"]=0
                DATOS ["puntos"][i]["bandera_uso"]=True
                
        
            for i in range(10):
                dados = [[0,False],[0,False],[0,False],[0,False],[0,False]]
            
                puntaje.mostrar_puntuaciones()
                dados = dados.tirada_de_dados(dados)
                dados_mantener = dados.dados_manetener(dados)
                dados_elegidos = dados.lista_de_dados_elegidos(dados_mantener)
                
                (puntaje,opcion) = puntaje.seleccion_puntaje(dados_elegidos)
                puntaje.modificacion_generala(puntaje, opcion)

            puntuacion = puntaje.suma_puntos()
            nombre = input("ingrese su nombre: ")
            puntaje.guardar_puntuacion(nombre, puntuacion)
            
                
        case 2:
            pass
        
        case 3:
            pass
            # creditos 
            # "2/11/2025  ->  -/-/-"
            
        case 4:
            break
        
        case _:
            print (f"Opcion Invalida....")


        