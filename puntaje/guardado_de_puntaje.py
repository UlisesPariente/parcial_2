import os
from datos.datos import DATOS


def suma_puntos ():
    puntaje_total = 0
    for i in range(len(DATOS)):
        puntaje_total +=  DATOS ["puntos"][i]["valor"]
    return puntaje_total

def guardar_puntuacion(nombre, puntuacion):
    archivo = "puntuaciones.csv"
    puntuaciones = []

   
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            lineas = f.readlines()

        for linea in lineas:
            partes = linea.strip().split(",")
            if len(partes) == 2:
                n = partes[0]
                p = int(partes[1])
                puntuaciones.append((n, p))

    
    puntuaciones.append((nombre, puntuacion))

  
    n = len(puntuaciones)
    for i in range(n):
        for j in range(0, n - i - 1):
            if puntuaciones[j][1] < puntuaciones[j + 1][1]:
                puntuaciones[j] = puntuaciones[j + 1]
                puntuaciones[j + 1] = puntuaciones[j]

   
    if len(puntuaciones) > 10:
        puntuaciones = puntuaciones[:10]

   
    with open(archivo, "w", encoding="utf-8") as f:
        for n, p in puntuaciones:
            f.write(f"{n},{p}\n")

    print(f"Puntuación guardada: {nombre} - {puntuacion}")