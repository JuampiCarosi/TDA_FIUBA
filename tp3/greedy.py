import heapq
import sys
import time

from utils import leer_archivo


def subsets_a_los_que_pertenecen(elemento, subconjuntos, subsets_cubiertos):
    subsets = set()
    for i in range(len(subconjuntos)):
        subset = subconjuntos[i]
        if elemento in subset and i not in subsets_cubiertos:
            subsets.add(i)
    return subsets

def generar_frecuencias_heap(jugadores, subconjuntos, subsets_cubiertos):
    frecuencias = {jugador: 0 for jugador in jugadores}

    for (i, subset) in enumerate(subconjuntos):
        if i not in subsets_cubiertos:
            for jugador in subset:
                frecuencias[jugador] += 1

    frecuencias_heap = [(-freq, jugador)
                        for jugador, freq in frecuencias.items()]

    heapq.heapify(frecuencias_heap)
    return frecuencias_heap


def greedy_rapido(jugadores, subconjuntos):
    seleccionados = set()
    subsets_cubiertos = set()
    
    frecuencias_heap = generar_frecuencias_heap(jugadores, subconjuntos, subsets_cubiertos)

    while not len(subsets_cubiertos) == len(subconjuntos):
        _, maximo = heapq.heappop(frecuencias_heap)
        
        subsets_cubiertos_nuevos = subsets_a_los_que_pertenecen(
            maximo, subconjuntos, subsets_cubiertos)

        if not subsets_cubiertos_nuevos:
            continue

        subsets_cubiertos |= subsets_cubiertos_nuevos
        seleccionados.add(maximo)

    return seleccionados


def greedy_preciso(jugadores, subconjuntos):
    
    seleccionados = set()
    subsets_cubiertos = set()

    while not len(subsets_cubiertos) == len(subconjuntos):
        frecuencias_heap = generar_frecuencias_heap(jugadores, subconjuntos, subsets_cubiertos)

        _, maximo = heapq.heappop(frecuencias_heap)
        
        subsets_cubiertos_nuevos = subsets_a_los_que_pertenecen(
            maximo, subconjuntos, subsets_cubiertos)

        subsets_cubiertos |= subsets_cubiertos_nuevos
        seleccionados.add(maximo)

    return seleccionados


if __name__ == "__main__":
    jugadores, subconjuntos = leer_archivo(sys.argv[1])
    
    start = time.time()
    solucion = greedy_rapido(jugadores, subconjuntos)
    end = time.time()
    print("===  Greedy rapido  ===")
    print("Tiempo de ejecucion:", end - start)
    print("Cantidad seleccionada:", len(solucion))
    print("Jugadores seleccionados:", solucion)
    
    start = time.time()
    solucion = greedy_preciso(jugadores, subconjuntos)
    end = time.time()
    print("\n===  Greedy preciso  ===")
    print("Tiempo de ejecucion:", end - start)
    print("Cantidad seleccionada:", len(solucion))
    print("Jugadores seleccionados:", solucion)