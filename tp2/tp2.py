import sys

def obtener_cronograma(archivo_txt):
  
  todo = open(archivo_txt, 'r').read().split('\n')[1:-1]
  todo = list(map(int, todo))

  energia = todo[:len(todo)//2]
  descanso = todo[len(todo)//2:]
  
  return energia, descanso

def ganacias_por_dia(energia, descanso, optimizar=True):
  dias = []

  for dia in range(len(energia)):
    if dia == 0:
      dias.append([min(energia[0], descanso[0])])
      continue
    
    posibilidades_hoy = []
    
    ante_ayer = dias[dia-2][-1] if dia >= 2 else 0
    ganacia_hoy_descansado = min(energia[dia], descanso[0])
    posibilidades_hoy.append(ante_ayer + ganacia_hoy_descansado)
    
    mejor_posibilidad = 0
    
    posibilidades_ayer = dias[dia-1]
    for dias_acumulados, posibilidad_ayer in enumerate(posibilidades_ayer):
      nueva_posibilidad = posibilidad_ayer + min(energia[dia], descanso[dias_acumulados + 1])
      posibilidades_hoy.append(nueva_posibilidad)
      
      if posibilidades_hoy[mejor_posibilidad] < nueva_posibilidad:
        mejor_posibilidad = dias_acumulados + 1
    
    if optimizar:
      posibilidades_hoy = posibilidades_hoy[:mejor_posibilidad+1]
    dias.append(posibilidades_hoy)
    
  return dias

def organizar_entrenamientos(dias, energia, descanso):
  entrenamientos = []
  dia = len(dias) - 1
  while dia >= 0:
    entrenos_seguidos = len(dias[dia])
    for i in range(entrenos_seguidos):
      entrenamientos.insert(0, 'Entreno')
    dia -= entrenos_seguidos
    
    if dia >= 0:
      entrenamientos.insert(0, 'Descanso')
      dia -= 1
    
  return entrenamientos
  

if __name__ == "__main__":
    archivo_txt = sys.argv[1]
    energia, descanso = obtener_cronograma(archivo_txt)
    dias = ganacias_por_dia(energia, descanso)
    print(dias)
    print("opciones posibles al final: ", len(dias[-1]))
    mejor = max(dias[-1])
    print(mejor)

    entrenamientos = organizar_entrenamientos(dias, energia, descanso)
    print(', '.join(entrenamientos))
  

# arriba: energia = 10, ganancia = 5
# abajo: energia = 12, ganancia = 6 
  
# posiblidad 1: el dia siguiente entrenan "poco": los dos avanzan igual en ganacia, pero el de abajo sigue mas energia (se mantienen relaciones)
  # esfuerzo = 5
  # arriba: energia = 5, ganancia = 10
  # abajo: energia = 7, ganancia = 11 
# posiblidad 2: el dia siguiente entrenan "mucho": el de arriba se cansa y el de abajo tiene todavia mas ganancia y mas o igual energia
  # esfuerzo = 11
  # arriba: energia = 0, ganancia = 15
  # abajo: energia = 1, ganancia = 16
# posiblidad 3: el dia siguiente descansan: ambos vuelven al "reset" de energia pero el de abajo con mas ganancia
  # arriba: energia = 20, ganancia = 5
  # abajo: energia = 20, ganancia = 6
  
  


  
  