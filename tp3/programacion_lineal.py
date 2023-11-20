from pulp import LpProblem, LpVariable, LpMinimize

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

problema = LpProblem("Hitting_Set", LpMinimize)

elemento_seleccionado = {e: LpVariable(
    f"elemento_{e}", cat='Binary') for e in elementos}

problema += sum(elemento_seleccionado[e] for e in elementos)

for subset in subconjuntos:
    problema += sum(elemento_seleccionado[e] for e in subset) >= 1

problema.solve()

print("Cantidad seleccionada:", problema.objective.value())
print("Elementos seleccionados:")
for e in elementos:
    if elemento_seleccionado[e].value() == 1:
        print(e)
