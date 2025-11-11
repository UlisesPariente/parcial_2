import pygame
from datos.constantes import ANCHO_PANTALLA,ALTO_PANTALLA


FONDO = pygame.image.load ("segundo_intento/assets/FONDO.png")
FONDO = pygame.transform.scale (FONDO,(ANCHO_PANTALLA,ALTO_PANTALLA))

LOGO = pygame.image.load ("segundo_intento/assets/LOGO.png")
LOGO = pygame.transform.scale (LOGO,(500,500))

def logo_juego ():
    return LOGO

def fondo_menu():
    return FONDO

def crear_boton_rect (superficie,x,y,ancho,alto,texto,color_fondo,color_texto):
    
    fuente =pygame.font.Font(None,40)
    rectangulo = pygame.Rect (x,y,ancho,alto)
    
    pygame.draw.rect(superficie,color_fondo,rectangulo,border_radius=10)
    
    texto_imagen = fuente.render(texto,True, color_texto)
    texto_x = x + (ancho - texto_imagen.get_width()) // 2
    texto_y = y + (alto - texto_imagen.get_height()) // 2
    
    superficie.blit (texto_imagen,(texto_x,texto_y))
    
    return rectangulo

def crear_boton_imagen (superficie,x,y,ancho,alto,ruta_imagen):
    imagen = pygame.image.load (ruta_imagen)
    imagen = pygame.transform.scale (imagen,(ancho,alto))
    
    forma = imagen.get_rect(topleft = (x, y))
    superficie.blit(imagen, forma.topleft)

    return forma