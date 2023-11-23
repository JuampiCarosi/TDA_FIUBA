def leer_archivo(nombre_archivo):
    archivo = open(nombre_archivo, "r")
    jugadores = []
    subconjuntos = [] 
    for line in archivo:
        line_stripped = line.strip()
        subset = line_stripped.split(",")
        subconjuntos.append(subset)
        for e in subset:
            jugador = e.strip()
            if jugador not in jugadores:
                jugadores.append(jugador)
    archivo.close()
    return jugadores, subconjuntos
