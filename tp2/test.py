import os
import time
import math
import matplotlib.pyplot as plt
from tp2 import *
from generar_datos import *

BASE=3
EXPONENTE_DESDE=1
EXPONENTE_HASTA=11
VARIACION_E=10
VARIACION_S=10

def generar_archivos(base, exp_desde, exp_hasta, v_e, v_s):
  archivos = []
  for exp in range(exp_desde, exp_hasta):
        cantidad = int(base**exp)
        archivo = f'tests/cronograma_{cantidad}.txt'
        generar_datos(cantidad, archivo, v_e, v_s)
        archivos.append({ 'nombre': archivo, 'cantidad': cantidad })
  return archivos
  

def calcular_tiempos_en_masa(base, exp_desde, exp_hasta, v_e, v_s):
    print("\n=== Calculando tiempos de ejecución ===")
    archivos = generar_archivos(base, exp_desde, exp_hasta, v_e, v_s)    
    performance = []
    for i, archivo in enumerate(archivos):
        print(f"Calculando test {i} con {archivo['cantidad']} dias")
        energia, descanso = obtener_cronograma(archivo['nombre'])
        
        inicio = time.time()
        dias = ganacias_por_dia(energia, descanso)
        entrenamientos = organizar_entrenamientos(dias, energia, descanso)
        fin = time.time()
        tiempo_ejecucion = fin - inicio
        
        test = {'dias': archivo['cantidad'], 'tiempo': tiempo_ejecucion}
        print(f"Test {i} terminado, tiempo total = {tiempo_ejecucion}s, performance = {tiempo_ejecucion / archivo['cantidad'] * 1000000000} ns/videos")
        performance.append(test)

    return performance

def graficar_performance(tests):
    print("Graficando performance...")
    dias = []
    tiempos = []
    dias_string = []
    tiempos_por_dias = []

    for test in tests:
        dias.append(test['dias'])
        tiempos.append(test['tiempo'])
        dias_string.append(str(test['dias']))
        tiempos_por_dias.append(test['tiempo'] / test['dias'])

    plt.figure(figsize=(12, 7))
    plt.plot(dias, tiempos, label="Algoritmo", marker='o')
    plt.xlabel("Cantidad de dias")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Tiempo de ejecución en función de la cantidad de dias")
    plt.legend()
    plt.show()
    
    plt.figure(figsize=(12, 7))
    plt.bar(dias_string, tiempos_por_dias, color='blue', label="Algoritmo")
    plt.xlabel("Cantidad de dias")
    plt.ylabel("Tiempo de ejecución x dias (segundos)")
    plt.title("Tiempo de ejecución por dias en función de la cantidad de dias")
    plt.show()
    

def calcular_optimizacion():
  print('=== Calcular operaciones ahorradas en los archivos de la catedra ===')  
  archivos = generar_archivos(BASE, EXPONENTE_DESDE, EXPONENTE_HASTA, VARIACION_E, VARIACION_S)
  
  for i, archivo in enumerate(archivos):
    energia, descanso = obtener_cronograma(archivo['nombre'])
    dias = ganacias_por_dia(energia, descanso)
    
    valores_opt = 0
    valores_sin_opt = 0
    for numero_dia, dia in enumerate(dias):
      valores_opt += len(dia)
      valores_sin_opt += numero_dia + 1
    
    print(f'Archivo: {archivo["nombre"]}, optimizado: {valores_opt}, sin optimizar: {valores_sin_opt}, diferencia: {(valores_sin_opt - valores_opt) / valores_sin_opt * 100}%')
    
    
calcular_optimizacion()
tests = calcular_tiempos_en_masa(BASE, EXPONENTE_DESDE, EXPONENTE_HASTA, VARIACION_E, VARIACION_S)
graficar_performance(tests)
