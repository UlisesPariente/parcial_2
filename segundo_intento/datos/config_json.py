import json
import os


configuracion_default = {
    "config": {
        "ventana": {"ancho": 800, "alto": 600, "titulo": "DICE NICE"},
        "audio": {"volumen": 0.7},
        "colores": {"fondo": [5, 1, 87], "primario": [113, 0, 255], "secundario": [252, 96, 248], "texto_claro": [255, 255, 255], "texto_oscuro": [0, 0, 0]}
    }
}

archi_config = "segundo_intento/datos/config.json"

def guardar_datos(datos):
    with open(archi_config, "w") as archivo:
        json.dump(datos, archivo, indent=4)

def cargar_datos():

    if not os.path.exists(archi_config) or os.path.getsize(archi_config) == 0:
        guardar_datos(configuracion_default)
        return configuracion_default
    
    with open(archi_config, "r") as archivo:
        datos = json.load(archivo)

    if "config" not in datos:
        guardar_datos(configuracion_default)
        return configuracion_default
    
    return datos
