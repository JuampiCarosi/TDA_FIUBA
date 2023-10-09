import sys


def obtener_cronograma(archivo_txt):

    todo = open(archivo_txt, 'r').read().split('\n')[1:-1]
    todo = list(map(int, todo))

    energia = todo[:len(todo)//2]
    descanso = todo[len(todo)//2:]

    return energia, descanso


def ganacias_por_dia(energia, descanso):
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
            nueva_posibilidad = posibilidad_ayer + \
                min(energia[dia], descanso[dias_acumulados + 1])
            posibilidades_hoy.append(nueva_posibilidad)

            if posibilidades_hoy[mejor_posibilidad] < nueva_posibilidad:
                mejor_posibilidad = dias_acumulados + 1

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
