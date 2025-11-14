import funciones

while True:
    print  (f"═════════════════════════\n\tMINI GENERALA\n═════════════════════════\n[1] Jugar\n[2] Estadisticas\n[3] Creditos\n[4] Salir\n× Seleccione una opcion:\n ")
    opcion = int(input(""))
    
    match opcion:
        case 1:
           Puntos_GENERALA = [
                    {"valor": 0,"bandera_uso": True},
                   {"jugada":"[DOS]","valor":0,"bandera_uso":True},
                   {"jugada":"[tRES]","valor":0,"bandera_uso":True},
                   {"jugada":"[CUATRO]","valor":0,"bandera_uso":True},
                   {"jugada":"[CINCO]","valor":0,"bandera_uso":True},
                   {"jugada":"[SEIS]","valor":0,"bandera_uso":True},
                   {"jugada":"[ESCALERA (20)]","valor":0,"bandera_uso":True},
                   {"jugada":"[FULL (30)]","valor":0,"bandera_uso":True},
                   {"jugada":"[POKER (40)]","valor":0,"bandera_uso":True},
                   {"jugada":"[GENERALA (50)]","valor":0,"bandera_uso":True}
                   ]

           for i in range(9):
               funciones.mostrar_puntuaciones
               dados = funciones.tirada_de_dados
               dados_elegidos = funciones.lista_de_dados_elegidos(dados)
              # puntaje, opcion = funciones.seleccion_puntaje(dados_elegidos)
               #funciones.modificacion_generala(puntaje, opcion)

           #puntuacion = funciones.suma_puntos()
           #nombre = input("ingrese su nombre: ")
           #funciones.guardar_puntuacion(nombre, puntuacion)
            
                
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


        