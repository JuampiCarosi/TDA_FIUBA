from pulp import LpProblem, LpVariable, LpMinimize, lpSum

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

problema = LpProblem("Hitting set", LpMinimize)

elementos_seleccionados = {
    elemento: LpVariable(
        f"elemento_{elemento}", cat='Binary') for elemento in elementos
}

problema += lpSum(elementos_seleccionados[e] for e in elementos)

for subset in subconjuntos:
    problema += lpSum(elementos_seleccionados[e] for e in subset) >= 1

problema.solve()

print("Cantidad seleccionada:", problema.objective.value())
print("Elementos seleccionados:")
for e in elementos:
    if elementos_seleccionados[e].value() == 1:
        print(e)
