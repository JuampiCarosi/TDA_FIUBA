from asyncio import sleep
import os
import random
import sys

random.seed(10)

def leer_base_de_jugadores():
    archivo = open("jugadores.txt", "r")
    jugadores = []
    for jugador in archivo:
        jugador_stripped = jugador.strip()
        jugadores.append(jugador_stripped)
    archivo.close()
    return jugadores

jugadores = leer_base_de_jugadores()

def crear_archivo(cant_periodistas, variedad_jugadores, jugadores_prom_por_periodista):

    jugadores_posibles = jugadores[:variedad_jugadores]    
    archivo = open("generados/" + str(cant_periodistas) + ".txt", "w")
    for periodista in range(cant_periodistas):
        cant_jugadores = round(jugadores_prom_por_periodista * random.randint(5, 15) / 10)
        jugadores_set = []
        
        while len(jugadores_set) < cant_jugadores:
            jugador = random.choice(jugadores_posibles)
            if jugador not in jugadores_set:
                jugadores_set.append(jugador)
            
        linea_set = ','.join(jugadores_set) + '\n'
        archivo.write(linea_set)
    archivo.close()
    
   
def armar_sets(variedad_jugadores, jugadores_prom_por_periodista):
    for file in os.listdir("generados"):
        os.remove("generados/" + file)
    
    generados = []

    # 10 en 10 hasta 50 // 5
    for i in range(10, 51, 10):
        generados.append(i)
        crear_archivo(i, variedad_jugadores, jugadores_prom_por_periodista)
    
    # 25 en 25 hasta 100 // 2
    for i in range(50, 101, 25):
        generados.append(i)
        crear_archivo(i, variedad_jugadores, jugadores_prom_por_periodista)
       
    # 50 en 50 hasta 500 // 8
    for i in range(100, 501, 50):
        generados.append(i)
        crear_archivo(i, variedad_jugadores, jugadores_prom_por_periodista)
       
    # 100 en 100 hasta 1000 // 5
    for i in range(500, 1001, 100):
        generados.append(i)
        crear_archivo(i, variedad_jugadores, jugadores_prom_por_periodista)
       
    # 500 en 500 hasta 5000 // 8
    for i in range(1000, 5001, 500):
        generados.append(i)
        crear_archivo(i, variedad_jugadores, jugadores_prom_por_periodista)
        
    return generados

if __name__ == '__main__':
    variedad_jugadores = int(sys.argv[1])
    jugadores_prom_por_periodista = int(sys.argv[2])
    armar_sets(variedad_jugadores, jugadores_prom_por_periodista)            