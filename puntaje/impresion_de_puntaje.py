
from datos.datos import DATOS
def mostrar_puntuaciones ():
    print("════════════════════════════════════")
    print("\tPLANTILLA DE PUNTAJES")
    print("════════════════════════════════════\n")

    Puntos_totales = 0

    for i, item in enumerate(DATOS ["puntos"], start=1):
        print(f"[{i}] \t{item['jugada']}\t:\t{item['valor']}")
        Puntos_totales += item["valor"]

    print("\n════════════════════════════════════")
    print(f"PUNTAJE TOTAL:\t{Puntos_totales}")
    print("════════════════════════════════════\n")
