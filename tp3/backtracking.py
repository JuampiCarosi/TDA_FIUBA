import sys
import time

from utils import leer_archivo


def es_valido(seleccionados, subconjuntos):
    for subset in subconjuntos:
        if not any(e in seleccionados for e in subset):
            return False
    return True



def backtracking(jugadores, subconjuntos, mejor_solucion, seleccionados = set(), i = 0):
    if i >= len(jugadores):
        return

    if len(mejor_solucion) > 0 and len(seleccionados) >= len(mejor_solucion):
        return

    if es_valido(seleccionados, subconjuntos):
        print("Mejor solucion encontrada:", len(seleccionados))
        mejor_solucion[:] = seleccionados.copy()
        return

    seleccionados.add(jugadores[i])
    
    backtracking(jugadores, subconjuntos, mejor_solucion,
                            seleccionados, i + 1)

    seleccionados.remove(jugadores[i])
    
    backtracking(
        jugadores, subconjuntos,mejor_solucion, seleccionados, i + 1)



if __name__ == '__main__':
    jugadores, subconjuntos = leer_archivo(sys.argv[1])

    solucion = []   
    start = time.time()
    backtracking(jugadores, subconjuntos, solucion)
    end = time.time()

    print("Tiempo de ejecucion:", end - start)
    print("Cantidad seleccionada:", len(solucion))
    print("Jugadores seleccionados:", solucion)
