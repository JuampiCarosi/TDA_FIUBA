# TDA_FIUBA_TP2

Para ejecutar el programa en primer lugar se debe instalar la libreria [matplotlib](https://matplotlib.org/):

```
$ pip3 install matplotlib
```

Una vez instaladas las dependencias, para ejecutar el programa principal se debe correr el archivo tp1.py, pasandole como argumentos los videos en el formato dado por la catedra

```
$ python3 tp2.py entrenamientos.txt
```

Tambien hay un ejecutable para realizar tests, el cual genera una cantidad determinada de sets de entrenamientos de cansancio y ganancia aleatoria, calcula la maxima ganancia para cada set y realiza dos graficos con los resultados (los mismos graficos que se encuentran en el informe).\
Para ejecutar los tests hay que correr:

```
$ python3 test.py
```

Para visualizar la secuencia de entrenamiento-descanso para llegar a la maxima ganancia se debe ejecutar el programa con el flag `--listar`, por ejemplo:

```
$ python3 tp2.py entrenamientos.txt --listar
```
