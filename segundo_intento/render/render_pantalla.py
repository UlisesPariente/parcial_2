import pygame
from render.render_elementos import logo_juego,fondo_menu,crear_boton_rect
from jugar.juego import tirada_de_dados
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
            txt=font.render("Ingresar nombre de jugador: ", True, (255,255,255))
            pantalla.blit(txt,(50,50))
            
            entrada = font.render (nombre,True,(255,255,255))
            
            pantalla.blit(entrada, (50,80))
            
            pygame.display.flip()
    return nombre


imagenes_originales = [pygame.image.load("segundo_intento/assets/dados/mercurio_1.png"), pygame.image.load("segundo_intento/assets/dados/venus_2.png"), pygame.image.load("segundo_intento/assets/dados/tierra_3.png"), pygame.image.load("segundo_intento/assets/dados/marte_4.png"), pygame.image.load("segundo_intento/assets/dados/jupiter_5.png"), pygame.image.load("segundo_intento/assets/dados/saturno_6.png")]

imagen_de_dados = [
    pygame.transform.scale(img, (120, 120)) 
    for img in imagenes_originales
]

        
def pantalla_jugar(pantalla,font):
    jugador  = ["",0,0]
    jugador [0] = solicitar_nombre (pantalla,font)
    font_categorias = pygame.font.SysFont("Comic Sans MS", 50)
            
    
   
    for ronda in range(1, 11): 
        dados = [[0,False],[0,False],[0,False],[0,False],[0,False]]        
        for subronda in range(1, 5):  
            subronda_activa = True    
            while subronda_activa:
                pantalla.blit (PANTALLA_FONDO_JUGAR,(0,0))
        
                titulo = font.render(f"Jugador: {jugador[0]} - ronda {ronda}/10", True, (130, 43, 138))
                pantalla.blit(titulo, (20, 20))

                subtitulo = font.render(f"Elija dados a jugar - tirada {subronda-1}/3", True, (130, 43, 138))
                pantalla.blit(subtitulo, (250, 70))
                
                
                
                for i in range(len(DATOS["puntos"])):
                    texto = DATOS["puntos"][i]["jugada"]
                    categorias = font_categorias.render(texto,True,(255,255,255))
                    pantalla.blit(categorias,(300,100+i*65))
                
                if subronda > 1:
                    btn_jugar= crear_boton_rect(pantalla,50,(ALTO_PANTALLA-140),150,50,"JUGAR",25,COLOR_TEXTO_CLARO, COLOR_SECUNDARIO)
                
                btn_categoria_uno = pygame.Rect (304,120,153,50)
                btn_categoria_dos =pygame.Rect (300,165,150,50)
                btn_categoria_tres =pygame.Rect (300,(100+2*65),150,50)
                btn_categoria_cuatro =pygame.Rect (300,(100+3*65),150,50)
                btn_categoria_cinco =pygame.Rect (300,(100+4*65),150,50)
                btn_categoria_seis =pygame.Rect (300,(100+5*65),150,50)
                btn_categoria_escalera =pygame.Rect (300,(100+6*65),150,50)
                btn_categoria_full =pygame.Rect (300,(100+7*65),150,50)
                btn_categoria_poker =pygame.Rect (300,(100+8*65),150,50)
                btn_categoria_generala =pygame.Rect (300,(100+9*65),150,50)
                
                
                
                btn_tirar = crear_boton_rect(pantalla,50,(ALTO_PANTALLA-70),150,50,"TIRAR",25,COLOR_TEXTO_CLARO,COLOR_SECUNDARIO)
                

                btn_dado_1 = pygame.Rect((ANCHO_PANTALLA-200),50,120,120) 
                btn_dado_2 = pygame.Rect((ANCHO_PANTALLA-200),200,120,120)
                btn_dado_3 = pygame.Rect((ANCHO_PANTALLA-200),350,120,120)
                btn_dado_4 = pygame.Rect((ANCHO_PANTALLA-200),500,120,120)
                btn_dado_5 = pygame.Rect((ANCHO_PANTALLA-200),650,120,120)
                
                mx , my = pygame.mouse.get_pos()
                if btn_categoria_uno.collidepoint (mx,my):
                    pygame.draw.rect(pantalla,(208,208,208),btn_categoria_uno,3)
                
                for i in range (len(dados)):
                    valor  = dados [i][0]
                    if valor > 0:
                        img = imagen_de_dados[valor-1]
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
                            tirada_de_dados(dados)
                            dados = tirada_de_dados(dados)
                            
                            subronda_activa = False
                        
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

            
        
                pygame.display.flip()
        

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

    
    
                
                
       