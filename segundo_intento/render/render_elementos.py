import pygame
from datos.constantes import ANCHO_PANTALLA,ALTO_PANTALLA


def logo_juego ():
    return LOGO_PANTALLA_MENU

def FONDO_PANTALLA(fondo):
    return fondo

FONDO = pygame.image.load ("segundo_intento/assets/FONDO.jpg")
FONDO_PANTALLA_MENU = pygame.transform.scale (FONDO,(ANCHO_PANTALLA,ALTO_PANTALLA))

LOGO = pygame.image.load ("segundo_intento/assets/LOGO.png")
LOGO_PANTALLA_MENU = pygame.transform.scale (LOGO,(500,500))

PANTALLA_FONDO_JUGAR= pygame.image.load( "segundo_intento/assets/fondo_jugar.jpg")
PANTALLA_FONDO_JUGAR = pygame.transform.scale(PANTALLA_FONDO_JUGAR,(ANCHO_PANTALLA,ALTO_PANTALLA))
PANTALLA_FONDO_JUGAR = FONDO_PANTALLA(PANTALLA_FONDO_JUGAR)

PANTALLA_FONDO_ESTADISTICAS = pygame.image.load("segundo_intento/assets/fondo_estadisticas.jpg")
PANTALLA_FONDO_ESTADISTICAS = pygame.transform.scale(PANTALLA_FONDO_ESTADISTICAS,(ANCHO_PANTALLA,ALTO_PANTALLA))
PANTALLA_FONDO_ESTADISTICAS = FONDO_PANTALLA (PANTALLA_FONDO_ESTADISTICAS)

PANTALLA_FONDO_CREDITOS = pygame.image.load("segundo_intento/assets/creditos_imagen.jpg")
PANTALLA_FONDO_CREDITOS = pygame.transform.scale(PANTALLA_FONDO_CREDITOS,(ANCHO_PANTALLA,ALTO_PANTALLA))
PANTALLA_FONDO_CREDITOS = FONDO_PANTALLA(PANTALLA_FONDO_CREDITOS)



#DADOS
imagenes_originales = [pygame.image.load("segundo_intento/assets/dados/mercurio_1.png"), pygame.image.load("segundo_intento/assets/dados/venus_2.png"), pygame.image.load("segundo_intento/assets/dados/tierra_3.png"), pygame.image.load("segundo_intento/assets/dados/marte_4.png"), pygame.image.load("segundo_intento/assets/dados/jupiter_5.png"), pygame.image.load("segundo_intento/assets/dados/saturno_6.png")]

imagen_de_dados = [
    pygame.transform.scale(img, (120, 120)) 
    for img in imagenes_originales
]





def crear_boton_rect (superficie,x,y,ancho,alto,texto,tamaño_texto,color_fondo,color_texto):
    
    fuente =pygame.font.Font(None,tamaño_texto)
    rectangulo = pygame.Rect (x,y,ancho,alto)

    
    if rectangulo.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(superficie,(155,155,155),rectangulo,border_radius=10)
    else :
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

def leer_TOP10_linea_por_linea(ruta,font,pantalla):
    
    with open(ruta, "r", encoding="utf-8") as archivo:
        contador=1
        for linea in archivo:
            
            nombre, puntaje = linea.strip().split(",")
            txt_nombre = font.render (f"{nombre}",True,(255,255,255))
            txt_puntaje = font.render (f"{puntaje}",True,(255,255,255))
            pantalla.blit (txt_nombre,(265,95+contador*50))
            pantalla.blit (txt_puntaje,(910,95+contador*50))
            contador+=1
        