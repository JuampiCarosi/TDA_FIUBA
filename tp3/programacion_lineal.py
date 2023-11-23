import sys
import time
from pulp import LpProblem, LpVariable, LpMinimize, lpSum

from utils import leer_archivo

def programacion_lineal(jugadores, subconjuntos):

    problema = LpProblem("Hitting set", LpMinimize)

    jugadores_seleccionados = {
        jugador: LpVariable(
            f"jugador_{jugador}", cat='Binary') for jugador in jugadores
    }

    problema += lpSum(jugadores_seleccionados[e] for e in jugadores)

    for subset in subconjuntos:
        problema += lpSum(jugadores_seleccionados[e] for e in subset) >= 1

    problema.solve()

    solucion = []
    for e in jugadores:
        if jugadores_seleccionados[e].value() == 1:
            solucion.append(e)
            
    return solucion
        
if __name__ == '__main__':
    jugadores, subconjuntos = leer_archivo(sys.argv[1])

    start = time.time()
    solucion = programacion_lineal(jugadores, subconjuntos)
    end = time.time()

    print("Tiempo de ejecucion:", end - start)
    print("Cantidad seleccionada:", len(solucion))
    print("Jugadores seleccionados:", solucion)

