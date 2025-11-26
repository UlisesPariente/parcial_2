import pygame
from render.render_elementos import logo_juego,fondo_menu,crear_boton_rect

from datos.constantes import ANCHO_PANTALLA,ALTO_PANTALLA,COLOR_SECUNDARIO,COLOR_TEXTO_OSCURO,COLOR_TEXTO_CLARO


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


def solicitar_nombre (pantalla,font):
    nombre = ""
    activa = True
    while activa:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "Jugador"
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and len(nombre)>0:
                    activa = False
                    pantalla = 

                elif event.key == pygame.K_BACKSPACE:
                    nombre = nombre [:-1]
                    
                else:
                    nombre += event.unicode
            pantalla.blit(PANTALLA_FONDO_JUGAR,(0,0))
            txt=font.render("Ingresar nombre de jugador: ", True, (255,255,255))
            pantalla.blit(txt,(50,50))
            
            entrada = font.render (nombre,True,(255,255,255))
            
            pantalla.blit(entrada, (50,100))
            
            pygame.display.flip()
    return nombre




def pantalla_jugar(pantalla,font):
    jugador  = ["",0,0]
    jugador [0] = solicitar_nombre (pantalla,font)
    

        
    while True:
        pantalla.blit (PANTALLA_FONDO_JUGAR,(0,0))
        titulo = font.render(f"Jugador: {jugador[0]}", True, (0,0,0))
        pantalla.blit(titulo, (20, 20))

        subtitulo = font.render("Elija dados a jugar", True, (0,0,0))
        pantalla.blit(subtitulo, (250, 70))

        jugador [1]=0 
        
        
        for event in pygame.event.get():
            if event.type ==  pygame.QUIT:
                return "salir"

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return "menu"
            
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                M_x,M_y = event.pos
                
                
                
       