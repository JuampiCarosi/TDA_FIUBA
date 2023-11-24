import os
import sys
from utils import leer_archivo

def mostrar_min_max_longitud_periodista_de_cada_set(archivo_corte):
    generados = os.listdir("generados")
    generados = [int(file.split('.')[0]) for file in generados]
    generados.sort()

    for cantidad in generados:
        if cantidad > archivo_corte:
            break
        jugadores, subconjuntos = leer_archivo(f'generados/{cantidad}.txt')
        max_jugadores = max([len(subconjunto) for subconjunto in subconjuntos])
        min_jugadores = min([len(subconjunto) for subconjunto in subconjuntos])
        print(f'Cantidad {cantidad} - Max {max_jugadores} - Min {min_jugadores}')
    
if __name__ == '__main__':
    archivo_de_corte = int(sys.argv[1])
    mostrar_min_max_longitud_periodista_de_cada_set(archivo_de_corte)