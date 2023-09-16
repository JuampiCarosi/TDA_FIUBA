import time
import math
import matplotlib.pyplot as plt
from tp1 import *
from generar_datos import *

BASE=4
EXPONENTE_DESDE=1
EXPONENTE_HASTA=12

def calcular_tiempos_en_masa():
    print("Calculando tiempos de ejecución...")
    print(f"Tests a realizar: {EXPONENTE_HASTA - EXPONENTE_DESDE}")

    performance = []
    for exp in range(EXPONENTE_DESDE, EXPONENTE_HASTA):
        cantidad = int(BASE**exp)
        print(f"Calculando test {exp} con {cantidad} elementos")
        generar_datos(cantidad, f'tests/elementos_{cantidad}.txt')
        videos = obtener_videos(f"tests/elementos_{cantidad}.txt")
        inicio = time.time()
        optimizar_cronograma(videos)
        calcular_tiempo(videos)
        fin = time.time()
        tiempo_ejecucion = fin - inicio
        test = {'cantidad': cantidad, 'tiempo': tiempo_ejecucion}
        print(f"Test {exp} terminado, performance = {tiempo_ejecucion / cantidad * 1000000000} ns/elemento")
        performance.append(test)

    return performance

def graficar_performance(tests):
    print("Graficando performance...")
    cantidades = []
    tiempos = []
    mejor_por_elemento = 999999

    for test in tests:
        mejor_por_elemento = min(mejor_por_elemento, test['tiempo'] / test['cantidad'])
        cantidades.append(test['cantidad'])
        tiempos.append(test['tiempo'])

    cantidades_big_o = []
    nlogn = []
    n = []
    for i in range(1, int(tests[-1]['cantidad']), 100):
        cantidades_big_o.append(i)
        nlogn.append(mejor_por_elemento * i * math.log10(i))
        n.append(mejor_por_elemento * i)

    plt.plot(cantidades, tiempos, label="Algoritmo")
    plt.plot(cantidades_big_o, nlogn, color='red', label="O(nlogn)")
    plt.plot(cantidades_big_o, n, color='green', label="O(n)")
    plt.xlabel("Cantidad de elementos")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Tiempo de ejecución en función de la cantidad de elementos")
    plt.legend()
    plt.show()


tests = calcular_tiempos_en_masa()
graficar_performance(tests)
