
from datos.datos import DATOS

def mostrar_puntuaciones ():
    print("════════════════════════════════════")
    print("\tPLANTILLA DE PUNTAJES")
    print("════════════════════════════════════\n")

    Puntos_totales = 0
    ancho = max(len(item['jugada']) for item in DATOS["puntos"])

    for i, item in enumerate(DATOS["puntos"], start=1):
       
        print(f"[{i:2}] {item['jugada']:<{ancho}}  :  {item['valor']:>3}")
        Puntos_totales += item["valor"]
    print("\n════════════════════════════════════")
    print(f"PUNTAJE TOTAL:\t{Puntos_totales}")
    print("════════════════════════════════════\n")


def leer_TOP10_linea_por_linea(ruta):
    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            print(linea.strip())
