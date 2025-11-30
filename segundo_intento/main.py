import pygame
import datos.constantes as constantes
from render.render_menu import pantalla_principal
from render.render_jugar import pantalla_jugar
from render.render_estadisticas import pantalla_estadisticas
from render.render_creditos import pantalla_creditos
from gestion_eventos.evento import gestionar_eventos 
from audio.gestor_audio import reproducir_musica,MUSICA_PRINCIPAL


pygame.init ()
pygame.mixer.init()

ejecutando = True

pantalla = pygame.display.set_mode ((constantes.ANCHO_PANTALLA,constantes.ALTO_PANTALLA))
pygame.display.set_caption (constantes.TITULO)
COLOR_FONDO= constantes.COLOR_FONDO
reloj = pygame.time.Clock()
pantalla_actual = "menu"

botones = None
musica=reproducir_musica(MUSICA_PRINCIPAL)
font = pygame.font.Font(None,50)
nombre_usuario = ""

while ejecutando:
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            ejecutando =False
        else:
            pantalla_actual = gestionar_eventos (evento,pantalla_actual,botones)
            
    if pantalla_actual =="menu":
        botones = pantalla_principal (pantalla) 
        
    elif pantalla_actual == "jugar":
       
        pantalla_actual = pantalla_jugar(pantalla,font)

    elif pantalla_actual == "estadisticas":
        
        pantalla_actual = pantalla_estadisticas(pantalla,font)
    elif pantalla_actual == "creditos":
        pantalla_actual = pantalla_creditos(pantalla)
        
    elif pantalla_actual == "salir":
        ejecutando = False

            
    reloj.tick(constantes.FPS)
    pygame.display.flip()
    

pygame.quit()