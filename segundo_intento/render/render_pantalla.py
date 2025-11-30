import pygame
from render.render_elementos import logo_juego,fondo_menu,crear_boton_rect
from jugar.juego import tirada_de_dados,seleccion_puntaje,modificacion_generala,suma_puntos
from datos.constantes import ANCHO_PANTALLA,ALTO_PANTALLA,COLOR_SECUNDARIO,COLOR_TEXTO_OSCURO,COLOR_TEXTO_CLARO
from datos.datos import DATOS

def pantalla_principal(pantalla):
    
    logo = logo_juego()
    fondo = fondo_menu()
    

    ancho_logo = logo.get_width()
    alto_logo = logo.get_height()


    x_logo = (ANCHO_PANTALLA - ancho_logo) // 2
    y_logo = 10

    etiquetas = ["Jugar","Créditos", "Estadísticas", "Salir"]
    claves = ["jugar", "creditos", "estadisticas", "salir"]

    ANCHO_BOTON = 160
    ALTO_BOTON = 60
    ESPACIO = 100

    total_ancho_botones = (ANCHO_BOTON  * 4) + (ESPACIO * 3)
    inicio_botones_x = (ANCHO_PANTALLA - total_ancho_botones) // 2
    y_botones = ALTO_PANTALLA-100
    botones = []
    
    pantalla.blit(fondo, (0, 0))
    pantalla.blit(logo, (x_logo, y_logo))
    
    for i, texto in enumerate(etiquetas):
        x = inicio_botones_x + i * (ANCHO_BOTON + ESPACIO)
        rect = crear_boton_rect(
            pantalla,
            x, y_botones,
            ANCHO_BOTON,
            ALTO_BOTON,
            texto,
            30,
            COLOR_TEXTO_CLARO,
            COLOR_SECUNDARIO,
        )
        botones.append({"accion": claves[i], "rect": rect})
    pygame.display.flip()

    return botones
            
PANTALLA_FONDO_JUGAR= pygame.image.load( "segundo_intento/assets/FONDO_JUGAR.png")
PANTALLA_FONDO_JUGAR = pygame.transform.scale(PANTALLA_FONDO_JUGAR,(ANCHO_PANTALLA,ALTO_PANTALLA))

def fondo_pantalla_jugar():
    return PANTALLA_FONDO_JUGAR


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


imagenes_originales = [pygame.image.load("segundo_intento/assets/dados/mercurio_1.png"), pygame.image.load("segundo_intento/assets/dados/venus_2.png"), pygame.image.load("segundo_intento/assets/dados/tierra_3.png"), pygame.image.load("segundo_intento/assets/dados/marte_4.png"), pygame.image.load("segundo_intento/assets/dados/jupiter_5.png"), pygame.image.load("segundo_intento/assets/dados/saturno_6.png")]

imagen_de_dados = [
    pygame.transform.scale(img, (120, 120)) 
    for img in imagenes_originales
]

        
def pantalla_jugar(pantalla,font):

    jugador  = ["",0]
    
    jugador [0] = solicitar_nombre (pantalla,font)
    font_categorias = pygame.font.SysFont("Comic Sans MS", 50)       
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
                            print ("asd")
                            
                            
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
                                        print (dados_elegidos)
                                        print (opciones_de_seleccion)
                
                                                                                                                                                                                                                     
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
                
    return "estadisticas", jugador        
            

def pantalla_creditos(pantalla):
   
    pantalla.blit(PANTALLA_FONDO_JUGAR, (0, 0))

    fuente_titulo = pygame.font.Font(None, 80)
    fuente_texto = pygame.font.Font(None, 45)

   
    titulo = fuente_titulo.render("Mini Generala Tematica", True, COLOR_TEXTO_CLARO)
    pantalla.blit(titulo, (ANCHO_PANTALLA//2 - titulo.get_width()//2, 30))

  
    informacion = [
        "Autores: Gonzalo Ruiz Diaz y Ulises pariente",
        "Fecha: -",
        "Materia: Programación 1",
        "Docentes: Martin Alejandro Garcia",
        "Carrera: Tecnicatura en programacion",
        "Email de contacto: ruizdiaz1020@gmail.com/ulisespariente1@gmail.com",
        "presione ESC si desea volver al menu"
    ]

    y = 150
    for linea in informacion:
        renglon = fuente_texto.render(linea, True, (255,255,255))
        pantalla.blit(renglon, (80, y))
        y += 60  

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "salir"
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return "menu"   
            

    
            pygame.display.flip()

PANTALLA_FONDO_ESTADISTICAS = pygame.image.load("segundo_intento/assets/FONDO_STATS.png")
PANTALLA_FONDO_ESTADISTICAS = pygame.transform.scale(PANTALLA_FONDO_ESTADISTICAS,(ANCHO_PANTALLA,ALTO_PANTALLA))

def pantalla_estadisticas(pantalla,font):
    
    while True:
        pantalla.blit(PANTALLA_FONDO_JUGAR,(0,0))
        txt=font.render("", True, (87, 81, 81), (191, 191, 191))
        pantalla.blit(txt,(50,50))
    


def leer_TOP10_linea_por_linea(ruta):
    print("┌──────┬──────────────┬───────────┐")
    print("│ Rank │ Nombre       │ Puntaje   │")
    print("├──────┼──────────────┼───────────┤")
    with open(ruta, "r", encoding="utf-8") as archivo:
        contador=1
        for linea in archivo:
            nombre, puntaje = linea.strip().split(",")
            print (f"│{contador:<6}│{nombre:<13} │ {puntaje:<9} │")
            contador+=1
        print("└──────┴──────────────┴───────────┘")
                    