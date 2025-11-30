import pygame
from datos.constantes import ANCHO_PANTALLA,ALTO_PANTALLA,COLOR_SECUNDARIO,COLOR_TEXTO_CLARO
from render.render_elementos import crear_boton_rect,PANTALLA_FONDO_CREDITOS
from audio.gestor_audio import reproducir_efecto,cargar_efecto,EFECTO_CLICK


def pantalla_creditos(pantalla):
   
    pantalla.blit(PANTALLA_FONDO_CREDITOS, (0, 0))

    fuente_titulo = pygame.font.Font(None, 80)
    fuente_texto = pygame.font.Font(None, 45)

   
    titulo = fuente_titulo.render("GENERALA UNIVERSAL", True, COLOR_TEXTO_CLARO)
    pantalla.blit(titulo, (ANCHO_PANTALLA//2 - titulo.get_width()//2, 30))

  
    informacion = [
        "Autores: Gonzalo Ruiz Diaz y Ulises Pariente",
        "Fecha: 3/11/2025 - 30/11/2025",
        "Materia: Programación 1",
        "Docentes: Martin Alejandro Garcia",
        "Carrera: Tecnicatura en programacion",
        "Email de contacto: ruizdiaz1020@gmail.com/ulisespariente1@gmail.com",
    ]

    y = 150
    for linea in informacion:
        renglon = fuente_texto.render(linea, True, (255,255,255))
        pantalla.blit(renglon, (80, y))
        y += 60  
    btn_menu = crear_boton_rect (pantalla,50,(ALTO_PANTALLA-100),100,50,"MENU",30,COLOR_TEXTO_CLARO,COLOR_SECUNDARIO)
    
    while True:
        mx,my= pygame.mouse.get_pos()     
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                return "salir"
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_menu.collidepoint(mx,my):
                    reproducir_efecto(cargar_efecto(EFECTO_CLICK))
                    return "menu"
    
            pygame.display.flip()
