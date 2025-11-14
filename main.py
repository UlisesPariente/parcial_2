import funciones

while True:
    print  (f"═════════════════════════\n\tMINI GENERALA\n═════════════════════════\n[1] Jugar\n[2] Estadisticas\n[3] Creditos\n[4] Salir\n× Seleccione una opcion:\n ")
    opcion = int(input(""))
    
    match opcion:
        case 1:
            for i in range (len(funciones.Puntos_GENERALA)):
                funciones.Puntos_GENERALA[i]["valor"]=0
                funciones.Puntos_GENERALA[i]["bandera_uso"]=True
                
        
            for i in range(10):
                dados = [[0,False],[0,False],[0,False],[0,False],[0,False]]
            
                funciones.mostrar_puntuaciones()
                dados = funciones.tirada_de_dados(dados)
                dados_mantener = funciones.dados_manetener(dados)
                dados_elegidos = funciones.lista_de_dados_elegidos(dados_mantener)
                
                (puntaje,opcion) = funciones.seleccion_puntaje(dados_elegidos)
                funciones.modificacion_generala(puntaje, opcion)

            puntuacion = funciones.suma_puntos()
            nombre = input("ingrese su nombre: ")
            funciones.guardar_puntuacion(nombre, puntuacion)
            
                
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


        