import os
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
    print("┌──────┬──────────────┬───────────┐")
    print("│ Rank │ Nombre       │ Puntaje   │")
    print("├──────┼──────────────┼───────────┤")
    with open(ruta, "r", encoding="utf-8") as archivo:
        contador=1
        for linea in archivo:
            nombre, puntaje = linea.strip().split(",")
            print (f"│{contador:<6}│{nombre:<13} │ {puntaje:<9} │")
            contador+=1
        print("└──────┴──────────────┴───────────┘")
                    
                    
                               
           
            

def verificar_archivo_existentes(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        return False

