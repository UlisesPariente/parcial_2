import pygame
from datos.datos import DATOS
from render.render_elementos import crear_boton_rect,imagen_de_dados,PANTALLA_FONDO_JUGAR
from jugar.juego import suma_puntos,tirada_de_dados,seleccion_puntaje,modificacion_generala,guardar_puntuacion
from datos.constantes import ALTO_PANTALLA,ANCHO_PANTALLA,COLOR_TEXTO_CLARO,COLOR_SECUNDARIO
from audio.gestor_audio import reproducir_efecto,cargar_efecto,EFECTO_CLICK

def solicitar_nombre(pantalla, font):
    nombre = ""
    activa = True
    while activa:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "jugador"
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and len(nombre)>0:
                    activa = False

                elif event.key == pygame.K_BACKSPACE:
                    nombre = nombre [:-1]
                
                else:
                    nombre += event.unicode
            pantalla.blit(PANTALLA_FONDO_JUGAR,(0,0))
            txt=font.render("Nombre a su Universo: ", True, (87, 81, 81), (191, 191, 191))
            pantalla.blit(txt,(50,50))
            
            entrada = font.render (nombre,True,(87, 81, 81), (191, 191, 191))
            
            pantalla.blit(entrada, (50,100))
            
            pygame.display.flip()
    return nombre  

def pantalla_jugar(pantalla,font):

    jugador  = ["",0]
    font_categorias = pygame.font.SysFont("Comic Sans MS", 50)  
    jugador [0] = solicitar_nombre (pantalla,font)
         
    categoria_activa = None
    categorias_seleccionadas = [True]*10
    
    for i in range (len (DATOS["puntos"])):
        DATOS["puntos"][i]["valor"] = 0
        DATOS["puntos"][i]["bandera_uso"] = True
    
    

   
    for ronda in range(1, 11): 
        
        dados = [[0,False],[0,False],[0,False],[0,False],[0,False]]
        opciones_de_seleccion = None

        
        dados_elegidos = []
        
        bandera_fin_subrondas = True
        bandera_tirar = True
        
        
        for subronda in range(1, 5):
            
            if bandera_fin_subrondas==False:   
                break
            else :
                subronda_activa = True
            
               
            while subronda_activa:
                
                pantalla.blit (PANTALLA_FONDO_JUGAR,(0,0))            
                titulo = font.render(f"{jugador[0]} - ronda {ronda}/10", True, (87, 81, 81), (191, 191, 191))
                pantalla.blit(titulo, (20, 20))
                subtitulo = font.render(f"Elija dados a jugar - tirada {subronda-1}/3", True, (87, 81, 81), (191, 191, 191))
                pantalla.blit(subtitulo, (250, 70))      
                                                                      
                for i in range(len(DATOS["puntos"])):
                    texto = DATOS["puntos"][i]["jugada"]
                    categorias = font_categorias.render(texto,True,(255,255,255))
                    pantalla.blit(categorias,(300,100+i*65))
                                            
                    Puntuaciones_txt = str(DATOS["puntos"][i]["valor"])
                    Puntuaciones = font_categorias.render(Puntuaciones_txt,True,(255,255,255))
                    pantalla.blit (Puntuaciones,(850,100+i*65))
                    
                    puntuacion_total_txt = str(suma_puntos())
                    Puntaje_total = font_categorias.render(puntuacion_total_txt,True,(87, 81, 81), (191, 191, 191))    
                    pantalla.blit(Puntaje_total,(100,355))
                    
                    titulo_total = "TOTAL"
                    total = font_categorias.render(titulo_total,True,(87, 81, 81), (191, 191, 191))
                    pantalla.blit(total,(40,300))
                                                        
                btn_jugar= crear_boton_rect(pantalla,50,(ALTO_PANTALLA-140),150,50,"JUGAR",25,COLOR_TEXTO_CLARO, COLOR_SECUNDARIO)                    
                btn_tirar = crear_boton_rect(pantalla,50,(ALTO_PANTALLA-70),150,50,"TIRAR",25,COLOR_TEXTO_CLARO,COLOR_SECUNDARIO)
                                 
                btn_dado_1 = pygame.Rect((ANCHO_PANTALLA-200),50,120,120) 
                btn_dado_2 = pygame.Rect((ANCHO_PANTALLA-200),200,120,120)
                btn_dado_3 = pygame.Rect((ANCHO_PANTALLA-200),350,120,120)
                btn_dado_4 = pygame.Rect((ANCHO_PANTALLA-200),500,120,120)
                btn_dado_5 = pygame.Rect((ANCHO_PANTALLA-200),650,120,120)                    
                mx , my = pygame.mouse.get_pos()
                
                botones_categorias = [pygame.Rect(240, 120 + i*65,40, 40)for i in range(10)]
                for i, rect in enumerate(botones_categorias):
                    pygame.draw.rect(pantalla, (208,208,208), rect, 3) 
                                                                           
                for i in range (len(dados)):
                    valor_dados  = dados [i][0]
                    if valor_dados > 0:
                        img = imagen_de_dados[valor_dados-1]
                        pantalla.blit(img,(ANCHO_PANTALLA-200,50 + (i * 150)))    
                                        
                    if dados[i][1] == True:
                        if i == 0:
                            pygame.draw.rect(pantalla,(255,255,255),btn_dado_1,3)
                        if i == 1:
                            pygame.draw.rect(pantalla,(255,255,255),btn_dado_2,3)
                        if i == 2:
                            pygame.draw.rect(pantalla,(255,255,255),btn_dado_3,3)
                        if i == 3:
                            pygame.draw.rect(pantalla,(255,255,255),btn_dado_4,3)                                
                        if i == 4:
                            pygame.draw.rect(pantalla,(255,255,255),btn_dado_5,3)                  
                                                           
                for event in pygame.event.get():
                    if event.type ==  pygame.QUIT:
                        return "salir"                        
                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        print (mx,my)                          

                        if btn_tirar.collidepoint(mx, my):
                            reproducir_efecto(cargar_efecto(EFECTO_CLICK))                                                        
                        
                            if subronda != 4:
                                subronda_activa = False
                                dados = tirada_de_dados(dados)  
                                
                            bandera_tirar = False
                                
                        if subronda >1:                                                 
                            if btn_dado_1.collidepoint(mx,my):
                                dados[0][1] = not dados[0][1]                            
                            if btn_dado_2.collidepoint(mx,my):
                                dados[1][1] = not dados[1][1]
                            if btn_dado_3.collidepoint(mx,my):
                                dados[2][1] = not dados[2][1]                            
                            if btn_dado_4.collidepoint(mx,my):
                                dados[3][1] = not dados[3][1]                            
                            if btn_dado_5.collidepoint(mx,my):
                                dados[4][1] = not dados[4][1]
                        
                        if subronda>1:    
                            for i, rect in enumerate(botones_categorias):
                                if rect.collidepoint(mx,my):
                                    opciones_de_seleccion = i
                                    
                                    if categoria_activa == i:
                                        categoria_activa = None
                                    else:
                                        categoria_activa = i 
                                                                                                                                   
                        if btn_jugar.collidepoint(mx,my):
                            reproducir_efecto(cargar_efecto(EFECTO_CLICK))
                            
                            if bandera_tirar == False and subronda>1:
                                
                                for i in range (len(categorias_seleccionadas)):
                                    if opciones_de_seleccion == i:
                                        categorias_seleccionadas[i] = False    
                                                                                                           
                                if opciones_de_seleccion != None:
                                    for i in range (5):
                                        dados_elegidos.append(dados[i][0])
                                        
                                    if DATOS["puntos"][opciones_de_seleccion]["bandera_uso"] == True:
                                                                         
                                        bandera_fin_subrondas = False
                                        subronda_activa = False
                                                                                                                                                                                                            
                                        puntaje, opciones_de_seleccion = seleccion_puntaje (opciones_de_seleccion,dados_elegidos,font_categorias,pantalla)
                                        modificacion_generala(puntaje,opciones_de_seleccion)                                        
                                        
                
                                                                                                                                                                                                                     
                for i, rect in enumerate (botones_categorias):
                    pygame.draw.rect(pantalla,(208,208,208),rect,3)
                    
                    if categorias_seleccionadas [i] == False:
                        pygame.draw.rect(pantalla,(20,188,20), rect, 20)
                        pygame.draw.rect(pantalla, (208, 208, 208), rect, 10)
                        
                                            
                for i, rect in enumerate(botones_categorias):
                    if categoria_activa == i:
                        pygame.draw.rect(pantalla, (208, 208, 208), rect, 10)
                        
                    
                        
                pygame.display.flip()
                
            if bandera_fin_subrondas == False:
                break   
                     
    jugador [1] = int(puntuacion_total_txt)
    guardar_puntuacion(jugador[0],jugador[1])          
    return "estadisticas"  
            
