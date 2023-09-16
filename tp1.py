import sys
import time
import progressbar

def obtener_videos(archivo_txt):
    with open(archivo_txt, "r") as archivo:
        lineas = archivo.readlines()

    primera_linea = True
    videos = []

    for linea in lineas:
        if primera_linea:
            primera_linea = False
            continue
        duraciones = linea.strip().split(',')
        video = { 'S_i': int(duraciones[0]), 'A_i': int(duraciones[1]) }
        videos.append(video)
           
    archivo.close()
    return videos

def optimizar_cronograma(videos):
    return sorted(videos, key=lambda video: video['A_i'], reverse=True)

def calcular_tiempo(videos):
    duracion_total = 0
    tiempo_scaloni = 0
    for video in videos:
        duracion_total = max(duracion_total, tiempo_scaloni + video['S_i'] + video['A_i'])
        tiempo_scaloni += video['S_i']
    return duracion_total

def main():
    archivo_txt = sys.argv[1]
    videos = obtener_videos(archivo_txt)
    videos_ordenados = optimizar_cronograma(videos)
    tiempo_total = calcular_tiempo(videos_ordenados)
    print(tiempo_total)



# main()