import datos.config_json as config_json

datos = config_json.cargar_datos()

ANCHO_PANTALLA = datos["config"]["ventana"]["ancho"] 
ALTO_PANTALLA = datos["config"]["ventana"]["alto"] 
COLOR_FONDO = datos["config"]["colores"]["fondo"] 
TITULO = datos["config"]["ventana"]["titulo"] 
COLOR_TEXTO_OSCURO = datos["config"]["colores"]["texto_oscuro"]
COLOR_TEXTO_CLARO = datos["config"]["colores"]["texto_claro"]
COLOR_SECUNDARIO =  datos["config"]["colores"]["primario"]
VOLUMEN = datos["config"]["audio"]["volumen"]
FPS = 60
