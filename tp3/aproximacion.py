from pulp import LpProblem, LpVariable, LpMinimize, lpSum, LpContinuous, value, lpSum
import sys

def leer_subconjuntos_de_jugadores(nombre_archivo):
    archivo = open(nombre_archivo, "r")
    jugadores = set()
    subconjuntos = []
    for linea in archivo:
        linea_stripped = linea.strip()
        subset = linea_stripped.split(",")
        subconjuntos.append(subset)
        for e in subset:
            jugadores.add(e.strip())
    archivo.close()
    return jugadores, subconjuntos

def hitting_set_relajado(elementos, subconjuntos):
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
    return solucion


def main():
    if len(sys.argv) < 2:
        print("No se ingreso nombre de archivo")
        return
    nombre_archivo = sys.argv[1]
    elementos, subconjuntos = leer_subconjuntos_de_jugadores(nombre_archivo)
    solucion = hitting_set_relajado(elementos, subconjuntos)
    print("Cantidad seleccionada:", len(solucion))
    print("Jugadores seleccionados:")
    for jugador in solucion:
        print(jugador)

main()


