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

                elif event.key == pygame.K_BACKSPACE:
                    nombre = nombre [:-1]
                
                else:
                    nombre += event.unicode
            pantalla.fill((50,120,50))
            txt=font.render("Ingresar nombre de jugador: ", True, (255,255,255))
            pantalla.blit(txt,(80,200))
            
            entrada = font.render (nombre,True,(255,255,255))
            
            pantalla.blit(entrada, (80,260))
            
            pygame.display.flip()
    return nombre
            
PANTALLA_FONDO_JUGAR= pygame.image.load( "segundo_intento/assets/FONDO_JUGAR.png")
PANTALLA_FONDO_JUGAR = pygame.transform.scale(PANTALLA_FONDO_JUGAR,(ANCHO_PANTALLA,ALTO_PANTALLA))

def fondo_pantalla_jugar():
    return PANTALLA_FONDO_JUGAR



def pantalla_jugar(pantalla):
    nombre_usuario = ""
    pantalla.blit(PANTALLA_FONDO_JUGAR,(0,0))

    fuente_pantalla = pygame.font.Font(None,70)
    fuente_input = pygame.font.Font(None,(60))
    texto = fuente_pantalla.render("Nomber:",True,(COLOR_TEXTO_CLARO))
    pantalla.blit (texto,(10,10))
    
    texto_nombre = fuente_input.render(nombre_usuario,True,(255,255,255))
    pantalla.blit(texto_nombre,(10,100))
    
    rect = crear_boton_rect(pantalla,(ANCHO_PANTALLA-170),(ALTO_PANTALLA-70),150,50,"Siguiente",25,(COLOR_TEXTO_CLARO),(20,3,3))

    pos = pygame.mouse.get_pos()
    
    for evento in pygame.event.get(()):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                if nombre_usuario.strip() != "":
                    return "estadisticas"
            
            elif evento.key == pygame.K_BACKSPACE:
                nombre_usuario = nombre_usuario[:-1]
            
            else:
                if evento.unicode.insprintable():
                    nombre_usuario += evento.unicode
                    
        if rect.collidepoint (pos):
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if nombre_usuario.strip () != "":
                    return "estadisticas"
    
    pygame.display.flip()
    
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

                elif event.key == pygame.K_BACKSPACE:
                    nombre = nombre [:-1]
                
                else:
                    nombre += event.unicode
            pantalla.fill((50,120,50))
            txt=font.render("Ingresar nombre de jugador: ", True, (255,255,255))
            pantalla.blit(txt,(80,200))
            
            entrada = pygame.font.Font(None,50).render (nombre,True,(255,255,255))
            
            pantalla.blit(entrada, (80,260))
            
            pygame.display.flip()
    return nombre