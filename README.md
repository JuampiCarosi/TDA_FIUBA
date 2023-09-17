# TDA_FIUBA_TP1

Para ejecutar el programa en primer lugar se debe instalar la libreria [matplotlib](https://matplotlib.org/):
```
$ pip3 install matplotlib
```
Una vez instaladas las dependencias, para ejecutar el programa principal se debe correr el archivo tp1.py, pasandole como argumentos los videos en el formato dado por la catedra
```
$ python3 tp1.py videos.txt
```

Tambien hay un ejecutable para realizar tests, el cual genera una cantidad determinada de sets de videos de duracion aleatoria, calcula el tiempo optimo para cada set y realiza dos graficos con los resultados (los mismos graficos que se encuentran en el informe).\
Para ejecutar los tests hay que correr:
```
$ python3 test.py
```

Para visualizar el orden optimo de los videos por consola (en output es tambien en el formato dado por la catedra) se debe ejecutar el programa con el flag `--listar`, por ejemplo:
```
$ python3 tp1.py videos.txt --listar
```


