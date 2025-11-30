import pygame
from render.render_elementos import crear_boton_rect,leer_TOP10_linea_por_linea,PANTALLA_FONDO_ESTADISTICAS
from datos.constantes import ANCHO_PANTALLA,ALTO_PANTALLA,COLOR_TEXTO_CLARO,COLOR_SECUNDARIO
from audio.gestor_audio import reproducir_efecto,EFECTO_CLICK,cargar_efecto





def pantalla_estadisticas(pantalla,font):
    
    while True:
        mx,my = pygame.mouse.get_pos()
        pantalla.blit(PANTALLA_FONDO_ESTADISTICAS,(0,0))    
        
        titulo = font.render("TOP PUNTUACIONES",True,(255,255,255))
        pantalla.blit (titulo,(ANCHO_PANTALLA//2-titulo.get_width()//2,20))
        
        btn_creditos = crear_boton_rect(pantalla,(ANCHO_PANTALLA-150),(ALTO_PANTALLA-100),100,50,"CREDITOS",27,COLOR_TEXTO_CLARO,COLOR_SECUNDARIO)
        btn_menu = crear_boton_rect (pantalla,50,(ALTO_PANTALLA-100),100,50,"MENU",30,COLOR_TEXTO_CLARO,COLOR_SECUNDARIO)
        
        leer_TOP10_linea_por_linea("puntuaciones.csv",font,pantalla)
                
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                return "salir"

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print (pos)
                
                if btn_creditos.collidepoint(mx,my):
                    reproducir_efecto(cargar_efecto(EFECTO_CLICK))
                    return "creditos"
                if btn_menu.collidepoint(mx,my):
                    reproducir_efecto(cargar_efecto(EFECTO_CLICK))
                    return "menu"
        
        pygame.display.flip()