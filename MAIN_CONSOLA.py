from dados.gestor_dados import *
from puntaje.guardado_de_puntaje import *
from puntaje.asignacion_puntaje import *
from puntaje.impresion_de_puntaje import *
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
                print (f"════════════════ RONDA #{i+1} ═══════════════════════════")
                mostrar_puntuaciones()
                dados = tirada_de_dados(dados)
                dados_mantener = dados_manetener(dados)
                dados_elegidos = lista_de_dados_elegidos(dados_mantener)
                
                (puntaje,opcion) = seleccion_puntaje(dados_elegidos)
                modificacion_generala(puntaje, opcion)

            puntuacion = suma_puntos()
            nombre = input("ingrese su nombre: ")
            guardar_puntuacion(nombre, puntuacion)
            
                
        case 2:
            if verificar_archivo_existentes ("puntuaciones.csv")==False:
                print("Todavia no se cargo ningun puntaje....")
            else:
                
                leer_TOP10_linea_por_linea("puntuaciones.csv")
        
        case 3:
            pass
            # creditos 
            # "2/11/2025  ->  -/-/-"
            
        case 4:
            #QUIT
            break
        
        case _:
            print (f"Opcion Invalida....")


        