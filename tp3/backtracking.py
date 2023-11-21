
archivo = open("10_todos.txt", "r")
elementos = set()
subconjuntos = []
for line in archivo:
    line_stripped = line.strip()
    subset = line_stripped.split(",")
    subconjuntos.append(subset)
    for e in subset:
        elementos.add(e.strip())
archivo.close()


def es_valido(seleccionados, subconjuntos):
    for subset in subconjuntos:
        if not any(e in seleccionados for e in subset):
            return False
    return True


mejor = float("inf")


def backtracking(elementos, subconjuntos, seleccionados, i, mejor_solucion=[]):
    global mejor
    if len(mejor_solucion) > 0 and len(mejor_solucion) < mejor:
        mejor = len(mejor_solucion)
        print("Mejor solucion encontrada:", mejor)

    if len(seleccionados) > 11:
        return mejor_solucion
    if i >= len(elementos):
        return mejor_solucion

    if len(mejor_solucion) > 0 and len(seleccionados) >= len(mejor_solucion):
        return mejor_solucion

    if es_valido(seleccionados, subconjuntos):
        return list(seleccionados)

    seleccionados.add(elementos[i])
    solucion = backtracking(elementos, subconjuntos,
                            seleccionados, i + 1, mejor_solucion)

    if len(mejor_solucion) == 0 and len(solucion) > 0:
        mejor_solucion[:] = solucion

    if solucion is not None and len(solucion) < len(mejor_solucion):
        mejor_solucion[:] = solucion

    seleccionados.remove(elementos[i])
    solucion_sin = backtracking(
        elementos, subconjuntos, seleccionados, i + 1, mejor_solucion)

    if len(solucion) == 0:
        return solucion_sin

    if len(solucion_sin) == 0:
        return solucion

    return min(solucion, solucion_sin, key=len)


solucion = backtracking(list(elementos), subconjuntos, set(), 0)
print("Cantidad seleccionada:", len(solucion))
print("Elementos seleccionados:", solucion)
