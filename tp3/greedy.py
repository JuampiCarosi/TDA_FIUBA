import heapq

archivo = open("75.txt", "r")
elementos = set()
subconjuntos = []
for linea in archivo:
    linea_stripped = linea.strip()
    subset = linea_stripped.split(",")
    subconjuntos.append(subset)
    for e in subset:
        elementos.add(e.strip())
archivo.close()


def es_valido(seleccionados, subconjuntos):
    for subset in subconjuntos:
        if not any(e in seleccionados for e in subset):
            return False
    return True


def subsets_a_los_que_pertenecen(elemento, subconjuntos, subsets_cubiertos):
    subsets = set()
    for i in range(len(subconjuntos)):
        subset = subconjuntos[i]
        if elemento in subset and i not in subsets_cubiertos:
            subsets.add(i)
    return subsets


def greedy(elementos, subconjuntos):
    frecuencias = {elemento: 0 for elemento in elementos}

    for subset in subconjuntos:
        for elemento in subset:
            frecuencias[elemento] += 1

    frecuencias_heap = [(-freq, elemento)
                        for elemento, freq in frecuencias.items()]
    heapq.heapify(frecuencias_heap)

    seleccionados = set()
    subsets_cubiertos = set()

    while not es_valido(seleccionados, subconjuntos):
        if not frecuencias_heap:
            break

        _, maximo = heapq.heappop(frecuencias_heap)
        subsets_cubiertos_nuevos = subsets_a_los_que_pertenecen(
            maximo, subconjuntos, subsets_cubiertos)

        if not subsets_cubiertos_nuevos:
            continue

        subsets_cubiertos |= subsets_cubiertos_nuevos
        seleccionados.add(maximo)

    return seleccionados


print(len(greedy(elementos, subconjuntos)))
