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


 

def pantalla_stats(pantalla):
    pantalla.fill((40, 40, 40))
    fuente = pygame.font.Font(None, 70)
    texto = fuente.render("ESTADISTICAS:", True, (COLOR_TEXTO_CLARO))
    pantalla.blit(texto, (100, 100))
    return []



PANTALLA_FONDO_JUGAR= pygame.image.load( "segundo_intento/assets/FONDO_JUGAR.png")
PANTALLA_FONDO_JUGAR = pygame.transform.scale(PANTALLA_FONDO_JUGAR,(ANCHO_PANTALLA,ALTO_PANTALLA))

def fondo_pantalla_jugar():
    return PANTALLA_FONDO_JUGAR


def pantalla_jugar(pantalla, eventos):
    
    pantalla.blit(PANTALLA_FONDO_JUGAR,(0,0))

    fuente_pantalla = pygame.font.Font(None,70)
    texto = fuente_pantalla.render("Nomber:",True,(COLOR_TEXTO_CLARO))
    pantalla.blit (texto,(10,10))
    rect = crear_boton_rect(pantalla,(ANCHO_PANTALLA-170),(ALTO_PANTALLA-70),150,50,"Siguiente",25,(COLOR_TEXTO_CLARO),(20,3,3))

    pos = pygame.mouse.get_pos()
    
    for evento in eventos():
        if rect.collidepoint(pos):
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                print ("lol")
        
    
    pygame.display.flip()