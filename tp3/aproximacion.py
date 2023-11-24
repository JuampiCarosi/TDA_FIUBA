from pulp import LpProblem, LpVariable, LpMinimize, lpSum, LpContinuous, value, lpSum
import sys

from utils import leer_archivo

def aproximacion(jugadores, subconjuntos):
    problema = LpProblem("Hitting set", LpMinimize)

    b = max(len(subset) for subset in subconjuntos)
    print("b:", b)

    jugadores_seleccionados = {
        jugador: LpVariable(
            f"jugador_{jugador}", lowBound=0, upBound=1, cat='Continuous') for jugador in jugadores
    }

    problema += lpSum(jugadores_seleccionados[e] for e in jugadores)

    for subset in subconjuntos:
        problema += lpSum(jugadores_seleccionados[e] for e in subset) >= 1
    problema.solve()

    solucion = []
    for e in jugadores:
        if value(jugadores_seleccionados[e]) > 1/b:
            print(value(jugadores_seleccionados[e]))
            solucion.append(e)
    return solucion


def main():
    if len(sys.argv) < 2:
        print("No se ingreso nombre de archivo")
        return
    nombre_archivo = sys.argv[1]
    jugadores, subconjuntos = leer_archivo(nombre_archivo)
    solucion = aproximacion(jugadores, subconjuntos)
    print("Cantidad seleccionada:", len(solucion))
    print("Jugadores seleccionados:")
    for jugador in solucion:
        print(jugador)


if __name__ == '__main__':
    main()  


