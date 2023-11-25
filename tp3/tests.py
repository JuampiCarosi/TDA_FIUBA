import math
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
    if cantidad > 300:
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
    if cantidad > 400:
      return resultados
    jugadores, subconjuntos = leer_archivo(f'generados/{cantidad}.txt')
    
    start = time.time()
    solucion = backtracking(jugadores, subconjuntos)
    end = time.time()
    resultados.append([cantidad, end - start, len(solucion)])
    
  return resultados

def test_lineal_relajada():
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

def comparacion_programacion_lineal():
  entera = test_lineal_entera()
  aprox = test_lineal_relajada()
  
  diferencias = []
  for i in range(len(entera)):
    diferencia = aprox[i][2] / entera[i][2]
    print(f'Diferencia {entera[i][0]} periodistas: ', {diferencia})
    print(f'    Entera {entera[i][2]} jugadores')
    print(f'    Aproximacion {aprox[i][2]} jugadores')
    diferencias.append(diferencia)
    
  print(f'Promedio diferencia {sum(diferencias) / len(diferencias)}')
  print(f'Maxima diferencia {max(diferencias)} en la posicion {diferencias.index(max(diferencias))}')
    
  plt.plot([entera[i][0] for i in range(len(entera))], diferencia)
  
  plt.xlabel('Cantidad periodistas')
  plt.ylabel('Cota de Aproximación')
  plt.legend()
  plt.show()
  
  
def cota_raiz_b():
  
  resultados_totales = []
  
  for promedio in range(6, 31, 4):
    resultados = []
    
    armar_sets(100, promedio)
    
    for test in generados:
      if test > 300:
        break
      jugadores, subconjuntos = leer_archivo(f'generados/{test}.txt')
      b = max(len(subset) for subset in subconjuntos)
      entera = len(programacion_lineal(jugadores, subconjuntos))
      relajada = len(aproximacion(jugadores, subconjuntos))
      
      print(f'Periodistas: {test}, promedio: {promedio}, b: {b}, raiz b: {math.sqrt(b)} relajada/entera: {relajada/entera}')
      
      resultados.append([promedio, test, b, entera, relajada])

    plt.title(f'Periodistas vs Relajada/Entera (promedio {promedio})')
    plt.plot([resultado[1] for resultado in resultados], [resultado[4]/resultado[3] for resultado in resultados], label=f'Relaja/Entera')
    plt.plot([resultado[1] for resultado in resultados], [math.sqrt(resultado[2]) for resultado in resultados], label=f'Raiz b')
    plt.xlabel('Cantidad periodistas')
    plt.ylabel('Cota de Aproximación')
    plt.legend()
    plt.show()
    resultados_totales.extend(resultados)
    
    for resultado in resultados_totales:
      print(f'Periodistas: {resultado[1]}, promedio: {resultado[0]}, b: {resultado[2]}, raiz b: {math.sqrt(resultado[2])} relajada/entera: {resultado[4]/resultado[3]}')
  
def graficos_detallados():
  global generados
  generados = armar_sets(31, 7) # valores similares a los dados por la catedra
  
  resultados = []
  resultados.append((test_greedy_rapido(), f'Greedy rapido  (7 prom.)'))
  resultados.append((test_greedy_preciso(), f'Greedy preciso  (7 prom.)'))
  resultados.append((test_lineal_entera(), f'Lineal entera  (7 prom.)'))
  resultados.append((test_backtracking(), f'Backtracking (7 prom.)')) 
  resultados.append((test_lineal_relajada(), f'Lineal relajada  (7 prom.)'))

  plt.title('Todos los algoritmos (30 jugadores)')
  mostrar_grafico_cantidad_tiempo(resultados)
  plt.title('Todos los algoritmos (30 jugadores)')
  mostrar_grafico_cantidad_seleccionados(resultados)

  
  plt.title('Greedy Rapido (30 jugadores)')
  mostrar_grafico_cantidad_tiempo([resultados[0]])
  plt.title('Greedy Rapido (30 jugadores)')
  mostrar_grafico_cantidad_seleccionados([resultados[0]])

  plt.title('Greedy Preciso (30 jugadores)')
  mostrar_grafico_cantidad_tiempo([resultados[1]])
  plt.title('Greedy Preciso (30 jugadores)')
  mostrar_grafico_cantidad_seleccionados([resultados[1]])
  
  plt.title('Programación Lineal Entera (30 jugadores)')
  mostrar_grafico_cantidad_tiempo([resultados[2]])
  plt.title('Programación Lineal Entera (30 jugadores)')
  mostrar_grafico_cantidad_seleccionados([resultados[2]])
  
  plt.title('Backtracking (30 jugadores)')
  mostrar_grafico_cantidad_tiempo([resultados[3]])
  plt.title('Backtracking (30 jugadores)')
  mostrar_grafico_cantidad_seleccionados([resultados[3]])
  
  plt.title('Programación Lineal Relajada (30 jugadores)')
  mostrar_grafico_cantidad_tiempo([resultados[4]])
  plt.title('Programación Lineal Relajada (30 jugadores)')
  mostrar_grafico_cantidad_seleccionados([resultados[4]])
  
  
  plt.title('Backtracking vs Programación Lineal Entera (30 jugadores)')
  mostrar_grafico_cantidad_tiempo([resultados[2], resultados[3]])
  plt.title('Backtracking vs Programación Lineal Entera (30 jugadores)')
  mostrar_grafico_cantidad_seleccionados([resultados[2], resultados[3]])
  
  plt.title('Programación Lineal Entera vs Relajada (30 jugadores)')
  mostrar_grafico_cantidad_tiempo([resultados[2], resultados[4]])
  plt.title('Programación Lineal Entera vs Relajada (30 jugadores)')
  mostrar_grafico_cantidad_seleccionados([resultados[2], resultados[4]])
  
  plt.title('Greedy Rapido vs Preciso (30 jugadores)')
  mostrar_grafico_cantidad_tiempo([resultados[0], resultados[1]])
  plt.title('Greedy Rapido vs Preciso (30 jugadores)')
  mostrar_grafico_cantidad_seleccionados([resultados[0], resultados[1]])
  
  plt.title('Greedys vs Lineal Relajada (30 jugadores)')
  mostrar_grafico_cantidad_tiempo([resultados[0], resultados[1], resultados[4]])
  plt.title('Greedys vs Lineal Relajada (30 jugadores)')
  mostrar_grafico_cantidad_seleccionados([resultados[0], resultados[1], resultados[4]])
  

if __name__ == '__main__':

  if sys.argv[1] == 'cota-raiz-b':
    cota_raiz_b()
    exit()

  if sys.argv[1] == 'comparacion':
    comparacion_programacion_lineal()
    exit()
  
  if  sys.argv[1] == 'detallado':
    graficos_detallados()
    exit()
  
  algoritmos = set(sys.argv[1].split(','))
  variedad_jugadores = int(sys.argv[2])
  jugadores_prom_por_periodista = [int(promedio) for promedio in sys.argv[3].split(',')]
  
  resultados = []
  
  if variedad_jugadores < max(jugadores_prom_por_periodista) * 2:
    print("La variedad de jugadores debe ser al menos el doble del promedio de jugadores por periodista") 
  
  for promedio_jugadores in jugadores_prom_por_periodista:
    generados = armar_sets(variedad_jugadores, promedio_jugadores)
    
    if 'greedy-r' in algoritmos or 'todos' in algoritmos:
      resultados.append((test_greedy_rapido(), f'Greedy rapido ({promedio_jugadores} prom.)'))
      
    if 'greedy-p' in algoritmos or 'todos' in algoritmos:
      resultados.append((test_greedy_preciso(), f'Greedy preciso ({promedio_jugadores} prom.)'))
    
    if 'entera' in algoritmos or 'todos' in algoritmos:
      resultados.append((test_lineal_entera(), f'Lineal entera ({promedio_jugadores} prom.)'))
      
    if 'backtracking' in algoritmos or 'todos' in algoritmos:
      resultados.append((test_backtracking(), f'Backtracking ({promedio_jugadores} prom.)'))
      
    if 'relajada' in algoritmos or 'todos' in algoritmos:
      resultados.append((test_lineal_relajada(), f'Lineal relajada ({promedio_jugadores} prom.)'))
  
  plt.title(f'Comparativa de tiempo ({variedad_jugadores} jugadores)')
  mostrar_grafico_cantidad_tiempo(resultados)
  plt.title(f'Comparativa de seleccionados ({variedad_jugadores} jugadores)')
  mostrar_grafico_cantidad_seleccionados(resultados)

  
  

  