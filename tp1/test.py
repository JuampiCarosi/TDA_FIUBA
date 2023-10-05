import time
import math
import matplotlib.pyplot as plt
from tp1 import *
from generar_datos import *

BASE=4
EXPONENTE_DESDE=1
EXPONENTE_HASTA=12
VARIACION_SCALONI=10
VARIACION_AYUDANTES=10

def calcular_tiempos_en_masa():
    print("Calculando tiempos de ejecución...")
    print(f"Tests a realizar: {EXPONENTE_HASTA - EXPONENTE_DESDE}")

    performance = []
    for exp in range(EXPONENTE_DESDE, EXPONENTE_HASTA):
        cantidad = int(BASE**exp)
        print(f"Calculando test {exp} con {cantidad} videoss")
        generar_datos(cantidad, f'tests/videoss_{cantidad}.txt', VARIACION_SCALONI, VARIACION_AYUDANTES)
        videos = obtener_videos(f"tests/videoss_{cantidad}.txt")
        inicio = time.time()
        optimizar_cronograma(videos)
        calcular_tiempo(videos)
        fin = time.time()
        tiempo_ejecucion = fin - inicio
        test = {'cantidad': cantidad, 'tiempo': tiempo_ejecucion}
        print(f"Test {exp} terminado, tiempo total = {tiempo_ejecucion}s, performance = {tiempo_ejecucion / cantidad * 1000000000} ns/videos")
        performance.append(test)

    return performance

def graficar_performance(tests):
    print("Graficando performance...")
    cantidades = []
    tiempos = []
    cantidades_string = []
    tiempos_por_videos = []
    mejor_por_videos = 999999

    for test in tests:
        mejor_por_videos = min(mejor_por_videos, test['tiempo'] / test['cantidad'])
        cantidades.append(test['cantidad'])
        tiempos.append(test['tiempo'])
        cantidades_string.append(str(test['cantidad']))
        tiempos_por_videos.append(test['tiempo'] / test['cantidad'])

    cantidades_big_o = []
    nlogn = []
    n = []
    for i in range(1, int(tests[-1]['cantidad']), 100):
        cantidades_big_o.append(i)
        nlogn.append(mejor_por_videos * i * math.log10(i))
        n.append(mejor_por_videos * i)

    plt.figure(figsize=(12, 7))
    plt.plot(cantidades, tiempos, label="Algoritmo", marker='o')
    plt.plot(cantidades_big_o, nlogn, color='red', label="O(nlogn)")
    plt.plot(cantidades_big_o, n, color='green', label="O(n)")
    plt.xlabel("Cantidad de videoss")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Tiempo de ejecución en función de la cantidad de videoss")
    plt.legend()
    plt.show()
    
    plt.figure(figsize=(12, 7))
    plt.bar(cantidades_string, tiempos_por_videos, color='blue', label="Algoritmo")
    plt.xlabel("Cantidad de videoss")
    plt.ylabel("Tiempo de ejecución x videos (segundos)")
    plt.title("Tiempo de ejecución por videos en función de la cantidad de videoss")
    plt.show()
    


tests = calcular_tiempos_en_masa()
graficar_performance(tests)
