from pulp import LpProblem, LpVariable, LpMinimize, lpSum, LpContinuous, value, lpSum

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

b = max(len(subset) for subset in subconjuntos)
print("b:", b)

elementos_seleccionados = {
    elemento: LpVariable(
        f"elemento_{elemento}", lowBound=0, upBound=1, cat='Continuous') for elemento in elementos
}

problema += lpSum(elementos_seleccionados[e] for e in elementos)

for subset in subconjuntos:
    problema += lpSum(elementos_seleccionados[e] for e in subset) >= 1
problema.solve()

solucion = []
for e in elementos:
    if value(elementos_seleccionados[e]) > 1/b:
        print(value(elementos_seleccionados[e]))
        solucion.append(e)
print("Cantidad:", len(solucion))


def hitting_set_lp_relaxed(sets):
    # Crear un problema de programación lineal
    prob = LpProblem("HittingSetRelaxed", LpMinimize)

    # Crear variables de decisión
    x = LpVariable.dict("x", range(1, len(sets) + 1),
                        0, 1, LpContinuous)

    # Crear variable b para redondeo
    b = max(len(s) for s in sets)

    # Definir la función objetivo
    prob += lpSum(x[i] for i in range(1, len(sets) + 1)), "Objective"

    # Definir restricciones
    for s in sets:
        prob += lpSum(x[i] for i in range(1, len(sets) + 1)
                      if len(sets[i-1].intersection(s)) > 0) >= 1, f"Cover_{s}"

    # Resolver el problema
    prob.solve()

    # Obtener el hitting set óptimo
    hitting_set = {i for i, var in x.items() if var.value() >= 1 / b}

    return hitting_set
