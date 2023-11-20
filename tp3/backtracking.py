archivo = open("200.txt", "r")
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
        if not any(e in subset for e in seleccionados):
            return False
    return True


def backtracking(elementos, subconjuntos, seleccionados, i, mejor_solucion=None):
    print("llamada rec ", i, "mejor:", len(mejor_solucion or []))
    if len(seleccionados) > 11:
        return mejor_solucion
    if i >= len(elementos):
        return mejor_solucion

    if mejor_solucion is not None and len(seleccionados) >= len(mejor_solucion):
        return mejor_solucion

    if es_valido(seleccionados, subconjuntos):
        return seleccionados.copy()

    seleccionados.append(elementos[i])
    solucion = backtracking(elementos, subconjuntos,
                            seleccionados, i + 1, mejor_solucion)

    if mejor_solucion is None:
        mejor_solucion = solucion

    if solucion is not None and len(solucion) < len(mejor_solucion):
        mejor_solucion = solucion

    seleccionados.remove(elementos[i])
    solucion_sin = backtracking(
        elementos, subconjuntos, seleccionados, i + 1, mejor_solucion)

    if solucion is None:
        return solucion_sin

    if solucion_sin is None:
        return solucion

    return min(solucion, solucion_sin, key=len)


solucion = backtracking(list(elementos), subconjuntos, [], 0)
print("Cantidad seleccionada:", len(solucion))
