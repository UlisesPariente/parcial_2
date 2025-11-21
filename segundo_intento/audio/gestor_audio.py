import pygame
from datos.constantes import VOLUMEN

MUSICA_PRINCIPAL = "segundo_intento/audio/intro.mp3"
VOLUMEN_MUSCIA = VOLUMEN
EFECTO_CLICK = "segundo_intento/audio/efecto.mp3"

def reproducir_musica(ruta,loop=True):
    pygame.mixer.music.load(ruta)
    if loop:
        cantidad_reproduccion = -1
    else:
        cantidad_reproduccion=0
    pygame.mixer.music.play(cantidad_reproduccion)
    
def detener_musica ():
    pygame.mixer.music.stop()
    
def pausar_musica():
    pygame.mixer.music.pause()
    
def reanudadr_musica():
    pygame.mixer.music.unpause()
    
def cargar_efecto(ruta):
    efecto = pygame.mixer.Sound(ruta)
    efecto.set_volume (VOLUMEN_MUSCIA + 0.2)
    return efecto

def reproducir_efecto (efecto):
    efecto.play()
    