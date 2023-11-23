import random
import sys

def leer_base_de_jugadores():
    archivo = open("jugadores.txt", "r")
    jugadores = []
    for jugador in archivo:
        jugador_stripped = jugador.strip()
        jugadores.append(jugador_stripped)
    archivo.close()
    return jugadores

def armar_sets(cantidad_maxima_sets, jugadores):
    for i in range(10, cantidad_maxima_sets + 1, 20):
        archivo = open("sets_prueba/" + str(i) + ".txt", "w")
        for j in range(i):
            tamano_set = random.randint(3, 11)
            jugadores_set = set()
            for k in range(tamano_set):
                jugador = random.choice(jugadores)
                while jugador in jugadores_set:
                    jugador = random.choice(jugadores)
                jugadores_set.add(jugador)
            linea_set = ','.join(jugadores_set) + '\n'
            archivo.write(linea_set)
        archivo.close()

def armar_sets_con_diferencia_de_cantidad_por_subset(cantidad_subsets, jugadores, minimo, rango_diferencia, repeticiones):
    maximo = minimo + rango_diferencia
    for i in range(repeticiones):
        archivo = open("sets_prueba/" + str(cantidad_subsets) + "_" + str(maximo-minimo) + ".txt", "w")
        for j in range(cantidad_subsets):
            tamano_set = random.randint(minimo, maximo)
            jugadores_set = set()
            for k in range(tamano_set):
                jugador = random.choice(jugadores)
                while jugador in jugadores_set:
                    jugador = random.choice(jugadores)
                jugadores_set.add(jugador)
            linea_set = ','.join(jugadores_set) + '\n'
            archivo.write(linea_set)
        archivo.close()
        maximo -= rango_diferencia // repeticiones

def main():
    jugadores = leer_base_de_jugadores()
    if len(sys.argv) > 2:
        print("Uso: python generar_sets.py <cantidad_subsets> <repeticiones> <minimo> <rango_diferencia>")
        armar_sets_con_diferencia_de_cantidad_por_subset(int(sys.argv[1]), jugadores, int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[2]))
        return
    cantidad_maxima_sets = int(sys.argv[1])
    armar_sets(cantidad_maxima_sets, jugadores)

main()
            
        




