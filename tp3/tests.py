import os
import sys
import time

from matplotlib import pyplot as plt
from greedy import greedy_preciso, greedy_rapido
from programacion_lineal import programacion_lineal
from aproximacion import aproximacion
from backtracking import backtracking
from generar_sets import armar_sets
from utils import leer_archivo

generados = os.listdir("generados")
generados = [int(file.split('.')[0]) for file in generados]
generados.sort()



def test_greedy_rapido():
  resultados_rapido = []
  
  for cantidad in generados:
    jugadores, subconjuntos = leer_archivo(f'generados/{cantidad}.txt')
    
    start = time.time()
    solucion = greedy_rapido(jugadores, subconjuntos)
    end = time.time()
    resultados_rapido.append([cantidad, end - start, len(solucion)])
    
  return resultados_rapido

def test_greedy_preciso():
  resultados_preciso = []
  
  for cantidad in generados:
    jugadores, subconjuntos = leer_archivo(f'generados/{cantidad}.txt')
    
    start = time.time()
    solucion = greedy_preciso(jugadores, subconjuntos)
    end = time.time()
    resultados_preciso.append([cantidad, end - start, len(solucion)])
    
  return resultados_preciso
  

def test_lineal_entera():
  resultados = []
  
  for cantidad in generados:
    if cantidad > 1000:
      return resultados
    jugadores, subconjuntos = leer_archivo(f'generados/{cantidad}.txt')
    
    start = time.time()
    solucion = programacion_lineal(jugadores, subconjuntos)
    end = time.time()
    resultados.append([cantidad, end - start, len(solucion)])
    
  return resultados

def test_backtracking():
  resultados = []
  
  for cantidad in generados:
    if cantidad > 200:
      return resultados
    jugadores, subconjuntos = leer_archivo(f'generados/{cantidad}.txt')
    
    start = time.time()
    solucion = backtracking(jugadores, subconjuntos)
    end = time.time()
    resultados.append([cantidad, end - start, len(solucion)])
    
  return resultados

def test_aproximacion():
  resultados = []
  
  for cantidad in generados:
    jugadores, subconjuntos = leer_archivo(f'generados/{cantidad}.txt')
    
    start = time.time()
    solucion = aproximacion(jugadores, subconjuntos)
    end = time.time()
    resultados.append([cantidad, end - start, len(solucion)])
    
  return resultados
    
def mostrar_grafico_cantidad_tiempo(resultados_algoritmos):
  for (resultados, algoritmo) in resultados_algoritmos:
    plt.plot([resultado[0] for resultado in resultados], [resultado[1] for resultado in resultados], label=algoritmo)

  plt.xlabel('Cantidad periodistas')
  plt.ylabel('Tiempo (s)')
  plt.legend()
  plt.show()
    
def mostrar_grafico_cantidad_seleccionados(resultados_algoritmos):
  for (resultados, algoritmo) in resultados_algoritmos:
    plt.plot([resultado[0] for resultado in resultados], [resultado[2] for resultado in resultados], label=algoritmo)

  plt.xlabel('Cantidad periodistas')
  plt.ylabel('Jugadores seleccionados')
  plt.legend()
  plt.show()

if __name__ == '__main__':
  
  print(sys.argv)
  
  algormitmos = set(sys.argv[1].split(','))
  jugadores_prom_por_periodista = [int(promedio) for promedio in sys.argv[2].split(',')]
  
  resultados = []
  
  for promedio in jugadores_prom_por_periodista:
    armar_sets(promedio)
    
    if 'greedy-r' in algormitmos or 'todos' in algormitmos:
      resultados.append((test_greedy_rapido(), f'Greedy rapido {promedio}'))
    
    if 'greedy-p' in algormitmos or 'todos' in algormitmos:
      resultados.append((test_greedy_preciso(), f'Greedy preciso {promedio}'))
    
    if 'entera' in algormitmos or 'todos' in algormitmos:
      resultados.append((test_lineal_entera(), f'Lineal entera {promedio}'))
      
    if 'backtracking' in algormitmos or 'todos' in algormitmos:
      resultados.append((test_backtracking(), f'Backtracking {promedio}'))
      
    if 'aproximacion' in algormitmos or 'todos' in algormitmos:
      resultados.append((test_aproximacion(), f'Aproximacion {promedio}'))
    
    
  mostrar_grafico_cantidad_tiempo(resultados)
  mostrar_grafico_cantidad_seleccionados(resultados)

  