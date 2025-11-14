import pygame
import datos.constantes as constantes
from render.render_pantalla import pantalla_principal,pantalla_opciones
from gestion_eventos.evento import gestionar_eventos 

pygame.init ()
ejecutando = True

pantalla = pygame.display.set_mode ((constantes.ANCHO_PANTALLA,constantes.ALTO_PANTALLA))
pygame.display.set_caption (constantes.TITULO)
COLOR_FONDO= constantes.COLOR_FONDO
reloj = pygame.time.Clock()
pantalla_actual = "menu"
botones =[]

while ejecutando:
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando =False
        else:
            pantalla_actual = gestionar_eventos (evento,pantalla_actual,botones)
    
    if pantalla_actual =="menu":
        pantalla_principal (pantalla)
        
    elif pantalla_actual == "juego":
        
        
        pass
    
    
    
    elif pantalla_actual == "opciones":
        botones = pantalla_opciones(pantalla)
    elif pantalla_actual == "estadisticas":
        pass
    elif pantalla_actual == "salir":
        break
    
    reloj.tick(constantes.FPS)
    pygame.display.flip()
    

pygame.quit()