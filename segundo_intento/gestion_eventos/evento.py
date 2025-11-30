import pygame
from audio.gestor_audio import cargar_efecto,EFECTO_CLICK,reproducir_efecto


def gestionar_eventos (evento,pantalla_actual,botones):
    if botones is None:
        return pantalla_actual
    if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
        pos  = pygame.mouse.get_pos ()
        for boton in botones:
            if boton["rect"].collidepoint(pos):
                reproducir_efecto(cargar_efecto(EFECTO_CLICK))
                
                accion =boton["accion"]
                
                if pantalla_actual == "menu":
                    
                    match accion:
                        case "jugar":
                            return "jugar"
                        case "estadisticas":
                            return "estadisticas"
                        case "creditos":
                            return "creditos"
                        case "salir":
                            return "salir"
    return pantalla_actual
                    
                    
                    
                    