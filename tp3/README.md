# TDA_FIUBA_TP3

## Integrantes

- Lucas Rafael Aldazabal
- Juan Pablo Carosi Warburg
- Mateo Daniel Vroonland

## Dependencias

Para ejecutar el programa del algoritmo de programación lineal entera y programación lineal relajada se debe instalar la librería [pulp](https://pypi.org/project/PuLP/)

```
$ python -m pip install pulp
```

Para ejecutar el programa de tests en primer lugar se debe instalar la librería [matplotlib](https://matplotlib.org/):

```
$ python -m pip install -U matplotlib
```

## Algoritmos

Para correr alguno de los cuatro algoritmos se debe ingresar el siguiente comando:

```
$ python3 <nombre_algoritmo> <ruta_archivo>
```

Los algoritmos posibles son:

- backtracking.py
- programacion_lineal.py (PLE)
- aproximacion.py (PL relajada)
- greedy.py

Un ejemplo puede ser:

```
$ python3 backtracking.py catedra/200.txt
```

## Creado de sets de datos

Dentro la carpeta de catedra se encuentran todos los archivos provistos por la catedra para asegurar la correcta ejecución de los algoritmos.

Además, dentro de la carpeta de resultados se encuentran los resultados de los algoritmos para cada archivo de la carpeta de catedra, junto al tiempo que tardo en cada caso.

Dentro de la carpeta generados se encuentran los sets de datos creados por nosotros para hacer pruebas de volumen con cada algoritmo.
Para crear nuevos sets de datos se debe ejecutar el siguiente comando:

```
$ python3 generador_sets.py <cantidad_de_jugadores_a_usar> <promedio_de_jugadores_por_subconjunto>
```

Cabe recalcar que los jugadores a utilizar se encuentran dentro de jugadores.txt y posee un máximo de 100 jugadores. Por lo tanto, cantidad_de_jugadores_a_usar debe ser menor o igual a 100.

El rango de jugadores por cada subconjunto esta dado por: promedio_de_jugadores_por_subconjunto.(0.5) y promedio_de_jugadores_por_subconjunto.(1.5), redondeando el resultado para abajo y para arriba respectivamente.

Además, utilizando el siguiente comando se puede verificar que el rango de los sets de datos generados sea el correcto:

```
$ python3 comprobacion.py <numero_archivo_de_corte>
```

Por ejemplo, si se desea verificar los sets de datos hasta el archivo 300.txt, numero_archivo_de_corte debe ser 300.

## Tests

Para correr los tests se debe ejecutar el siguiente comando:

```
$ python3 tests.py <nombre_algoritmo> <cantidad_de_jugadores_a_usar> <promedio_de_jugadores_por_subconjunto>
```

Por cada test se genera un gráfico del tiempo tardado por cada archivo y otro con la longitud de la solución por cada archivo.
Se puede ingresar múltiples algoritmos y promedios de jugadores por subconjunto separados por comas (,). Por ejemplo:

```
$ python3 tests.py backtracking,greedy-r,greedy-p 100 4,8,12
```

Corriendo el siguiente comando, se corren todos los tests para todos los algoritmos utilizando 31 jugadores y un promedio de 7 jugador por subconjunto:

```
$ python3 tests.py detallado
```

En este detallado se crea una combinación de gráficos ya predefinida para cada algoritmo, con el fin de poder comparar selectivamente entre sí.

Para ver la demostración de la cota Raiz(b) en la aproximación de programacion lineal relajada, se debe correr el siguiente comando:

```
$ python3 tests.py cota-raiz-b
```

Por último, corriendo el siguiente comando, se corre un test de comparación de la longitud de la solución entre programación lineal entera y programación lineal relajada para determinar la cota entre las mismas:

```
$ python3 tests.py comparacion
```

### Resultados de los tests

Los resultados de los tests ejecutados se encuentran en la carpeta resultados de este repositorio. Tambien los graficos generados con los mismos se encuentran en sus respectivas carpetas (detallado, cota-raiz-b, comparacion)
