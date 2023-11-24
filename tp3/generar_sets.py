import os
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

jugadores = leer_base_de_jugadores()

def crear_set(cant_periodistas, jugadores_prom_por_periodista):
    archivo = open("generados/" + str(cant_periodistas) + ".txt", "w")
    for periodista in range(cant_periodistas):
        cant_jugadores = round(jugadores_prom_por_periodista * random.randint(5, 15) / 10)
        jugadores_set = set()
        
        while len(jugadores_set) < cant_jugadores:
            jugador = random.choice(jugadores)
            jugadores_set.add(jugador)
            
        linea_set = ','.join(jugadores_set) + '\n'
        archivo.write(linea_set)
    archivo.close()
    
   
def armar_sets(jugadores_prom_por_periodista):
    for file in os.listdir("generados"):
        os.remove("generados/" + file)

    # 10 en 10 hasta 50 // 5
    for i in range(10, 51, 10):
       crear_set(i, jugadores_prom_por_periodista)
    
    # 25 en 25 hasta 100 // 2
    for i in range(50, 101, 25):
       crear_set(i, jugadores_prom_por_periodista)
       
    # 50 en 50 hasta 500 // 8
    for i in range(100, 501, 50):
       crear_set(i, jugadores_prom_por_periodista)
       
    # 100 en 100 hasta 1000 // 5
    for i in range(500, 1001, 100):
       crear_set(i, jugadores_prom_por_periodista)
       
    # 500 en 500 hasta 5000 // 8
    for i in range(1000, 5001, 500):
       crear_set(i, jugadores_prom_por_periodista)



if __name__ == '__main__':
    
    jugadores_prom_por_periodista = int(sys.argv[1])
    armar_sets(jugadores_prom_por_periodista)            